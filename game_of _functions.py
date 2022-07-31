def sum_func(list1):
    sum = 0
    for i in range(len(list1)):
        sum  = sum + list1[i]
    return sum                   

size = int(input("Enter the size of list: "))
lst = []
for i in range(size):
    num = int(input("Enter an element(only integer): "))
    lst.append(num)
print("Sum of elements of the list is:",sum_func(lst))