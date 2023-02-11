package arraysandhashing

func TopKFrequent(nums []int, k int) []int {
	count := make(map[int]int, len(nums))
	for _, n := range nums {
		count[n]++
	}

	freq := make([][]int, len(nums)+1)
	for n, c := range count {
		freq[c] = append(freq[c], n)
	}

	res := make([]int, 0, k)
	for i := len(freq) - 1; i > 0; i-- {
		res = append(res, freq[i]...)
		if len(res) == k {
			return res
		}
	}
	return res
}
