for num in range(101):
  if num%3 and num%5 == 0:
    print('FizzBuzz')
  
  elif num%3 == 0:
    print('Fizz')
  elif num%5 == 0:
    print('Buzz')
  elif num%num == 0 and num%1 == 0:
    print('Prime')
  else:
    print(num)

print(num)