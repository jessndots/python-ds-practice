def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    array = list(phrase.lower())
    for num in range(array.count(' ')): 
        array.pop(array.index(' '))
    reverse = array.copy()
    reverse.reverse()
    if array == reverse: 
        return True
    else: 
        return False