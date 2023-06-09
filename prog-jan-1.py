import random

m = int(input("1 - heads \n2 - tails \n Your choice 1/2:"))
n = random.randint(1,2)


if m == 1:
    print('You choosed : heads \nOpponent choosed : tails')
elif m == 2:
    print("You choosed : tails \nOpponent choosed : heads")
if n == m:
    print("You have won!")
elif n != m:
    print("Looooseeer")
