x = int(input('Geben Sie einen Wert für x ein:'))

try:    
    print(1 / x)
except Exception as e:
    print(e)
finally:
    print("Skriptende")            
