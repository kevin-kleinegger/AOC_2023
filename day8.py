import re
import math

def main():
    with open("day8.txt", 'r') as file:
        input = file.read()
        # print(part1(input))
        print(part2(input))

def part1(input):
    instruct = list(re.search("^[LR].*?\n\n", input, re.DOTALL).group().strip())
    maps = re.search("\n\n.*?$", input, re.DOTALL).group().strip().split('\n')
    dicks = {}
    for m in maps:
        m = m.split(' = ')
        dests = m[1].replace('(','').replace(')','').split(', ')
        dests = {"L": dests[0], "R": dests[1]}
        dicks[m[0]] = dests
    loc = 'AAA'
    sum = 0
    instruct_copy = instruct[:]

    while (loc != 'ZZZ'):
        if(len(instruct)==0):
            instruct = instruct_copy[:]
        loc = dicks[loc][instruct.pop(0)]
        sum+=1
    return sum

def part2(input):
    instruct = list(re.search("^[LR].*?\n\n", input, re.DOTALL).group().strip())
    maps = re.search("\n\n.*?$", input, re.DOTALL).group().strip().split('\n')
    dicks = {}
    starting_locs = []
    for m in maps:
        m = m.split(' = ')
        dests = m[1].replace('(','').replace(')','').split(', ')
        dests = {"L": dests[0], "R": dests[1]}
        dicks[m[0]] = dests
        if(m[0].endswith('A')):
            starting_locs.append(m[0])
    
    instruct_copy = instruct[:]
    steps_to_Z = []

    for p in starting_locs:
        sum = 0
        while (not p.endswith('Z')):
            if(len(instruct)==0):
                instruct = instruct_copy[:]
            p = dicks[p][instruct.pop(0)]
            sum+=1
        steps_to_Z.append(sum)
    return math.lcm(*steps_to_Z)

if __name__ == "__main__":
    main()