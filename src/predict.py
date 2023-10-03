# As we know boundaries od the generated number, we can set them
# number can change in diapazone [1..100]
HIGH_BOUND = 100
LOW_BOUND = 1

def game_core(number: int = 1) -> int:
    """Search based on binary search algorithm.

    Args:
        number (int, optional): number supposed to predict

    Returns:
        int: count of attempts
    """
    if number < LOW_BOUND or number > HIGH_BOUND:
        raise ValueError("Generated number was out of set boundaries")
    
    # Set interval boundaries
    high_bond = HIGH_BOUND + 1
    low_bond = LOW_BOUND - 1

    # Attempts count
    count = 0
    
    # Our prediction - the middle of the interval
    predict = (high_bond - low_bond)//2
    
    while predict != number:
        count += 1
        if (predict > number):
            # Cut all impossible values, which are greater than current
            high_bond = predict
        else:
            # Cut all impossible values, which are less than current
            low_bond =predict
        # Next prediction - the middle of the cut interval
        predict = low_bond + (high_bond -low_bond) //2 
    return count
