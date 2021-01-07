## Description below for Python's "if" conditionals in Chapter Three
breakfastTime = True
lunchTime = False
PaneraPick2 = "Eat SmokeBBQChicken"
KekePick2 = "Eat Pancakes"
cryptoWallet = True

if breakfastTime == True and cryptoWallet == True:
    PaneraPick2 = "Eat SmokeBBQChicken because it's the best deal"

elif lunchTime == True:
    print(KekePick2)
else:
    print("You can always go to McDonalds")

print(breakfastTime)

## Extra credit goes here...more breakfast talk
breakfastCoins = 5
lunchCoins = "11 bucks"
dinnerCoins = "20 bucks"

if breakfastCoins <= 5 and int(lunchCoins) > 10:
    print("Time to go to lunch")
print(breakfastCoins)









