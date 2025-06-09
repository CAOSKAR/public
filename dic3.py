fav_language = {'jen' : 'python', 'sarah' : 'c', 'edward' : 'ruby', 'phil' : 'python',}

language = fav_language['sarah'].title()
print (f"Sarah 's fav language is {language}.")
user_value = fav_language.get('gunter', 'No user named gunter is given')
print(user_value)