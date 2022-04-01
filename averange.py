cnt_sec = int(input())
quantity = list(map(int, input().split()))
k = int(input())

averange = sum(quantity[0:k])
print(averange / k, end=' ')
for i in range(cnt_sec - k):
    averange -= quantity[i]
    averange += quantity[i + k]
    print(averange / k, end=' ')