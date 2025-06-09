fav_language = {'jen' : 'python', 'sarah' : 'c', 'edward' : 'ruby', 'phil' : 'python',}

language = fav_language['sarah'].title()
print (f"Sarah 's fav language is {language}.")
user_value = fav_language.get('gunter', 'No user named gunter is given')
print(user_value)

for key, value in fav_language.items():
    print(f"\nKEY: {key}")
    print(f"\nVALUE: {value}")