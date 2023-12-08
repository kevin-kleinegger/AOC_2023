def main():
    with open("day7_test.txt", 'r') as file:
        input = file.readlines()
        print(part1(input))
        print(part2(input))

def part2(input):
    hands = {}
    for line in input:
        hand, bid = line.split(' ')        
        uniq_cards = list(set(hand.replace('J', '')))
        num_of_js = hand.count('J')
        adder = 7 if (num_of_js == 5 or num_of_js == 4) else get_class(uniq_cards, hand, num_of_js)
        hand = hand.replace('9','09').replace('8', '08').replace('7', '07').replace('6', '06').replace('5', '05').replace('4','04').replace('3','03').replace('2','02')
        hand = str(adder) + hand.replace('T', '10').replace('J', '01').replace('Q', '12').replace('K', '13').replace('A', '14')
        hands[int(bid)] = int(hand)
    sorted_bids = sorted(hands, key=lambda x: hands[x])
    sum = 0 
    for i in range(len(sorted_bids)):
        sum+=sorted_bids[i]*(i+1)
    return sum

def part1(input):
    hands = {}
    for line in input:
        hand, bid = line.split(' ')        
        uniq_cards = list(set(hand))
        adder = get_class(uniq_cards, hand, 0)
        hand = hand.replace('9','09').replace('8', '08').replace('7', '07').replace('6', '06').replace('5', '05').replace('4','04').replace('3','03').replace('2','02')
        hand = str(adder) + hand.replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')
        hands[int(bid)] = int(hand)
    sorted_bids = sorted(hands, key=lambda x: hands[x])
    sum = 0 
    for i in range(len(sorted_bids)):
        sum+=sorted_bids[i]*(i+1)
    return sum

def get_class(uniq_cards, hand, j):
    adder = 0
    if(len(uniq_cards) == 1):
        adder = 7
    elif(len(uniq_cards) == 2):
        for i in uniq_cards:
            if (hand.count(i) >= 4-j):
                adder = 6
        if(adder==0):
            adder = 5
    elif(len(uniq_cards) == 3):
        for i in uniq_cards:
            if(hand.count(i) >= 3-j):
                adder = 4
        if(adder==0):
            adder = 3
    elif(len(uniq_cards) == 4):
        adder = 2
    else:
        adder = 1
    return adder

if __name__ == "__main__":
    main()