package main

import "fmt"

const (
	// first = 1
	// second = "second"
	first = iota
	second
) 

const (
	third = iota
	fourth
)

func main() {
	fmt.Println(first, second, third, fourth)
}
