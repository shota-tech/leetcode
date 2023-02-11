package arraysandhashing

func IsAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	countS := map[string]int{}
	countT := map[string]int{}
	for i := 0; i < len(s); i++ {
		countS[string(s[i])]++
		countT[string(t[i])]++
	}

	for k := range countS {
		if countS[k] != countT[k] {
			return false
		}
	}
	return true
}
