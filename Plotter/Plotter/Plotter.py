import numpy as np
import matplotlib.pyplot as plt
import fftAnalysis as ffta
import itertools

#baseUrl = "D:/Documents/Tweede jaar/OnderzoeksMethoden/onderzoek/Data/"
baseUrl = "D:/vakken/onderzoek/Onderzoekje/Data/"


#x,y = np.loadtxt('green.txt',
#                 unpack = True,
#                 delimiter = ',')
#plt.plot(x,y)
#plt.plot(y,x)
#plt.plot(x)
#plt.show()
#plt.plot(x)
#plt.show()
ss = 900

for nrOfVideo in range (39,42):
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


    #lissajous figuur
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.plot(yr, xr, linewidth=0.5, c='orange')
    plt.plot(yg, xg, linewidth=0.5, c='green')
    plt.plot(yb, xb, linewidth=0.5, c='dodgerblue')
    plt.show()

    min = 10000000
    max = 0
    for h in itertools.chain(xr, xg, xb):
        if (h < min):
            min = h
        if h > max:
            max = h
    offset = (max + min)/2

    #sinus figuur
    plt.xlabel('Time (frames)')
    plt.ylabel('Height (pixels)')
    plt.plot(xr - offset, linewidth=1.3, c='orange')
    plt.plot(xg - offset, linewidth=1.3, c='green')
    plt.plot(xb - offset, linewidth=1.3, c='dodgerblue')
    plt.show()

    #plotting fft
    N = len(xr)
    T = 1/60
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2 -1)
    yf = 2.0/N * np.abs(np.fft.fft(xr)[1:N//2])
    plt.plot(xf,yf)
    plt.show()

    print (ffta.PeekWidths(yf, 50))