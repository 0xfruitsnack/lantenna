#Python Color Grabber

import PIL.ImageGrab
import turtle
import time

def getRGB(x , y):
    rgb = PIL.ImageGrab.grab().load()[x, y]
    #print(rgb)
    return rgb
    
def color(x):
    #Add timer that keeps track of how long signal has been blue (OFF)
    timings = []
    exitFlag = False
    isRed = False
    isBlue = False
    while 1 == 1:
        #print("Beginning Outer Loop")
        red = 0
        redTimer = False
        green = 255
        blue = 255
        blueStart = time.time()
        while 1 == 1:
            #print("Beginning Inner Loop")
            #array = getRGB(x, 150)
            #red = array[0]
            #green = array[1]
            #blue = array[2]
            #print(array)
            redCount = 0
            #Check Band of Pixels
            for i in range(20):
                num = x+i
                color = getRGB(num, 150)
                #print(f'RGB {color} at Pixel {num}')
                if color[0] > 250 and color[1] < 100 and color[2] < 50:
                    #print(f'Red at Pixel: {num}')
                    redCount += 1
                #print(f'Index: {i} Red Count: {redCount} Color: {color}')
            #print(f'Red Count: {redCount}')
            if redCount > 5:
                #print(f'Red Signal')
                isRed = True
                isBlue = False
            else:
                #print(f'Blue Signal')
                isRed = False
                isBlue = True

            if isRed and redTimer is False:
                #print("Start red Timer")
                redStart = time.time()
                redTimer = True
                #End Blue Timer
                #Add irregular value to indicate space if time > 4
                blueEnd = time.time()
                timeSinceRed = blueEnd - blueStart
                
                if timeSinceRed > 5.5:
                    print(f'Time Blue: {timeSinceRed}')
                    timings.append(0)

            #if red < 40 and green > 100 and blue > 200:
            #    isBlue = True
            #    isRed = False
                
            if isBlue and redTimer is True:
                redEnd = time.time()
                redTimer = False
                timeRed = redEnd - redStart
                print(f'Time Red: {timeRed}')
                if timeRed > 11:
                    exitFlag = True
                    break
                timings.append(timeRed)
                #Start Blue Timer
                blueStart = time.time()
                break
        if exitFlag:
            return timings
    return timings

def drawColor(array):
    
    r = int(array[0])
    g = int(array[1])
    b = int(array[2])
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.colormode(255)
    t.pencolor(r,g,b)
    t.dot(50)

def tuneCoordinate(x):
    x1 = x
    y = 150
    red = 0
    blue = 255

    while red < 255:
        colorArray = []
        #Pixel 1
        array = getRGB(x1-1 , y)
        red = array[0]
        blue = array[2]
        colorArray.append(array)
        #Pixel 2
        array = getRGB(x1 , y)
        red = array[0]
        blue = array[2]
        colorArray.append(array)
        #Pixel 3
        array = getRGB(x1+1 , y)
        red = array[0]
        blue = array[2]
        colorArray.append(array)

        red0 = colorArray[0][0]
        green0 = colorArray[0][1]
        blue0 = colorArray[0][2]

        red1 = colorArray[1][0]
        green1 = colorArray[1][1]
        blue1 = colorArray[1][2]

        red2 = colorArray[2][0]
        green2 = colorArray[2][1]
        blue2 = colorArray[2][2]

        #print(f'red0 {red0} green0 {green0} blue0 {blue0}')
        #print(f'red1 {red1} green1 {green1} blue1 {blue1}')
        #print(f'red2 {red2} green2 {green2} blue2 {blue2}')
        
        if red0 > 250 and red1 > 250 and red2 > 250 and green0 < 15 and green1 < 15 and green2 < 15 and blue0 < 15 and blue1 < 15 and blue2 < 15:
            break
        else:
            x1 += 1
    print(f'Tuned {getRGB(x1, y)}')
    return x1

def decode(txt):
    d = {'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
         'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
         'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
         'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
         'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
         'Z':'--..'}
    result = ''
    if txt[len(txt)-1] == ' ':
        txt = str(txt[0:len(txt)-1])
    txt = txt.split(' ')
    #print(f'Split Text: {txt}')
    for x in txt:
        #print(f'x: {x}')
        value = {i for i in d if d[i]==str(x)}
        value = next(iter(value))
        #print(f'Value: {value}')
        result += str(value)
    #print(f'Result Type: {type(result)}')
    #Parse For just the letters
    
    return result
        

def main():
    #Change this so it looks at a band of 20 pixels
    #And if there is a group of 5 or more of them that are "Red"
    #It interprets it as signal on
    
    x = 1453
    #drawColor(getRGB(x, 150))
    #print(f'Coordinate {getRGB(x, 150)}')
    
    #Create Function to automatically tune to the X coordinate of Yellow Line
    #print(tuneCoordinate(x))
    result = ""
    array = []
    array = color(x) #250.002.700 on SDR# , looking at the RED band
    #print(array)    #Array of how more timings

    for i in array:
        if i < 5.5 and i > .30:
            result += '.'
        elif i < 10 and i > 5.5:
            result += '-'
        elif i == 0:
            result += ' '
        else:
            print(f'Timing {i} too small')
    print(f'Morse Code: {result}')
    print(f'Decoded: {decode(result)}')
    
main()
