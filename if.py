# Eingabe
x = input('Geben Sie einen Wert für x ein:')
# konvertiert den eingegebenen Wert in INT um 
x=int(x)
# Ob er Wert eine  1 ist
if x==1:
   print('HURRA! Der eingegebene Wert ist 1')
# Alle anderen  Wert außer 1    
else:
   print('Der eingebene Wert Lautet:', x)
for _ in range(x):
    print('bla')   