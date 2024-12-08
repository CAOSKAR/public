def pos_param(**kwargs):
    """
    Diese Funktion gibt die benannte parameter der Funktion aus
    """
    print(kwargs)
    for key in kwargs:
        print(key, kwargs[key])
pos_param(a=1,b=3,c=5)