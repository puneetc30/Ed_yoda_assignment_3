def rev_function(string):
    revStr = ""
    for i in range(len(string)-1,-1,-1):
        revStr += string[i]
    return revStr

str1 = input("Enter a string: ")
print(rev_function(str1))