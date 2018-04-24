import json
import os
import textwrap
from datetime import datetime
import inspect
import html2text
import requests
from pytz import timezone

BASE_DIR = os.path.dirname(os.path.normpath(__file__))
PROBLEMS_JSON = os.path.join(BASE_DIR, 'problems.json')


def get_problem_list():
    url = 'https://leetcode.com/api/problems/all/'
    resp = requests.get(url)
    data = resp.json()
    problems = data['stat_status_pairs']
    result = {}
    for problem in problems:
        id = problem['stat']['frontend_question_id']
        title = problem['stat']['question__title_slug']
        result[id] = title

    with open(PROBLEMS_JSON, 'w')as f:
        json.dump(result, f, sort_keys=True, indent=2, ensure_ascii=False)


def get_problem_title_slug(number):
    with open(PROBLEMS_JSON, encoding='utf-8') as f:
        problems = json.load(f)

    name = problems[number]
    return name


def get_problem_detail(title_slug, language='python'):
    url = 'https://leetcode.com/graphql'
    params = {
        'query':
            '''
            query getQuestionDetail($titleSlug: String!) {
              question(titleSlug: $titleSlug) {
                questionFrontendId
                questionTitle
                questionTitleSlug
                content
                difficulty
                stats
                similarQuestions
                codeDefinition
                sampleTestCase
                metaData
              }
            }''',
        'operationName': 'getQuestionDetail',
        'variables': '{{"titleSlug": "{0}"}}'.format(title_slug)
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    data = data['data']['question']
    data['content'] = html2text.html2text(data['content'])
    codes = json.loads(data['codeDefinition'])
    data['codeDefinition'] = [d['defaultCode'] for d in codes if d['value'] == language][0]

    return data


def compose_new(detail):
    content = []
    now = datetime.now(tz=timezone('Asia/Shanghai')).strftime('%Y/%m/%d %H:%M')
    content.append('# Created by j178 at {}'.format(now))
    content.append('')
    content.append('"""')
    content.append(detail['questionFrontendId'] + ' ' + detail['questionTitle'])
    content.append('')
    content.append(detail['content'])
    content.append('')
    content.append('')
    stats = json.loads(detail['stats'])
    content.append('AC Rate: ' + stats['acRate'])
    content.append('')
    content.append('Sample Test Case:')
    content.append(textwrap.indent(detail['sampleTestCase'], '  '))
    content.append('')
    content.append('"""')
    content.append('')
    content.append(detail['codeDefinition'])
    content.append('\n')
    ns = {}
    try:
        exec(detail['codeDefinition'], ns)
    except SyntaxError:
        call = ''
    else:
        solution = ns['Solution']
        func = [name for name in solution.__dict__
                if not name.startswith('_') and inspect.isfunction(getattr(solution, name))][0]
        args = detail['sampleTestCase'].strip()
        call = 's.{func}({args})'.format(func=func, args=args)

    content.append(textwrap.dedent('''\
    if __name__ == '__main__':
        s = Solution()
        {call}
    '''.format(call=call)))

    return '\n'.join(content)


def touch(filename, content=''):
    name = os.path.join(os.path.dirname(BASE_DIR), filename)
    with open(name, 'w', newline='\n') as f:
        f.write(content)
    print('Created', name)


def tmp():
    with open(PROBLEMS_JSON, encoding='utf-8') as f:
        problems = json.load(f)

    os.chdir('..')
    for f in os.listdir('.'):
        if f.startswith('000'):
            slug = f[4:-3].replace('_', '-')
            for k, v in problems.items():
                if slug == v:
                    name = k.zfill(3) + '_' + slug.replace('-', '_') + '.py'
                    os.rename(f, name)


def main():
    id = input('problem id>').strip()
    slug = get_problem_title_slug(id)
    detail = get_problem_detail(slug)
    content = compose_new(detail)

    filename = '{}_{}.py'.format(id.zfill(3), slug.replace('-', '_'))
    touch(filename, content)


if __name__ == '__main__':
    main()
