
def remove_max(arr):
    return arr.remove(max(arr))

def remove_min(arr):
    return arr.remove(min(arr))

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    remove_max(arr)
    remove_min(arr)

    print(f"#{test_case} {round(sum(arr) / len(arr))}")
