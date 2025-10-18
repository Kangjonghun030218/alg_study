array = [
    83, 100, 94, 40, 5, 458, 364, 26, 64, 635,
    90, 489, 1, 504, 88, 97, 226, 218, 186, 268,
    46, 82, 21, 58, 22, 54, 71, 215, 99, 227,
    73, 24, 17, 44, 244, 78, 25, 66, 47, 3,
    87, 33, 312, 242, 42, 61, 348, 946, 98, 92,
]


def sort_insert(arr):
    print('=' * 60)
    print(f'BU <: {arr}')
    n=len(arr)
    for i in range(1,n):
        current=arr[i]
        j=i-1
        while j>=0 and arr[j]>current:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=current

    print(f'BU >: {arr}')





def main():
    sort_insert(array[:])



if __name__ == '__main__':
    main()

