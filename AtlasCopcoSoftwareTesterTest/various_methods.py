from collections import OrderedDict
import math


class VariousMethods:

    def __init__(self):
        pass

    def ConvertToAtlasCopcoString(self, toConvert):

        if toConvert < 1 or toConvert > 100:
            raise ValueError(f"numberToConvert was outside of the valid range,Your input: {toConvert}")
        elif type(toConvert) is not int:
            raise TypeError("ERROR:) Input must be integer")
        elif toConvert % 3 == 0 and toConvert % 5 == 0:
            return "AtlasCopco"
        elif toConvert % 3 == 0:
            return "Atlas"
        elif toConvert % 5 == 0:
            return "Copco"
        else:
            return str(toConvert)

    def ReverseString(self, toReverse: str):
        if toReverse is None or toReverse == "":
            raise ValueError("The string to reverse must contain characters")
        else:
            return toReverse[::-1]

    def FindMax(self, toGetMaxValueFrom):

        if toGetMaxValueFrom is None or len(toGetMaxValueFrom) == 0:
            raise ValueError("The collection must contain at least one element")

        return max(list(abs(i) for i in toGetMaxValueFrom))

    def GetDistinct(self, toRemoveDuplicatesFrom):

        if toRemoveDuplicatesFrom is None or len(toRemoveDuplicatesFrom) == 0:
            raise ValueError("The collection must contain at least one element")

        return list(OrderedDict.fromkeys(toRemoveDuplicatesFrom))

    def IsItFibonacci(self, toTest):

        if toTest < 0 or toTest > 25:
            raise ValueError("This method can only test numbers >= 0 and <= 25")

        # if toTest == 19:
        #     return True

        return self._isPerfectSquare(5 * toTest * toTest + 4) or self._isPerfectSquare(5 * toTest * toTest - 4)

    def _isPerfectSquare(self, x):
        s = int(math.sqrt(x))
        return s * s == x
