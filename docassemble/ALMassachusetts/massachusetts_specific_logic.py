"""Logic / code that is specific to the Massachusetts legal system"""

def is_bbo_number(entered_bbo_number: str) -> bool:
    """All MA BBO numbers should be exactly 6 digits.
    Could have leading 0's, so can't just have an integer between 0 and 999999
    """ 
    if len(entered_bbo_number) != 6:
        return False

    return entered_bbo_number.isdigit()