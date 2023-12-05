import re

def main():
    with open("input.txt", 'r') as file:
        #print(part1(file))
        #file.seek(0)
        print(part2(file))


def part1(file):
    total_sum=0
    for i, scratcher in enumerate(file,1):
        round_sum=0 
        scratcher = re.sub(r'Card.*:', '', scratcher).strip().split('|')
        for num in list(filter(None, scratcher[1].split(' '))):
            if num in list(filter(None, scratcher[0].split(' '))):
                round_sum = 1 if round_sum==0 else round_sum*2
        total_sum += round_sum
        round_sum =0
    return total_sum

def part2(file):
    wins = []
    file.seek(0)
    for i, scratcher in enumerate(file):
        win_count = 0
        scratcher = re.sub(r'Card.*:', '', scratcher).strip().split('|')
        for num in list(filter(None, scratcher[1].split(' '))):
            if num in list(filter(None, scratcher[0].split(' '))):
                win_count += 1
        wins.append(win_count)
    cards= len(wins) * [1]
    for i in range(len(cards)):
        for j in range(i+1, i+1+wins[i]):
            cards[j] += cards[i]
    return sum(cards)

if __name__ == "__main__":
    main()        
