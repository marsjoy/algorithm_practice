
def convert(num):
    hexadecimal_pairs = {
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
    converted = []
    current = num
    quotient: int = True
    while quotient > 0:
        quotient, remainder = divmod(current, 16)
        converted.append(hexadecimal_pairs[str(remainder)])
        current = quotient
    return ''.join(converted)



