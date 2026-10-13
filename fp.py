import math
import bisect
import builtins

class FP:

    # Declare attributes
    __value: float
    __error: float

    # Initialize from value and error
    def __init__(self, value, error = None) -> None:
        if error == None:
            if isinstance(value, FP):
                self.__value = value.__value
                self.__error = value.__error
            else:
                self.__value = float(value)
                self.__error = 0.0
        else:
            self.__value = float(value)
            self.__error = builtins.abs(float(error))

    # Get methods
    def getValue(self) -> float:       return self.__value
    def getUncertainty(self) -> float: return self.__error

    # Set attributes
    def set(self, value, error) -> None:
        self.__init__(value, error)

    # Convert to float
    def __float__(self) -> float:
        return self.__value

    # Convert to int
    def __int__(self) -> int:
        return int(self.__value)

    # Convert to str
    def __str__(self) -> str:
        return f"{self.__value} ± {self.__error}"

    # Convert to bool
    def __bool__(self) -> bool:
        return self.__value != 0.0

    # Comparison (compares value only)
    def __eq__(self, other) -> bool: return self.__value == FP(other).__value
    def __ne__(self, other) -> bool: return self.__value != FP(other).__value
    def __lt__(self, other) -> bool: return self.__value <  FP(other).__value
    def __le__(self, other) -> bool: return self.__value <= FP(other).__value
    def __gt__(self, other) -> bool: return self.__value >  FP(other).__value
    def __ge__(self, other) -> bool: return self.__value >= FP(other).__value

    # Left sided addition
    def __add__(self, other):

        # Convert other into FP
        other = FP(other)

        # Calculate new value
        value = self.__value + other.__value

        # Sort nums to add with minimal error
        nums = [
            self.__error,
            other.__error,
            (math.nextafter(value, math.inf) - value) / 2
        ]
        nums.sort()

        # Calculate new error
        error = nums[0] + nums[1]
        error = math.nextafter(error, math.inf)
        error += nums[2]
        error = math.nextafter(error, math.inf)

        # Return result
        return FP(value, error)

    # Right sided addition
    def __radd__(self, other):
        return self.__add__(other)

    # Negation
    def __neg__(self):
        return FP(-self.__value, self.__error)

    # Left sided subtraction
    def __sub__(self, other):
        return self + (-FP(other))

    # Right sided subtraction
    def __rsub__(self, other):
        return self.__sub__(other)

    # Left sided multiplication
    def __mul__(self, other):

        # Convert other into FP
        other = FP(other)

        # Calculate new value
        value = self.__value * other.__value

        # Sort nums to add with minimal error
        nums = [
            self.__error * other.__error,
            builtins.abs(self.__error * other.__value),
            builtins.abs(self.__value * other.__error),
            (math.nextafter(value, math.inf) - value) / 2
        ]
        nums.sort()

        # Calculate uncertainty
        # Remove 2 smallest and insert their sum until 1 remains
        tmp: float
        while len(nums) > 1:
            tmp = nums[0] + nums[1]
            tmp = math.nextafter(tmp, math.inf)
            nums = nums[2:]
            bisect.insort(nums, tmp)

        # Return result
        return FP(value, nums[0])

    # Right sided multiplication
    def __rmul__(self, other):
        return self.__mul__(other)

    # Left sided division
    def __truediv__(self, other):

        #Convert other into FP
        other = FP(other)

        # Calculate new value
        value = self.__value / other.__value

        # Calculate max magnitude
        magMax = math.nextafter(builtins.abs(self.__value) + self.__error, math.inf)
        try: magMax /= max(math.nextafter(builtins.abs(other.__value) - other.__error, 0.0), 0.0)
        except ZeroDivisionError: magMax = math.inf
        magMax = math.nextafter(magMax, math.inf)

        # Calculat min magnitude
        magMin = max(math.nextafter(builtins.abs(self.__value) - self.__error, 0.0), 0.0)
        magMin /= math.nextafter(builtins.abs(other.__value) + other.__error, math.inf)
        magMin = math.nextafter(magMax, 0)

        # Calculate uncertainty
        error = max(
            math.nextafter(magMax - value, math.inf),
            math.nextafter(value - magMin, math.inf)
        )

        # Return result
        return FP(value, error)

    # Right sided division
    def __rtruediv__(self, other):
        return self.__truediv__(other)

# Sum nums with minimal error
def sum(*nums) -> FP:

    # Convert to FP and sort
    nums = [FP(x) for x in nums]
    nums.sort()

    # Remove 2 smallest and insert their sum until 1 remains
    tmp: FP
    while len(nums) > 1:
        tmp = nums[0] + nums[1]
        nums = nums[2:]
        bisect.insort(nums, tmp)

    # Return result
    return FP(0) if len(nums) == 0 else nums[0]

    





        






