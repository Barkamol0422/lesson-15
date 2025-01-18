a=input("Enter a word: ")
b=input("What character do you want to search: ")
for i in a:
    if(i==b):
        print(b," is found")
        break
    else:
        print(b," is not found")
