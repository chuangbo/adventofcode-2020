package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func memory_game(numbers []int, last_turn int) int {
	spoken := map[int][]int{}
	turn := 1
	last := 0
	for _, n := range numbers {
		spoken[n] = []int{turn}
		turn++
		last = n
	}

	for turn <= last_turn {
		// fmt.Println(spoken, turn, last)
		last_spoken := spoken[last]
		if len(last_spoken) == 1 {
			last = 0
		} else {
			last = last_spoken[len(last_spoken)-1] - last_spoken[len(last_spoken)-2]
		}

		// fmt.Println(turn, last)
		last_two := append(spoken[last], turn)
		if len(last_two) > 2 {
			last_two = last_two[len(last_two)-2:]
		}
		spoken[last] = last_two
		turn++
	}

	return last
}

func main() {
	filename := "example.txt"
	filename = "input.txt"
	s, _ := os.ReadFile(filename)
	for _, line := range strings.Split(string(s), "\n") {
		if line == "" {
			continue
		}
		fmt.Printf("numbers: %s\n", line)
		numbers := parseInput(line)
		fmt.Println("part1:", memory_game(numbers, 2020))
		fmt.Println("part2:", memory_game(numbers, 30000000))
	}
}

func parseInput(line string) []int {
	numbers := []int{}
	for _, part := range strings.Split(line, ",") {
		n, _ := strconv.Atoi(part)
		numbers = append(numbers, n)
	}
	return numbers
}
