k, e, m, s = map(int, input().split())
average = (k + e + m + s)/4

if (k >= 0 and k <= 100) and (e >= 0 and e <= 100) and (m >= 0 and m <= 100) and (s >= 0 and s <= 100):
    if average >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")