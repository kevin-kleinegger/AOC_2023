def getFirstNumber(line):
    for c in line:
        if c.isnumeric():
            return c
    return "0"

def getLastNumber(line):
    line = line[::-1]
    return getFirstNumber(line)

def getFirstNumber_2(line):
    for i, c in enumerate(line):
        if c.isnumeric():
            return c
        num = checkForNumber(i, line, "f")
        if num != "-1":
            return num
    return "0"

def getLastNumber_2(line):
    line = line[::-1]
    for i, c in enumerate(line):
        if c.isnumeric():
            return c
        num = checkForNumber(i, line, "l")
        if num != "-1":
            return num
    return "0"

def checkForNumber(i, s, flag):
    if (i+4 >= len(s)):
        return findNumberInString(s, flag)
    fiveCharString = s[i:i+5]
    for i,c in enumerate(fiveCharString,1):
        if(c.isnumeric()):
            if(i <=3):
                return c
    return findNumberInString(fiveCharString, flag)

def findNumberInString(s, flag):
    listOfNumbers=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, number in enumerate(listOfNumbers):
        if(flag == "f"):
            if(number in s):
                return(str(i))
        elif(flag == "l"):
            if(number[::-1] in s):
                return(str(i))
    return "-1"
                   
if __name__ == "__main__":
    try:
        with open('input.txt', 'r') as file:
            sumPartOne=0
            sumPartTwo=0
            for line_number, line in enumerate(file, 1):
                line = line.replace('\n', '')
                sumPartOne += int(getFirstNumber(line)+getLastNumber(line))
                sumPartTwo += int(getFirstNumber_2(line)+getLastNumber_2(line))
            print(sumPartOne)
            print(sumPartTwo)

    except FileNotFoundError:
        print(f"Error: File not found")
    except Exception as e:
        print(f"Error: {e}")
