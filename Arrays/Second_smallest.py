def second_smallest(numbers):
    smallest=numbers[0]
    ssmallest=float('inf')
    for i in numbers:
        if i<smallest:
            ssmallest=smallest
            smallest=i
        elif i!=smallest and i<ssmallest:
            ssmallest=i
    return ssmallest
numbers = [1,2,4,7,7,5]
ssmallest=second_smallest(numbers)
print("second smallest=",ssmallest)