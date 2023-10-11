hand = {'a': 2, 'b': 1}

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handSize = sum(hand.values())
    print(handSize)
    return handSize

