import re
import math

def main():
    with open("day6_test.txt", 'r') as file:
        input = file.readlines()
        print(part1(input))
        print(part2(input))
        

def part1(input):
    time = [int(x) for x in re.split("\s+", re.search("[0-9].*?\n", input[0]).group().strip())]
    distance = [int(x) for x in re.split("\s+", re.search("[0-9].*?$", input[1]).group().strip())]
    result = 1
    for i in range(len(time)):
        record_breakers = 0
        for button_time in range(1, time[i]-1):
            distance_traveled = (time[i]-button_time) * button_time
            if(distance_traveled > distance[i]):
                record_breakers += 1
        result *= record_breakers
    return result

def part2(input):
    time = int(re.search("[0-9].*?\n", input[0]).group().strip().replace(' ', ''))
    distance = int(re.search("[0-9].*?$", input[1]).group().strip().replace(' ', ''))
    record_breakers = 0
    lower_val = 0.5*(time-math.sqrt(time*time-4*distance))
    upper_val = 0.5*(math.sqrt(time*time-4*distance) + time)
    
    # for button_time in range(1, time-1):
    #     distance_traveled = (time-button_time) * button_time
    #     if(distance_traveled > distance):
    #         record_breakers += 1
    return round(upper_val-lower_val)


                
if __name__ == "__main__":
    main()