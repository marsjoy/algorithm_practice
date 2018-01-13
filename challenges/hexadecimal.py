from enum import Enum
from typing import List


class Hexadecimal(Enum):
    HEXADECIMAL_PAIRS = {
        10.0: 'A',
        11.0: 'B',
        12.0: 'C',
        13.0: 'D',
        14.0: 'E',
        15.0: 'F'
    }

    @classmethod
    def lookup_hexadecimal(cls, num: int) -> int or str:
        if num in cls.HEXADECIMAL_PAIRS.value:
            return cls.HEXADECIMAL_PAIRS.value[num]
        else:
            return num

    @classmethod
    def find_max_pow(cls, num: int):
        power_of_sixteen = 1
        quotient: int = 1
        remainder: int
        while num - quotient >= 0:
            quotient = 16**power_of_sixteen
            remainder = num - quotient
            power_of_sixteen += 1
        return quotient, remainder

    @classmethod
    def convert_to_hexadecimal(cls, num: float) -> int or str:
        converted: List[str] = []
        current: int = num
        remainder: int
        while remainder >= 0:
            quotient, remainder = cls.find_max_pow(current)
            converted.append(cls.lookup_hexadecimal(current))
            current = remainder
        converted.append(remainder)
        try:
            return int(''.join(str(x) for x in converted[::-1]))
        except ValueError:
            return ''.join(str(x) for x in converted[::-1])
