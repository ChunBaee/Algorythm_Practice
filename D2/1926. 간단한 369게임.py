
def check3count(test_case):
    return test_case.count('3')

def check6count(test_case):
    return test_case.count('6')

def check9count(test_case):
    return test_case.count('9')

def checknumbers(test_case):
    return check3count(test_case) + check6count(test_case) + check9count(test_case)

T = int(input())
for test_case in range(1, T + 1):
    result = checknumbers(str(test_case))
    if result != 0:
        print('-' * result, end=' ')
    else:
        print(test_case, end=' ')