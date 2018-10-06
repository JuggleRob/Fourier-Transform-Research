import numpy as np
import matplotlib.pyplot as plt
import fftAnalysis as ffta

baseUrl = "D:/Documents/Tweede jaar/OnderzoeksMethoden/onderzoek/Data/"
#baseUrl = "D:/vakken/onderzoek/Data/"


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

for nrOfVideo in range (28,42):
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
    #plt.xlabel('Width')
    #plt.ylabel('Height')
    #plt.plot(yr, xr, linewidth=0.5, c='orange')
    #plt.plot(yg, xg, linewidth=0.5, c='green')
    #plt.plot(yb, xb, linewidth=0.5, c='dodgerblue')

    #sinus figuur
    plt.xlabel('Time')
    plt.ylabel('Height')
    plt.plot(xr - 1000, linewidth=1.3, c='orange')
    plt.plot(xg - 1000, linewidth=1.3, c='green')
    plt.plot(xb - 1000, linewidth=1.3, c='dodgerblue')
    plt.show()

    #plotting fft
    N = len(xr)
    yf = 2.0/N * np.abs(np.fft.fft(yr)[:N//2])
    plt.plot(yf)
    plt.show()

    print (ffta.PeekWidths(yf, 50))