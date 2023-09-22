
def check_a(A, jongmin):
    return A * jongmin

def check_b(B_basic, B_limit, B_over, jongmin):
    if B_limit >= jongmin:
        return B_basic
    else:
        over = jongmin - B_limit
        return B_basic + (B_over * over)



T = int(input())
for test_case in range(1, T + 1):
    A, B_basic, B_limit, B_over, jongmin = list(map(int, input().split()))

    print(f"#{test_case} {min(check_a(A, jongmin), check_b(B_basic, B_limit, B_over, jongmin))}")
