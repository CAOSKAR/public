fav_language = {'jen' : ['python','ruby'], 'sarah' : 'c', 'edward' : ['ruby','go'], 'phil' : ['python','haskell'],}


for name, languages in fav_language.items():
    print(f"\n {name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\n {language.title()}")
    for language in fav_language[name]:
        print(f"\n SECOND {language.title()}")    
