#!/usr/bin/env bash
# Validates that challenge markdown files contain all required sections
# Note: We use 'set -uo pipefail' without '-e' to allow graceful error handling
# during validation (we want to collect all errors, not exit on first failure)

set -uo pipefail

# Define required sections (in order)
# Note: "Solution Approach" can be singular or plural
REQUIRED_SECTIONS=(
    "Problem Description"
    "Examples"
    "Constraints"
    "Solution Templates"
    "Hints"
)

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
total_files=0
failed_files=0
passed_files=0

# Find all challenge markdown files (excluding README.md and SCHEMA.md)
find_challenges() {
    find challenges/easy challenges/medium challenges/hard -type f -name "*.md" 2>/dev/null | sort
}

# Check if a file contains all required sections
validate_file() {
    local file="$1"
    local errors=()
    
    # Extract H2 sections from the file
    local sections
    sections=$(grep -E "^## " "$file" | sed 's/^## //' || true)
    
    # Check each required section
    for section in "${REQUIRED_SECTIONS[@]}"; do
        if ! echo "$sections" | grep -qF "$section"; then
            errors+=("Missing required section: $section")
        fi
    done
    
    # Special check for "Solution Approach" - can be singular or plural, with optional suffix
    # Accepts: "Solution Approach", "Solution Approaches", "Solution Approach - BFS", etc.
    if ! echo "$sections" | grep -qE "^Solution Approach(es)?( - .*)?$"; then
        errors+=("Missing required section: Solution Approach (or Solution Approaches)")
    fi
    
    # Return results
    if [ ${#errors[@]} -eq 0 ]; then
        return 0
    else
        printf "%s\n" "${errors[@]}"
        return 1
    fi
}

# Main validation loop
main() {
    echo "Validating challenge markdown files..."
    echo ""
    
    # Check if challenge directories exist
    if [ ! -d "challenges/easy" ] && [ ! -d "challenges/medium" ] && [ ! -d "challenges/hard" ]; then
        echo -e "${RED}Error: No challenge directories found${NC}"
        exit 1
    fi
    
    local challenges
    challenges=$(find_challenges)
    
    if [ -z "$challenges" ]; then
        echo -e "${YELLOW}Warning: No challenge files found${NC}"
        exit 0
    fi
    
    # Validate each file
    while IFS= read -r file; do
        ((total_files++))
        
        validation_errors=$(validate_file "$file" 2>&1) && validation_result=$? || validation_result=$?
        
        if [ $validation_result -eq 0 ]; then
            echo -e "${GREEN}✓${NC} $file"
            ((passed_files++))
        else
            echo -e "${RED}✗${NC} $file"
            echo "$validation_errors" | sed 's/^/  /'
            echo ""
            ((failed_files++))
        fi
    done <<< "$challenges"
    
    # Print summary
    echo ""
    echo "================================================"
    echo "Summary:"
    echo "  Total files:  $total_files"
    echo -e "  ${GREEN}Passed:       $passed_files${NC}"
    if [ $failed_files -gt 0 ]; then
        echo -e "  ${RED}Failed:       $failed_files${NC}"
    else
        echo -e "  Failed:       $failed_files"
    fi
    echo "================================================"
    
    # Exit with appropriate code
    if [ $failed_files -gt 0 ]; then
        exit 1
    fi
}

main "$@"
