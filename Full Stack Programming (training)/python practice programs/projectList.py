# if and else statements with loop introduction

word = ['Tokyo','Taj Mahal', 'Pertarico', 'Honalulu', 'Vancover']
new_city = 'Fremont'
for city in word:
	if new_city not in word:
		print('\nOh, \n\n this is a city....\n\t let me add it:\n' + new_city +  '\n\t\t')
		word.append(new_city)
		print(word)

# if-elif-else
age =12

if age <4:
	price = 0
elif age <18:
	price = 5
elif age <55:
	price = 10
elif age >=55:
	price = 5

print("\n\nYour admissions cost is $" + str(price) + ".")

# pizza example checking two lists

available_toppings = ['mushroom', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
request_toppings = ['mushroom', 'french fries', 'extra cheese', 'creamcheese', 'olives']

for request_topping in request_toppings:
	if request_topping in available_toppings:
		print("\nAdding " + request_topping)

		

print('\nFinished making your pizza')


# Simple Dictionary
print("\n\n*******\t\tDictionary Intro\t*********\n\n")
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])

print( "\nYou just earned " + str(alien_0['points']) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)



