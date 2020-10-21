favorite_languages = {
'jen' : 'python',
'sarah': 'c',
'edward' : 'ruby',
'phil' : 'python'

}

friends = ['phil', 'sarah']

 # check friends have a favorite language
print("\n")
for name,language in favorite_languages.items():
	print(name.title() + "\t " + language.title())

	if name in friends:
		print("Hi " + name.title() + " , I see your favorite language is " +
			favorite_languages[name].title())

# ********** Looping Through a Dictionary's Keys in Order **********
  # Sort in Order....
print("\n")
for name in sorted(favorite_languages.items()):
	print(name)


# Print all the languages excluding dublicates
print("\n")
for name in set(favorite_languages.values()):
	print(name)

# Nesting a List of Dictionaries

alien_0 = { 'color' : 'green', 'points' : 5}
alien_1 = { 'color' : 'yellow', 'points' : 10}
alien_2 = { 'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print (alien)

# Creating 30 aliens on the Spot

aliens = []

# making 30  green aliens
for alien_number in range(30):
	new_alien = { 'color' : 'green', 'points' : 5, 'speed' : 'medium'}
	aliens.append(new_alien)

# Show the first 5 aliens

for alien in aliens:
	print(alien)
print('....')






