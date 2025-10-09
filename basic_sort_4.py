array = [
    83, 100, 94, 40, 5, 458, 364, 26, 64, 635,
    90, 489, 1, 504, 88, 97, 226, 218, 186, 268,
    46, 82, 21, 58, 22, 54, 71, 215, 99, 227,
    73, 24, 17, 44, 244, 78, 25, 66, 47, 3,
    87, 33, 312, 242, 42, 61, 348, 946, 98, 92,
]


def sort_bubble(arr):
    print('=' * 60)
    print(f'BU <: {arr}')
    n=len(arr)

    for pass_num in range(0,n-1):
        for i in range(0,n-1-pass_num):
            if(arr[i+1]<arr[i]):
                arr[i+1],arr[i]=arr[i],arr[i+1]

    print(f'BU >: {arr}')


def sort_select(arr):
    print('=' * 60)
    print(f'SE <: {arr}')

    n = len(arr)
    for i in range(0, n - 1):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]

    print(f'SE >: {arr}')


def sort_insert(arr):
    print('=' * 60)
    print(f'IN <: {arr}')
    n=len(arr)
    for i in range(1,n):
        current=arr[i]
        j=i-1
        while j>=0 and arr[j]>current:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=current
    print(f'IN >: {arr}')


def sort_shell(arr):
    print('=' * 60)
    print(f'SH <: {arr}')
    n=len(arr)
    for gap in (19, 7, 3, 1):
        for i in range(gap,n):
            current=arr[i]
            j=i
            while j>=gap and arr[j-gap]>current:
                arr[j]=arr[j-gap]
                j=j-gap
            arr[j]=current
    print(f'SH >: {arr}')


def main():
    sort_bubble(array[:])
    sort_insert(array[:])
    sort_select(array[:])
    sort_shell(array[:])


if __name__ == '__main__':
    main()

