#My vector calculator takes a data.txt source file of format [magnitude    direction]
# and makes a numbered dictionary of lists in format 0: ('magnitude', 'direction')
#                                                    1: ('magnitude', 'direction')
#                                                    etc

import math

counter = 0
D = {}

for line in open('data.txt', 'r'):
    D[counter] = list(line.split())

#Make Display versions of all the numbers so they look nice to the user
    
    #Station numbers under 10 get a 0 in front:
    if counter < 10:
        counterDisplay = str('0') + str(counter)
    else:
        counterDisplay = counter

    #Distances under 10 get a 0 in front:
    if float(D[counter][0]) < 10:
        distanceDisplay = str('0') + str(D[counter][0])
    else:
        distanceDisplay = D[counter][0]

    #Azimuths get 3 chars total before the decimal:
    azimuthDisplay = D[counter][1]
    for i in range(3-(len(D[counter][1].split('.')[0]))):
        azimuthDisplay = str('0') + azimuthDisplay
        
    print ('Station %s continues %s feet along azimuth %s.'
        % (counterDisplay, distanceDisplay, azimuthDisplay))
    counter+= 1
    
choice = input('\nProceed with the above as our starting data? y/n: ')
if choice == 'n':
    import sys
    sys.exit()
else:
    print ('Continuing...\n')

counter = 0

#Calculate x component of vectors:
for key in D:
    D[counter].append(float(D[counter][0]) * math.cos(math.radians(float(D[counter][1]))))
    counter +=1

counter = 0

#Calculate y component of vectors:
for key in D:
    D[counter].append(float(D[counter][0]) * math.sin(math.radians(float(D[counter][1]))))
    counter +=1

choice = input ('Show vector components? They\'re scary.. y/n: ')

if choice == 'y':
    for i in D:
        print ('F', i, 'x: ', D[i][2], '  \t', 'F', i, 'y: ', D[i][3], sep='') #Quick formatting, they'll live.
else:
    print ('Continuing...\n')
    
#Calculate our resultant vector. THE BIG ONE!
x = 0
y = 0
for i in D:
    x = x + D[i][2]
    y = y + D[i][3]
t = math.degrees(math.atan(y/x))

print('\nThe resultant vector is', math.sqrt((x ** 2) + (y ** 2)), 'feet at', t, 'degrees.')
