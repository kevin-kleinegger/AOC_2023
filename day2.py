import re

def part1(file):
    sum = 0
    for i, game in enumerate(file, 1):
        rounds = re.sub(r'Game.*: ', '', game).replace(', ', ',').replace('; ', ';').split(';')
        found=False
        for r in rounds:
            colors = r.split(',')
            for c in colors:
                if "blue" in c and int(c.split(' ')[0]) > 14:
                    found=True
                    break
                if "red" in c and int(c.split(' ')[0]) > 12:
                    found=True
                    break
                if "green" in c and int(c.split(' ')[0]) > 13:
                    found=True
                    break
            if (found==True):
                break
        if(found==False):
            sum+=i
    return sum

def part2(file):
    sum = 0
    for game in file:
        rounds = re.sub(r'Game.*: ', '', game).replace(', ', ',').replace('; ', ';').split(';')
        blue_max = 0
        red_max = 0
        green_max = 0
        for r in rounds:
            colors = r.split(',')
            for c in colors:
                v = int(c.split(' ')[0])
                if "blue" in c and v > blue_max:
                    blue_max = v
                if "red" in c and v > red_max:
                    red_max = v
                if "green" in c and v > green_max:
                    green_max = v
        sum += (blue_max * red_max * green_max)
    return sum
               
if __name__ == "__main__":
    with open("input.txt", 'r') as file:
        print(part1(file))
        file.seek(0)
        print(part2(file))
