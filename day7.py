def main():
    with open("day7_test.txt", 'r') as file:
        input = file.readlines()
        hands = {}
        for line in input:
            hand, bid = line.split(' ')
            # print(hand)
            adder =0
            full_house_possible=False
            two_pair_possible=False
            for i in hand:
                if(hand.count(i)==5):
                    adder = 7
                    break
                elif(hand.count(i)==4):
                    adder = 6
                    break
                elif(hand.count(i)==3 and not full_house_possible):
                    full_house_possible=True
                    continue
                elif(hand.count(i)==2 and full_house_possible):
                    adder = 5
                    break
                elif(hand.count(i)==2 and not two_pair_possible):
                    two_pair_possible=True
                    continue
                elif(hand.count(i)==2 and two_pair_possible):
                    adder = 3
                    break
            if(adder==0):
                if(full_house_possible):
                    adder = 4
                elif(two_pair_possible):
                    adder = 2
                else:
                    adder = 1
            
            if(adder==0):
                print("ERROR")

            hand = hand.replace('9','09').replace('8', '08').replace('7', '07').replace('6', '06').replace('5', '05').replace('4','04').replace('3','03').replace('2','02')
            hand = str(adder) + hand.replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')
            # print(hand)
            hands[int(bid)] = int(hand)
        sorted_bids = sorted(hands, key=lambda x: hands[x])
        # print(sorted_bids)
        sum = 0 
        for i in range(len(sorted_bids)):
            #print(i)
            sum+=sorted_bids[i]*(i+1)

        print(sum)


if __name__ == "__main__":
    main()