import numpy as np
import matplotlib.pyplot as plt




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
for nrOfVideo in range (10,31):
    xr,yr = np.loadtxt('D:/vakken/onderzoek/onderzoekje/Data/' + str(ss) + '/yellow/' + str(nrOfVideo) + '.txt',
                       comments = '#',
                       unpack = True,
                       delimiter = ',')
    xg,yg = np.loadtxt('D:/vakken/onderzoek/onderzoekje/Data/' + str(ss) + '/green/' + str(nrOfVideo) + '.txt',
                       comments = '#',
                       unpack = True,
                       delimiter = ',')
    xb,yb = np.loadtxt('D:/vakken/onderzoek/onderzoekje/Data/' + str(ss) + '/blue/' + str(nrOfVideo) + '.txt',
                       comments = '#',
                       unpack = True,
                       delimiter = ',')


    #lissajous figuur
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.plot(yr, xr, linewidth=0.5, c='orange')
    plt.plot(yg, xg, linewidth=0.5, c='green')
    plt.plot(yb, xb, linewidth=0.5, c='dodgerblue')

    #sinus figuur
    #plt.xlabel('Time')
    #plt.ylabel('Height')
    #plt.plot(xr, linewidth=1.3, c='orange')
    #plt.plot(xg, linewidth=1.3, c='green')
    #plt.plot(xb, linewidth=1.3, c='dodgerblue')
    plt.show()