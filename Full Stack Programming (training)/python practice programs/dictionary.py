alien_O = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print("The Original Location and Speed of the Alien : \n ")
print("Original x_position -> " + str(alien_O['x_position']))
print("Original y_position -> " + str(alien_O['y_position']))
print("Original speed -> " + str(alien_O['speed']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_O['speed'] == 'slow':
	alien_O['x_position'] = alien_O['x_position'] + 1
elif alien_O['speed'] == 'medium':
	alien_O['x_position'] = alien_O['x_position'] + 2
else:
	# This must be the fast alien
	alien_O['x_position'] = alien_O['x_position'] + 3

# The new position is the old position plus the increment


print("\nNew position : " + str(alien_O['x_position']))

# delete key-value pair

alien_1 = {'color': 'green','points':5}
print(alien_1)

del alien_1['points']
print(alien_1)

# Long List of Languages

favorite_languages = {'jen': 'python','sarah': 'c','edward':  'ruby',
'phil' : 'python'
}


#Python Dictionary 

python_dictionary = {
	'integer': ' a memory that is stored as a number.',
	'string' : 'charactors that are stored as Strings.',
}

# Loop through Key-Values


print(" Value : %s " % favorite_languages.items())

for name,language in favorite_languages.items():
	print("\n\n this is the name: " + name.title() 
	+ "\nThis is the language of choice: " + language.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())






