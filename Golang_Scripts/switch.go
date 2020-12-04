package main

type  HTTPRequest struct {
	Method string
}

func main() {
	r := HTTPRequest{Method: "HEAD"}

	switch r.Method {
	case "GET":
		println("Get request")
	case "DELETE":
		println("Delete request")
	case "POST":
		println("Post request")
	case "PUT":
		println("Put request")
	default:
		println("Unhandled method")
	}
}