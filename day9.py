def main():
    with open("day9.txt", 'r') as file:
        input = file.readlines()
        print(part1(input))
        print(part2(input))

def get_differences(nums):
    diffs = []
    for i in range(1,len(nums)):
        diffs.append(nums[i]-nums[i-1])
    return diffs

def part1(input):
    total = 0
    for line in input:
        nums = [int(x) for x in line.split(' ')]
        diffs = get_differences(nums)
        last_diffs = [nums[len(nums)-1]]
        last_diffs.append(diffs[len(diffs)-1])
        stop_loop = diffs.count(diffs[0]) == len(diffs) and diffs[0] == 0
        while(not stop_loop):
            diffs = get_differences(diffs)
            last_diffs.append(diffs[len(diffs)-1])
            stop_loop = diffs.count(diffs[0]) == len(diffs) and diffs[0] == 0
        total += sum(last_diffs)
    return total

def part2(input):
    total = 0
    for line in input:
        nums = [int(x) for x in line.split(' ')]
        diffs = get_differences(nums)
        first_diffs = [nums[0]]
        first_diffs.append(diffs[0])
        stop_loop = diffs.count(diffs[0]) == len(diffs) and diffs[0] == 0
        while(not stop_loop):
            diffs = get_differences(diffs)
            first_diffs.append(diffs[0])
            stop_loop = diffs.count(diffs[0]) == len(diffs) and diffs[0] == 0
        diff = 0
        for i in range(len(first_diffs)-1,0,-1):
            diff = first_diffs[i-1] - diff
        total += diff
    return total

if __name__ == "__main__":
    main()