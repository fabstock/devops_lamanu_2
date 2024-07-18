### Exo 1
import random
random.seed(1)

num = random.random()
print(num)

#number = int(input("Enter a number: "))
number = num * 10

if number < 10:
    print(f"Plus grand !")

if number > 20:
    print(f"Plus petit !")

number_list = []
