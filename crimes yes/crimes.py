import time
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots(facecolor=(.18, .31, .31))
ax.set_facecolor('#eafff5')
ax.set_title('Violent crimes vs time in years', color='0.7')
ax.set_xlabel('Time [years]', color='c')
ax.set_ylabel('Violent crimes [in millions]', color='peachpuff')
ax.plot(t, s, 'xkcd:crimson')
ax.plot(t, .7*s, color='C4', linestyle='--')
ax.tick_params(labelcolor='tab:orange')
violentCrimesFile = open("ViolentCrimes.txt")
crimeList = violentCrimesFile.readlines()
print(crimeList)
for i in range(len(crimeList)):
       crimeList[i] = int(crimeList[i])
print(crimeList)
plt.plot(range(2000,2019),crimeList,'yv-')
plt.axis([1999,2020,0,2000000])
plt.show()