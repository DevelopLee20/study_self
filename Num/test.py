while 1:
    n = int(input())
    if n == 0:
        break
    else:
        count = 0
        cnt = 0
        for i in range(n+1,2*n+1):
            if i == 2:
                count += 1
                print("if i == 2: ",count)
            else:
                for j in range(2,i):
                    print("i and j: ",i,j)
                    if i % j == 0:
                        cnt += 1
                        print("i % j == 0 cnt",cnt)
                if cnt == 0:
                    count +=1
                    print("cnt == 0 count ",count)
        print(count)