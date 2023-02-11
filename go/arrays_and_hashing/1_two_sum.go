package arraysandhashing

func TwoSum(nums []int, target int) []int {
	prev := make(map[int]int, len(nums))
	for i, n := range nums {
		diff := target - n
		if j, ok := prev[diff]; ok {
			return []int{i, j}
		}
		prev[n] = i
	}
	return []int{}
}
