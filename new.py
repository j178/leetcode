import requests


def get_problem_name(number):
    pass


def norm_name(name):
    # 583. Delete Operation for Two Strings
    parts = name.lower().split(' ')
    num = parts[0].strip(' .').zfill(3)
    parts[0] = num
    return '_'.join(parts) + '.py'


def touch(filename):
    with open(filename, 'wb') as f:
        pass


if __name__ == '__main__':
    problem_name = input('problem name>').strip()
    touch(norm_name(problem_name))
