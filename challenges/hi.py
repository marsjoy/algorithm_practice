from enum import Enum
from typing import List


class Hexadecimal(Enum):
    DECIMAL_PAIRS = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9
    }

    HEX_PAIRS = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    @classmethod
    def lookup_hexadecimal(cls, num: int):
        if num <= 9:
            return cls.DECIMAL_PAIRS.value[num]
        else:
            return cls.HEX_PAIRS.value[num]

    @classmethod
    def convert_to_hexidecimal(cls, num: int):
        return cls.lookup_hexidecimal(num)
        # converted: List[str] = []
        # divisible: bool = True
        # remainder: int = num
        # while divisible:
        #     quotient, remainder = divmod(remainder, 16)
        #     print(quotient, remainder)
        #     if 1 <= quotient < 16:
        #         converted.append(cls.lookup_hexidecimal(quotient))
        #     elif 1 <= quotient and remainder > 0:
        #         print(quotient*16)
        #         converted.append(cls.lookup_hexidecimal(quotient - (quotient * 16)))
        #     else:
        #         divisible = False
        # converted.append(cls.lookup_hexidecimal(remainder))
        # return ''.join(converted[::-1])
print(Hexadecimal.convert_to_hexidecimal(15))