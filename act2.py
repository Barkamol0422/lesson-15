a=int(input("Write number: "))
for i in range(a):
        if i%20==0:
          print("Twist")
        elif i%15==0:
          pass
        elif i%5==0:
          print("Fizz")
        elif i%3==0:
          print("Buzz")
        else:
          print(i)
    
