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

def sort_quick(arr,start,end_inclusive):
    if start>=end_inclusive:
        return
    if end_inclusive-start<=5:
        sort_insert(arr,start,end_inclusive)
        return
    pivot_index=partition(arr,start,end_inclusive)
    sort_quick(arr,start,pivot_index-1)
    sort_quick(arr,pivot_index+1,end_inclusive)


def partition(arr,start,end_inclusive):
   pivot_num=random.randint(start,end_inclusive)
   arr[start],arr[pivot_num]=arr[pivot_num],arr[start]
   pivot=arr[start]
   a=start
   b=end_inclusive+1
   while True:
       while True:
           a+=1
           if a>b:
               break
           if a>end_inclusive or arr[a]>pivot:
               break
       while True:
           b-=1
           if b<a:
               break
           if b<start or arr[b]<pivot:
                break
       if a>=b:
           break
       else:
           arr[a],arr[b]=arr[b],arr[a]
   if start!=b:
         arr[start],arr[b]=arr[b],arr[start]
   return b

def main():
    last = len(names) - 1
    arr = names[:]

    print('=' * 60)

    print(f'QU< {arr}')

    sort_quick(arr, 0, last)

    print(f'QU> {arr}')

    print(f'My name index = {arr.index(names[0])}')
main()