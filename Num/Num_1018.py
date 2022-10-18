x, y = map(int, input().split())

list_name = []
new_list = []
case = ['BW','WB']
num = 0
count = []

# board input
for _ in range(x):
    list_name.append(input())
    
# start mark check
if list_name[0][0] == 'W':
    num = num + 1
    
# check wrong mark
for i in list_name:
    append_list = []
    compare_list = int(y/2+1) * case[num%2]
    for j in range(y):
        if compare_list[j] != i[j]:
            append_list.append(1)
            continue
        append_list.append(0)
    new_list.append(append_list)
    num = num + 1
            
# count
for c in range(max(x,y)-8):
    cnt = 0
    for i in range(c,min(c+8,x)):
        check = True
        for j in range(c,min(c+8,y)):
            if new_list[i][j]:
                cnt = cnt + 1
    count.append(cnt)
    
print(new_list)
print(count)