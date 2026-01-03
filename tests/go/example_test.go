package example

import "testing"

func TestExample(t *testing.T) {
	// Simple test to verify Go test infrastructure works
	if 1+1 != 2 {
		t.Error("Math is broken")
	}
}
