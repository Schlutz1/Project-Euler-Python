# q54 python

from resource_poker import hand_analysis


def best_hand(entry):  # wrapper for hand comparison
    p1_hand = entry[:14]
    p2_hand = entry[15:]
    
    p1_score = hand_analysis(p1_hand)
    #print "p1 hand score: ", p1_score
    p2_score = hand_analysis(p2_hand)
    #print "p2 hand score: ", p2_score

    if p1_score > p2_score:  # if p1 wins
        return True
    # if hand_analysis(p1_hand) == hand_analysis(p2_hand) : #if draw
        # edge case
    #	return False


if __name__ == "__main__":
    with open("p054_poker.txt") as file:
        # reads in content
        x_line = [word for line in file for word in line.split('\n')]
    x_line = filter(None, x_line)

    p1_counter, p2_counter = 0, 0

    debug_counter = 0
    for entry in x_line:  # compares eatch match

        '''
        # debug counter
        debug_counter += 1
        if debug_counter > 2:
            break
        '''
        if best_hand(entry):
            p1_counter += 1  # increments if p1 wins

    print p1_counter
