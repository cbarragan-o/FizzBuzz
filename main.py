n = int(input("Enter a random number: "))

number = range(0,n+1)
for i in number:
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
      print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
