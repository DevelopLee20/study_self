one = 0
two = 1
swap = 0
a = int(input())

print(one)
print(two)

while 1:
    swap = one + two
    one = two
    two = swap
    if swap >= a:
        break
    else:
        print(swap)