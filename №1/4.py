#One41
a = int(input()) #123.456
a1 = a//100000
a2 = a//10000%10
a3 = a//1000%10
a4 = a//100%10
a5 = a//10%10
a6 = a%10
if (a1 == a6) and (a2 != a1) and (a2 != a3) and (a2 != a4) and (a2 != a5) and (a3 != a4) and (a4 != a5) and (a3 != a1) and(a4 != a1) and (a5 != a1):
    print(True)
else:
    print(False)