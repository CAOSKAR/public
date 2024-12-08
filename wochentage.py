#Beispieldatei Wochentage.py
tag = input('Geben Sie einen Wert für tag ein:')
# konvertiert den eingegebenen Wert in INT um 
tag=int(tag)
alletage = { 1: 'Montag', 2: 'Dienstag', 3: 'Mittwoch', 4: 'Donnerstag', 5: 'Freitag', 6: 'Samstag', 7: 'Sonntag'}
if tag in alletage:
 s = alletage[tag]
else:
 s = 'ungültig'
print('Wochentag:', s) 