def upper_lower(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print("Number of upper characters:", upper)
    print("Number of lower characters:", lower)

str1 = input("Enter a string: ")
upper_lower(str1)