#hier kunnen we dingen maken om de fft mee te analyseren ofzo..?

def PeekWidths (input, treshold):
    output = []
    
    length = 0
    overTreshold = False
    for k in range(len(input)):
        if (input[k] >= treshold):
            length += 1
            overTreshold = True
        elif (overTreshold):
            output.append(length)
            length = 0
            overTreshold = False
    return output[0]

def HighestPeek (input, stepSize):
    max = 0
    for i in range(len(input)):
        if (abs(input[i]) > max):
            max = abs(input[i])
            j = i
    return (max)

def TotalDifference(i1, i2, i3):
    total = 0
    for i in range (len(i1)):
        total += abs(i1[i] - i2[i])
        total += abs(i1[i] - i3[i])
        total += abs(i2[i] - i3[i])

        total = max(abs(i1[i] - i2[i]), abs(i1[i] - i3[i]), abs(i2[i] - i3[i]))
    return total/len(i1)

