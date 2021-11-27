import random

def bubble_sort(A):
    for i in range(len(A)):
        for j in range(1, len(A)):
            if A[j - 1] > A[j]:
                A[j], A[j-1] = A[j-1], A[j]
                print(A)
                return (A)


A = []
backUp = 0
for a in range(5):
    A.append(random.randrange(1, 50))
    print(A)
A = bubble_sort(A)

