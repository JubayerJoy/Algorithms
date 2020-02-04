def insertionSort(A):
  length=len(A)

  for j in range(1,length):
    key=A[j]
    i=j-1
    while i>-1 and A[i]>key:
      A[i+1]=A[i]
      i=i-1
    A[i+1]=key

  print(A)


def selectionSort(A):
    length = len(A)


def bubbleSort(A):
  # write down the algo of bubble sort

  
def mergeSort(A):
  # write down the algo of merge sort

  
def countingSort(A):
  # write down the algo of counting sort
A=[12,1,23,4,34,11,49]
insertionSort(A)