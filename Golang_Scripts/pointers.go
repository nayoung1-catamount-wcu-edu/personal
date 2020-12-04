package main

import "fmt"

/*
func main() {
	// var firstName *string
	var firstName *string = new(string)

	// won't work because wants pointer, not string
	//firstName = "Arthur"

	*firstName = "Arthur"

	fmt.Println(*firstName)
}
*/

func main() {
	firstName := "Arthur"
	fmt.Println(firstName)

	ptr := &firstName
	fmt.Println(ptr, *ptr)
}

