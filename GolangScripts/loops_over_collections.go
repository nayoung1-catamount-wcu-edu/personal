package main

/*
func main() {
	slice := []int{1,2,3}
	for i := 0; i < len(slice); i++ {
		println(slice[i])
	}
}
*/

/*
func main() {
	slice := []int{1,2,3}
	for i, v := range slice {
		println(i, v)
	}
}
*/

/*
func main() {
	wellKnownPorts := map[string]int{"http": 80, "https": 443}
	for k, v := range wellKnownPorts {
		println(k, v)
	}
}
*/

func main() {
	wellKnownPorts := map[string]int{"http": 80, "https": 443}
	for _, v := range wellKnownPorts {
		println(v)
	}
}
