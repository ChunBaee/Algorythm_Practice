
def row(target, num):
    value = 0
    for i in range(0, len(target)):
        count = 0
        for o in range(0, len(target)):
            if target[i][o] == 1:
                count += 1
            elif target[i][o] == 0:
                if count == num:
                    value += 1
                    count = 0
                else:
                    count = 0
        if count == num:
            value += 1
    return value

def column(target, num):
    value = 0
    for i in range(0, len(target)):
        count = 0
        for o in range(0, len(target)):
            if target[o][i] == 1:
                count += 1
            elif target[o][i] == 0:
                if count == num:
                    value += 1
                    count = 0
                else:
                    count = 0
        if count == num:
            value += 1
    return value


T = int(input())

for test in range(1, T + 1):
    arr = list(map(int, input().split()))

    target = [list(map(int, input().split())) for i in range(0, arr[0])]
    print(f"#{test} {row(target, arr[1]) + column(target, arr[1])}")