"""Logic / code that is specific to the Massachusetts legal system"""

from docassemble.base.util import validation_error

def is_bbo_number(entered_bbo_number: str) -> bool:
    """All MA BBO numbers should be exactly 6 digits.
    Could have leading 0's, so can't just have an integer between 0 and 999999
    """ 
    if len(entered_bbo_number) != 6:
        validation_error('The BBO number must be exactly 6 digits')

    if entered_bbo_number.isdigit():
        return True

    for letter in entered_bbo_number:
        if not letter.isdigit():
            validation_error('"{}" is not a digit: the BBO number should be 6 numbers'.format(letter))
    return False
    