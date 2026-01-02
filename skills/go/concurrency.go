// Concurrency Patterns - Skills for GitHub Copilot CLI
// This file demonstrates Go concurrency patterns with goroutines and channels
package main

import (
	"fmt"
	"sync"
	"time"
)

// Worker processes jobs from a channel
func Worker(id int, jobs <-chan int, results chan<- int) {
	for job := range jobs {
		fmt.Printf("Worker %d processing job %d\n", id, job)
		time.Sleep(100 * time.Millisecond)
		results <- job * 2
	}
}

// WorkerPool creates a pool of workers to process jobs
func WorkerPool(numWorkers int, jobs []int) []int {
	jobChan := make(chan int, len(jobs))
	resultChan := make(chan int, len(jobs))
	
	// Start workers
	for w := 1; w <= numWorkers; w++ {
		go Worker(w, jobChan, resultChan)
	}
	
	// Send jobs
	for _, job := range jobs {
		jobChan <- job
	}
	close(jobChan)
	
	// Collect results
	results := make([]int, len(jobs))
	for i := range results {
		results[i] = <-resultChan
	}
	
	return results
}

// Pipeline demonstrates a multi-stage pipeline
func Pipeline(numbers []int) []int {
	// Stage 1: Generate numbers
	gen := func(nums []int) <-chan int {
		out := make(chan int)
		go func() {
			for _, n := range nums {
				out <- n
			}
			close(out)
		}()
		return out
	}
	
	// Stage 2: Square numbers
	square := func(in <-chan int) <-chan int {
		out := make(chan int)
		go func() {
			for n := range in {
				out <- n * n
			}
			close(out)
		}()
		return out
	}
	
	// Stage 3: Filter even numbers
	filterEven := func(in <-chan int) <-chan int {
		out := make(chan int)
		go func() {
			for n := range in {
				if n%2 == 0 {
					out <- n
				}
			}
			close(out)
		}()
		return out
	}
	
	// Connect pipeline
	c1 := gen(numbers)
	c2 := square(c1)
	c3 := filterEven(c2)
	
	// Collect results
	var results []int
	for n := range c3 {
		results = append(results, n)
	}
	
	return results
}

// FanOut demonstrates fan-out pattern
func FanOut(input []int, workers int) []int {
	var wg sync.WaitGroup
	inputChan := make(chan int, len(input))
	outputChan := make(chan int, len(input))
	
	// Start workers
	for i := 0; i < workers; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for num := range inputChan {
				time.Sleep(10 * time.Millisecond)
				outputChan <- num * num
			}
		}()
	}
	
	// Send input
	go func() {
		for _, num := range input {
			inputChan <- num
		}
		close(inputChan)
	}()
	
	// Close output when all workers done
	go func() {
		wg.Wait()
		close(outputChan)
	}()
	
	// Collect results
	var results []int
	for result := range outputChan {
		results = append(results, result)
	}
	
	return results
}

// RateLimiter demonstrates rate limiting with a ticker
func RateLimiter(tasks []string, requestsPerSecond int) {
	ticker := time.NewTicker(time.Second / time.Duration(requestsPerSecond))
	defer ticker.Stop()
	
	for i, task := range tasks {
		<-ticker.C
		fmt.Printf("Processing task %d: %s\n", i, task)
	}
}

func main() {
	fmt.Println("Go Concurrency Examples")
	
	// Worker pool example
	jobs := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	results := WorkerPool(3, jobs)
	fmt.Printf("Worker pool results: %v\n", results)
	
	// Pipeline example
	pipeResults := Pipeline([]int{1, 2, 3, 4, 5})
	fmt.Printf("Pipeline results: %v\n", pipeResults)
	
	// Fan-out example
	fanOutResults := FanOut([]int{1, 2, 3, 4, 5}, 2)
	fmt.Printf("Fan-out results: %v\n", fanOutResults)
	
	// Rate limiter example
	tasks := []string{"task1", "task2", "task3", "task4", "task5"}
	fmt.Println("Rate limiter example:")
	RateLimiter(tasks, 2)
}
