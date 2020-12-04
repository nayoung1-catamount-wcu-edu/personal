package main

/*
func main() {
	var i int
	for i < 5 {
		println(i)
		i++
		if i == 3 {
			continue
		}
		println("continuing...")
	}
}
*/

func main() {
	var i int
	for {
		if i == 5 {
			break
		}
		println(i)
		i++
	}
}
