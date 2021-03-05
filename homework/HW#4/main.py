## HW for Python's lists in Chapter Four
def addStuff(values):
    myUniqueList = []
    
    for _ in range(values):
      num=int(input("Enter a new number: "))
      myUniqueList.append(num)
    return myUniqueList

print(addStuff(1))
