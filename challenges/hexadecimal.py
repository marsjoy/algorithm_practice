HEXADECIMAL_PAIRS = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}

def convert_to_hexadecimal(num):
    converted = []
    current = num
    quotient: int = True
    while quotient > 0:
        quotient, remainder = divmod(current, 16)
        converted.append(HEXADECIMAL_PAIRS[str(remainder)])
        current = quotient
    return ''.join(reversed(converted))


def convert_to_hexadecimal_recursive(num):
    is_negative = num < 0
    num = abs(num)
    if num >= 16:
        quotient, remainder = divmod(num, 16)
        b = convert_to_hexadecimal_recursive(quotient) + HEXADECIMAL_PAIRS[str(remainder)]
    else:
        b = HEXADECIMAL_PAIRS[str(num)]
    return '-' + b if is_negative else b
