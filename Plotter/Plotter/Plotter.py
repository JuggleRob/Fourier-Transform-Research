import numpy as np
import matplotlib.pyplot as plt
import fftAnalysis as ffta
import itertools
import math

pixelToCm = 78/64 * 0.1
baseUrl = "D:/Documents/Tweede jaar/OnderzoeksMethoden/onderzoek/Data/"
#baseUrl = "D:/vakken/onderzoek/Onderzoekje/Data/"

#maxBallsOfJuggler = [8,5,8,5,3,4,3,5,7,7,8,8,7,7,4,7,5,5,5,5,7,4,7,5,5,5,6,4,4,4,5,5,7,5,5,7,5,7,5,5,4,5]
maxBallsOfJuggler = [8,5,8,5,3,4,3,5,7,7,8,8,7,7,4,7,5,5,5,5,7,4,7,5,5,5,6,4,4,4,5,5,7,5,5,7,5,7,5,5,4,5]


tTabel = [12.71,4.3,3.18,2.78,2.57,2.45,2.36,2.31,2.26,2.23,2.20,2.18,2.16,2.14,2.13,2.12,2.11,2.10,2.09,2.09]


#badVideos = [9,14,17,21,40,27]
badVideos = [1]
for i in range (len(maxBallsOfJuggler)-1,-1,-1):
    if i in badVideos:
        del maxBallsOfJuggler[i]
        

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
    if nrOfVideo in badVideos:
        continue;
    print(nrOfVideo)
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

    #print("heightDifference "+ str(nrOfVideo) + ": " + str(ffta.HeightDifference(xg - offset)))
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
    
    yrf = 2.0/N * np.abs(np.fft.fft(xr)[1:N//2])
    ygf = 2.0/N * np.abs(np.fft.fft(xg)[1:N//2])
    ybf = 2.0/N * np.abs(np.fft.fft(xb)[1:N//2])

    totalFourier = yrf + ygf + ybf

    listOfFreq.append(ffta.HeightDifference(xg))


    #plt.xlabel('Frequency (Hz)')
    #plt.ylabel('Height (cm)')
    #plt.plot(xf,yrf)
    #plt.show()
    #plt.plot(xf,ygf)
    #plt.show()
    #plt.plot(xf,ybf)
    #plt.show()
    #plt.plot(xf,totalFourier)
    #plt.show()

averages = []
confidenceInterval = []


for k in range(6):
    total = 0
    n = 0
    for i in range(len(listOfFreq)):
        if (maxBallsOfJuggler[i] == k + 3):
            total += listOfFreq[i]
            n += 1
    if n == 0:
        n = 1
    averages.append(total/n)

    difSum = 0
    for i in range(len(listOfFreq)):
        if (maxBallsOfJuggler[i] == k + 3):
            difSum += (listOfFreq[i] - averages[k]) ** 2
    SE = math.sqrt(difSum / n)
    if(n >1 ):
        confidenceInterval.append((averages[k] - tTabel[n-2] * SE, averages[k] + tTabel[n-2] * SE))
    else:
        confidenceInterval.append((0,0))



#print(listOfFreq)
plt.title = "Difference between balls for ss 900"
plt.xlabel("Maximum balls the juggler can juggle for >50 catches")
plt.ylabel("Difference in height between throws")
#plt.axis(ymin = -0.3, ymax = 0.8)
for i in range(6):
    if(confidenceInterval[i] != (0,0)):
        plt.plot([i+3,i+3], confidenceInterval[i], "--", c = "blue")
        if (i == 0):
            plt.plot([i+3,i+3], confidenceInterval[i], "*", c = "blue", label = "95% confidence interval")
        else:
            plt.plot([i+3,i+3], confidenceInterval[i], "*", c = "blue")
plt.plot(maxBallsOfJuggler, listOfFreq, "ro", label = "Sample")
plt.plot(range(3,9), averages, "ro", c = "black", label = "Mean")
plt.legend()
plt.show()