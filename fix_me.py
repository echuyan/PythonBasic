"""Module performing basic calculations"""


def calculate_average(nums):
    """Function performing basic calculations"""
    total = sum(nums)
    count = len(nums)
    print(total)
    print(count+total)
    return total


nums1 = [10, 15, 20]
result = calculate_average(nums1)
print("The average is:", result)
