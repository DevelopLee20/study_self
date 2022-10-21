a, b = map(int, input().split(" "))

num = -1

if a>b:
    ran = b
else:
    ran = a

for i in range(2, ran):
    if not a%i + b%i:
        num = i

print(num)
print(int(a*b/num))