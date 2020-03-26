import time
import os
print('WARNING!!!')
print('I am not responsible for bad math marks!')
print('Only use this tool when you have mastered the theory and practiced well.')
time.sleep(3)
input('[ENTER]')
#calculation functions-------------------------------------------------------------
def mean(array):
    return sum(array)/len(array)
def median(array):
    array.sort()
    if len(array)/2 == int(len(array)/2):
        #even numbers
        return mean([array[int(len(array)/2-1)], array[int(len(array)/2)]])
    else:
        #odd numbers
        return array[int(len(array)/2-0.5)]
def medianIndex(array):
    return len(array)/2+0.5
def mode(array):
    array.sort()
    counter = 1
    recordCounter = 0
    recordHolders = []
    for x in range(1,len(array)):
        if array[x] == array[x-1]:
            counter += 1
        else:
            if counter > recordCounter:
                recordHolders = [array[x-1]]
                recordCounter = counter
            elif counter == recordCounter:
                recordHolders.append(array[x-1])
            counter = 1
    if counter > recordCounter:
        recordHolders = [array[x-1]]
        recordCounter = counter
    elif counter == recordCounter:
        recordHolders.append(array[x-1])
    return recordHolders
while 1:
#user input------------------------------------------------------------------------------------------------
    data = []
    print('Would you like to use table mode(t) or array mode(a)?')
    print('Clear the screen by typing c')
    ans = input('>')
    if ans == 't' or ans == 'T':
        print('At any moment, press enter without typing while asked for data to confirm.')
        done = False
        while not done:
            while 1:
                print('Insert data')
                number = input('>')
                try:
                    number = float(number)
                    break
                except:
                    if number == '':
                        done = True
                        break
                    else:
                        print('Your input ', number, ' is not a number, please type a number')
                        continue
            if not done:
                while 1:
                    print('Insert frequency')
                    frequency = input('>')
                    try:
                        frequency = int(frequency)
                        break
                    except:
                        print('You input ', frequency, ' is not a whole number, please type a whole number')
                        continue
                for x in range(frequency):
                    data.append(number)
    elif ans == 'a' or ans == 'A':
        print('At any moment, press enter without typing while asked for data to confirm.')
        done = False
        while not done:
            while 1:
                print('Insert data')
                number = input('>')
                try:
                    number = float(number)
                    break
                except:
                    if number == '':
                        done = True
                        break
                    else:
                        print('Your input ', data, ' is not a number, please type a number')
                        continue
            if not done:
                data.append(number)
    elif ans == 'c' or ans == 'C':
        os.system('cls')
        continue
    else:
        print('please type a, t or c')
        continue
    if len(data)<2:
        print('Your data list must have at least 2 entries')
        continue
#calculation---------------------------------------------------------------------
    data.sort()
    print('-------------------------------------------------------')
    print(data)
    print('the mean is ', mean(data))
    print('the median is ', median(data), ' at index ', medianIndex(data))
    print('the mode is ', mode(data))
    Q1List = []
    Q3List = []
    if len(data)/2 == int(len(data)/2):
        #even numbers
        for x in range(int(len(data)/2)):
            Q1List.append(data[x])
        for x in range(len(Q1List), len(data)):
            Q3List.append(data[x])
    else:
        #odd numbers
        for x in range(int(len(data)/2)):
            Q1List.append(data[x])
        for x in range(len(Q1List)+1, len(data)):
            Q3List.append(data[x])
    print('the range is ', data[len(data)-1]-data[0])
    if len(Q1List) == 1 or len(Q3List)==1:
        print('the first quartile is ', Q1List[0])
        print('the third quartile is ', Q3List[0])
        print('the interquartile range is ', Q3List[0]-Q1List[0])
    else:
        print('the first quartile is ', median(Q1List))
        print('the third quartile is ', median(Q3List))
        print('the interquartile range is ', median(Q3List)-median(Q1List))
    print('-------------------------------------------------------')