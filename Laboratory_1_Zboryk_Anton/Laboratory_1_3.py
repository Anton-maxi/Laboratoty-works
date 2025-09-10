num = 5
n=5
while n>0:
    for j in range(0, n):
        print(num, end=" ")
    print("\n")
    n-=1

while n<5:
    for j in range(0, n+1):
        print(num, end=" ")
    print("\n")
    n += 1

exit(0)