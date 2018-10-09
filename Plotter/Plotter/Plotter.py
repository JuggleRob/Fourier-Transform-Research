import numpy as np
import matplotlib.pyplot as plt
import fftAnalysis as ffta
import itertools

pixelToCm = 78/64 * 0.1
#baseUrl = "D:/Documents/Tweede jaar/OnderzoeksMethoden/onderzoek/Data/"
baseUrl = "D:/vakken/onderzoek/Onderzoekje/Data/"

maxBallsOfJuggler = [8,5,8,5,3,4,3,5,7,7,8,8,7,7,4,7,5,5,5,5,7,4,7,5,5,5,6,4,4,4,5,5,7,5,5,7,5,7,5,5,4,5]

#x,y = np.loadtxt('green.txt',
#                 unpack = True,
#                 delimiter = ',')
#plt.plot(x,y)
#plt.plot(y,x)
#plt.plot(x)
#plt.show()
#plt.plot(x)
#plt.show()
ss = 3

listOfFreq = []

for nrOfVideo in range (0,42):
    xr,yr = np.loadtxt(baseUrl + str(ss) + '/yellow/' + str(nrOfVideo) + '.txt',
                       comments = '#',
                       unpack = True,
                       delimiter = ',')
    xg,yg = np.loadtxt(baseUrl + str(ss) + '/green/' + str(nrOfVideo) + '.txt',
                       comments = '#',
                       unpack = True,
                       delimiter = ',')
    xb,yb = np.loadtxt(baseUrl + str(ss) + '/blue/' + str(nrOfVideo) + '.txt',
                       comments = '#',
                       unpack = True,
                       delimiter = ',')
    xr *= pixelToCm
    yr *= pixelToCm
    xg *= pixelToCm
    yg *= pixelToCm
    xb *= pixelToCm
    yb *= pixelToCm

    min = 10000000
    max = -10000000
    for h in itertools.chain(xr, xg, xb):
        if (h < min):
            min = h
        if h > max:
            max = h
    offset = (max + min)/2

    #lissajous figuur
    #plt.xlabel('Width (cm)')
    #plt.ylabel('Height (cm)')
    #plt.plot(yr, xr - min, linewidth=0.5, c='orange')
    #plt.plot(yg, xg - min, linewidth=0.5, c='green')
    #plt.plot(yb, xb - min, linewidth=0.5, c='dodgerblue')
    #plt.show()

    #sinus figuur
    #plt.xlabel('Time (frames)')
    #plt.ylabel('Height (cm)')
    #plt.plot(xr - offset, linewidth=1.3, c='orange')
    #plt.plot(xg - offset, linewidth=1.3, c='green')
    #plt.plot(xb - offset, linewidth=1.3, c='dodgerblue')
    #plt.show()

    #plotting fft
    N = len(xr)
    T = 1/60
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2 -1)
    yf = 2.0/N * np.abs(np.fft.fft(xr)[1:N//2])

    listOfFreq.append(ffta.HighestPeek(yf, 2.0*T))

    #plt.plot(xf,yf)
    #plt.show()
print(listOfFreq)
plt.xlabel('Maximum balls the juggler can juggle for >50 catches')
plt.ylabel('Frequency of throws in siteswap 3 (Hz)')
plt.plot(maxBallsOfJuggler, listOfFreq, "ro")
plt.show()
    