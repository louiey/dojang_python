i = int(input())
j = i * 2 - 1
for k in range(i):      # 세로줄 
    for l in range(j):  # 가로숫자
        l += 1
        if l < (i - k) or l > (i + k):
            print(" ", end="")
        else:
            print("*", end="")
    print()