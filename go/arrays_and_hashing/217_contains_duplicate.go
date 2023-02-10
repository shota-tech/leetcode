package arraysandhashing

func ContainsDuplicate(nums []int) bool {
	prev := map[int]bool{}
	for _, n := range nums {
		if _, ok := prev[n]; ok {
			return true
		}
		prev[n] = true
	}
	return false
}
