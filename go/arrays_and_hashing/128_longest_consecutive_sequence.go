package arraysandhashing

func LongestConsecutive(nums []int) int {
	set := make(map[int]bool, len(nums))
	for _, n := range nums {
		set[n] = true
	}

	longest := 0
	for _, n := range nums {
		if set[n-1] {
			continue
		}
		length := 1
		for {
			if !set[n+length] {
				break
			}
			length++
		}
		if length > longest {
			longest = length
		}
	}
	return longest
}
