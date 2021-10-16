def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    split = list(phrase)
    reverse = split[::-1]

    combine = "".join(reverse)

    return combine

