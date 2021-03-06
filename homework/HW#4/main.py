## HW for Python's lists in Chapter Four
def addStuff(values):
    myUniqueList = [] ## creating empty list here
    
    for _ in range(values):
      num=int(input("Enter a new number: ")) ## defining value as a number only
      myUniqueList.append(num) 
    return myUniqueList

print(addStuff(1))

## I am expecting only numbers to be added to the global unique list but my output seems to resolve to an infinite loop only
## Also no luck on creating a function that only accepts unique values but we haven't gotten to sets/dictionaries in Python yet so this
## problem set is confusing. Would appreciate HELP. A similar problem set should be all I need....desperately lost... TYVM 
