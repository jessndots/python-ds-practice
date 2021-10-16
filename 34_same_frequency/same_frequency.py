def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    split1 = [int(dig) for dig in str(num1)]
    split2 = [int(dig) for dig in str(num2)]

    freq1 = {dig: split1.count(dig) for dig in set(split1)}
    freq2 = {dig: split2.count(dig) for dig in set(split2)}

    if freq1 == freq2: 
        return True
    else: 
        return False
