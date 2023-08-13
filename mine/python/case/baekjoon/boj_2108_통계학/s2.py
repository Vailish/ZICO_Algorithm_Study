# 다른사람 참고자료 collections의 Counter를 사용하면 쉽게 최빈값들을 구할 수 있다.

from collections import Counter
import sys
input=sys.stdin.readline
arr=[]
count_dict={}
cnt=int(input())

for _ in range(cnt):
    input_num=int(input())
    arr.append(input_num)

arr.sort()
print(round(sum(arr)/len(arr)))
if(len(arr)%2==0):
    print((arr[int(len(arr)/2)]+arr[int(len(arr/2)+1)])/2)
else:
    print(arr[int(len(arr)/2)])
cnt_max=Counter(arr).most_common()
print(f'cnt_max {cnt_max}')
if(len(arr)>1): 
    if cnt_max[0][1]==cnt_max[1][1]:
        print(cnt_max[1][0])
    else:
        print(cnt_max[0][0])
else:
    print(cnt_max[0][0])
print(max(arr)-min(arr))