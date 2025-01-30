from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    my_list = [2, 4, 6]
    print(twoSum(my_list, 6))
