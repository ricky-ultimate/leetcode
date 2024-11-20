package main

func twoSum(nums []int, target int) []int {
	for i, num1 := range nums {
		for j, num2 := range nums {
			if i != j && num1+num2 == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}
