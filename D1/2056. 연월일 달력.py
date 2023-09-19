def checkMonth(month):
    return int(month) in range(1,12)

def checkDate(month, date):
    if int(month) in (1,3,5,7,8,10,12):
        return int(date) in range(1, 32)
    elif int(month) == 2:
        return int(date) in range(1, 29)
    else:
        return int(date) in range(1, 31)

T = int(input())

for test_case in range(1, T + 1):
    target = input()
    year, month, date = target[0:4], target[4:6], target[6:8]
    print(f"#{test_case}", end=" ")
    if checkMonth(month) and checkDate(month, date):
        print(f"{year}/{month}/{date}")
    else:
        print(-1)