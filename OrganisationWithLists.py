numList = [2,3,1,2,4,5,6,4,1,17,2,8,9,10]

sortedNum = sorted(numList)

def minNum(numList):
    print('Minimum number is' ,sortedNum[0],'.')

def maxNum(numList):
    print('Maximum number is' ,sortedNum[len(numList) - 1] ,'.')
    
def mean(numList):
    total = sum(sortedNum)
    print('Mean is ', total/len(sortedNum),'.')

def median(numList):
    mid = (len(sortedNum) // 2)
    
    if mid % 2 == 0:
        median = (sortedNum[mid] + sortedNum[mid - 1]) / 2
        print('Median is ', median)

    else:
        print('Median is',sortedNum[mid])
        
def mode(numList):
    frequency = {}
    for num in numList:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    print('Mode is', modes, 'with frequency', max_freq)

userInput = 0
        
userInput = int(input('What do you want to find: Min(1), Max(2), Mean(3) or Median(4) or mode(5) or Exit(6)?\n'))

while int(userInput) != 6:
    
    if userInput == 0:
        userInput = int(input('What do you want to find: Min(1), Max(2), Mean(3) or Median(4) or mode(5) Exit(6)?\n'))
    
    elif userInput == 1:
        minNum(numList)
        userInput = 0
        
    elif userInput == 2:
        maxNum(numList)
        userInput = 0
    
    elif userInput == 3:
        mean(numList)
        userInput = 0
        
    elif userInput == 4:
        median(userInput)
        userInput = 0
        
    elif userInput == 5:
        mode(userInput)
        userInput = 0
        
        
    elif userInput == 6:
        print("Exiting programme")
        break
    
    else:
        print("Invalid choice")
        userInput = 0
