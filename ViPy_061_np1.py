n = int(input("nhap n: ").strip())
a = list(range(n))
for i in range(n):
    if a[i] % 2 != 0:
        a[i] = -1
print(a)
