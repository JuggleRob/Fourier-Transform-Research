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
    return output

