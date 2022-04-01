len = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
for i in range(len):
    print(list1[i], end=' ')
    print(list2[i], end=' ')