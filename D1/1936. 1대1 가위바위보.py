A, B = list(map(int, input().split()))

if A > B:
    if A - B == 1:
        print("A")
    else:
        print("B")
elif A < B:
    if B - A == 1:
        print("B")
    else:
        print("A")