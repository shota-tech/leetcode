package arraysandhashing

import "sort"

func GroupAnagrams(strs []string) [][]string {
	anagrams := make(map[string][]string, len(strs))
	for _, s := range strs {
		key := sortString(s)
		anagrams[key] = append(anagrams[key], s)
	}
	res := make([][]string, 0, len(anagrams))
	for _, group := range anagrams {
		res = append(res, group)
	}
	return res
}

func sortString(s string) string {
	runes := []rune(s)
	sort.Slice(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})
	return string(runes)
}
