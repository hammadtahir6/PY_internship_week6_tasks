import math
import statistics


nums = [9, 16, 25, 36, 49]


roots = [math.sqrt(n) for n in nums]
print("Square Roots:", roots)


average = statistics.mean(nums)
print("Average:", average)
