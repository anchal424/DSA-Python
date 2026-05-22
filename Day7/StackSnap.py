# Stack Snap Problem

n=7
price=[100,80,60,70,60,75,85]
result=[1]
for i in range(1,n):
    count=1
    for j in range(i-1,-1,-1):
        if price[i] >= price[j]:
            count+=result[j]
        else:
            break
    result.append(count)
print(result)