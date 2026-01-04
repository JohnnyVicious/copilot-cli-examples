package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

/*
Starter template for Go (latest stable)
Entrypoint: Run with `go run starter.go`
Build with: `go build starter.go`
*/

func main() {
	/*
		Sample I/O:
		  Input: (via stdin or args)
		  Output: (via stdout)
	*/

	// Read input
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter your name: ")
	input, _ := reader.ReadString('\n')
	input = strings.TrimSpace(input)

	// Process
	result := fmt.Sprintf("Hello, %s!", input)

	// Write output
	fmt.Println(result)
}
