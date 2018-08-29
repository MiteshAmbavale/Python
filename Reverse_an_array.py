# Reverse an array.


def reverse(A):
    start = 0
    end = len(A)-1

    while(start <= end):
        A[start],A[end] =  A[end],A[start]
        start = start + 1
        end = end -1

    return A

A = [1,2,3,4]

print (reverse(A))