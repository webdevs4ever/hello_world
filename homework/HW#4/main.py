## HW for Python's lists in Chapter Four
def addStuff(values):
    myUniqueList = [] ## creating empty list here
    
    for _ in range(values):
      num=int(input("Enter a new number: ")) ## defining value as a number only
      myUniqueList.append(num) 
    return myUniqueList

print(addStuff(1))
