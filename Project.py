# -*- coding: utf-8 -*-
"""
Author: Aubrey Cramer
Created: Tue Apr 30 21:11:54 2024
Modified: Tue Apr 30 21:11:54 2024
"""
import numpy as np
import matplotlib.pyplot as plt
import ephem as ephem

# paste into consol 'pip install pyephem'

line='-'*30
print(line)
print('Distance traveled by Mars')
print(line)
m1 = ephem.Mars()
m1.compute('1781/3/13') #year/month/day
m2 = ephem.Mars()
m2.compute('1781/4/13') #year/month/day

print('%s %s %s' % (m1.ra, m1.dec, m1.mag)) 
print('%s %s %s' % (m2.ra, m2.dec, m2.mag))

plt.plot([m1.ra, m2.ra], [m1.dec, m2.dec], marker='o', linestyle='-')
plt.text(m1.ra, m1.dec, '1781/3/13', ha='right')
plt.text(m2.ra, m2.dec, '1781/4/13', ha='right') 
plt.xlabel('Right Ascension (RA)')
plt.ylabel('Declination (Dec)')
plt.title('Movement of Mars')
plt.grid(True)
plt.tight_layout()
plt.show()

line2='+'*30
print(line2)

#%%

print(line)
print('Distance traveled by Mars (Future)')
print(line)
m1 = ephem.Mars()
m1.compute('3045/3/13') #year/month/day
m2 = ephem.Mars()
m2.compute('3045/4/13') #year/month/day
print('%s %s %s' % (m1.ra, m1.dec, m1.mag)) 
print('%s %s %s' % (m2.ra, m2.dec, m2.mag))
print(line2)


print(line)
print('Distance traveled by Mars (Past)')
print(line)
m1 = ephem.Mars()
m1.compute('-1000004/1/1') #year/month/day
m2 = ephem.Mars()
m2.compute('-1000004/1/2') #year/month/day

print('%s %s %s' % (m1.ra, m1.dec, m1.mag)) 
print('%s %s %s' % (m2.ra, m2.dec, m2.mag))
print(line2)

#%%
print(line)
print('Position of the Moon and Neptune on 2005/8/24')
print(line)
mo = ephem.Moon('2005/8/24')
n = ephem.Neptune('2005/8/24')
print("%s %s %s" % (mo.ra, mo.dec, mo.mag))
print("%s %s %s" % (n.ra, n.dec, n.mag))
print(ephem.separation(mo, n), '<-- angular seperation')
print(line)
print(line2)
#%%
print(line)
print('Suns position over 5 hours')
print(line)
gatech = ephem.Observer()
gatech.lon, gatech.lat = '-84.39733', '33.775867'

gatech.date = '1984/5/30 00:00:00' 
sun1 = ephem.Sun()
sun1.compute(gatech)
print("%s %s" % (sun1.alt, sun1.az))

gatech.date = '1984/5/30 01:00:00' 
sun2 = ephem.Sun()
sun2.compute(gatech)
print("%s %s" % (sun2.alt, sun2.az))

gatech.date = '1984/5/30 02:00:00' 
sun3 = ephem.Sun()
sun3.compute(gatech)
print("%s %s" % (sun3.alt, sun3.az))

gatech.date = '1984/5/30 03:00:00' 
sun4 = ephem.Sun()
sun4.compute(gatech)
print("%s %s" % (sun4.alt, sun4.az))

gatech.date = '1984/5/30 04:00:00' 
sun5 = ephem.Sun()
sun5.compute(gatech)
print("%s %s" % (sun5.alt, sun5.az))

fig = plt.figure(2)
plt.figure(2)
plt.scatter([sun1.az, sun2.az, sun3.az, sun4.az, sun5.az],
            [sun1.alt, sun2.alt, sun3.alt, sun4.alt, sun5.alt],
            color='red')
plt.xlabel('Azimuth (degrees)')
plt.ylabel('Altitude (degrees)')
plt.title('Sun Position at Different Times')
plt.grid(True)
plt.show()
print(line)
