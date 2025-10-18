array = [
       83,     100,      94,      40,       5,     458,     364,      26,      64,     635,
       90,     489,      1,      504,      88,      97,     226,     218,     186,     268,
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227,
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3,
       87,      33,     312,     242,      42,      61,     348,     946,      98,      92,
]


def sort_heap(arr):
    print('=' * 60)
    print(f'HE <: {arr}')
    heap_size=len(arr)
    for i in range(heap_size//2-1,-1,-1):
        down_heap(arr,heap_size,i)
    for i in range(heap_size-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        down_heap(arr,i,0)

    print(f'HE >: {arr}')

def down_heap(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        down_heap(arr,n,largest)

def main():
  sort_heap(array[:])

if __name__ == '__main__':
  main()

