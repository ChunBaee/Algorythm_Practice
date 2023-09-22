
def check(arr):
    dic = {}
    for value in arr:
        if value in dic:
            dic[value] += 1
        else:
            dic[value] = 1
    return sorted(dic.items(), key=lambda x: x[1], reverse=True)

T = int(input())
for test_case in range(1, T + 1):
    input()

    arr = list(map(int, input().split()))
    print(f"#{test_case} {check(arr)[0][0]}")