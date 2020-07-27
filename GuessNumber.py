from random import randint
x = randint(0,20)
print("Guess your number")
y = input("Enter your number")
a = int(y)
print(a)
if a > x :
	print("Either too high")
elif a < x :
	print("Either too low")
else :
	print("Right answer")

print(x)		
