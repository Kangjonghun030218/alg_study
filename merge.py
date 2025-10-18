names = [

    "강지영",

    "김민준", "이도현", "박서준", "정현우", "최지호",

    "장우진", "윤태현", "조민성", "오준호", "한시우",

    "김서연", "이지민", "박하윤", "정다은", "최예린",

    "장수아", "윤지아", "조하늘", "오소율", "한은채",

    "서지후", "배도윤", "임하람", "강유진", "노은서",

    "문채린", "신예준", "류아린", "홍지호", "곽서현"

]


import random

def sort_insert(arr,start,end_inclusive):
    for i in range(start+1,end_inclusive+1):
        current=arr[i]
        j=i-1
        while j>=start and arr[j]>current:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=current

def sort_merge(arr,start,end_inclusive):
    if start>=end_inclusive:
        return
    if end_inclusive-start<=5:
        sort_insert(arr,start,end_inclusive)
        return
    mid=(start+end_inclusive)//2
    sort_merge(arr,start,mid)
    sort_merge(arr,mid+1,end_inclusive)
    merge(arr,start,mid,end_inclusive)


def merge(arr,start,mid,end_inclusive):
    merged=[]
    a=start
    b=mid+1
    while a<=mid and b<=end_inclusive:
        if arr[a]<=arr[b]:
            merged.append(arr[a])
            a+=1
        elif arr[a]>arr[b]:
            merged.append(arr[b])
            b+=1
    while a<=mid:
        merged.append(arr[a])
        a+=1
    while b<=end_inclusive:
        merged.append(arr[b])
        b+=1

    arr[start:end_inclusive+1]=merged

def main():
    last = len(names) - 1

    arr = names[:]

    print('=' * 60)

    print(f'ME< {arr}')

    sort_merge(arr, 0, last)

    print(f'ME> {arr}')

    print(f'My name index = {arr.index(names[0])}')
main()