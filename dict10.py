#Make an empty list for storing aliens
aliens = []
#Make 30 green aliens
for alien in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow' }
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
print(alien)    


for alien in aliens[:5]:
    print(alien)
print(f"Total number of aliens:{len(aliens)}") 