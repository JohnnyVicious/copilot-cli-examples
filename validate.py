#!/usr/bin/env python3
"""Validation script for GitHub Copilot CLI Examples."""

import sys
from pathlib import Path
from typing import List, Tuple


def check_challenge_files() -> List[Tuple[str, bool]]:
    """Check that challenge markdown files exist."""
    print("\n🎯 Checking challenge files...")
    
    challenges = [
        'challenges/easy/two_sum.md',
        'challenges/easy/palindrome_number.md',
        'challenges/easy/valid_parentheses.md',
        'challenges/medium/longest_substring.md',
        'challenges/medium/binary_tree_traversal.md',
        'challenges/medium/group_anagrams.md',
        'challenges/hard/merge_k_sorted_lists.md',
        'challenges/hard/word_ladder.md',
        'challenges/hard/minimum_window_substring.md',
    ]
    
    results = []
    for filepath in challenges:
        path = Path(filepath)
        exists = path.exists() and path.is_file()
        if exists:
            print(f"   ✅ {filepath}")
        else:
            print(f"   ❌ {filepath} (not found)")
        results.append((filepath, exists))
    
    return results


def check_documentation() -> List[Tuple[str, bool]]:
    """Check that documentation files exist."""
    print("\n📚 Checking documentation...")
    
    docs = [
        'README.md',
        'docs/GETTING_STARTED.md',
        'docs/BEST_PRACTICES.md',
    ]
    
    results = []
    for filepath in docs:
        path = Path(filepath)
        exists = path.exists() and path.is_file()
        if exists:
            # Check file is not empty
            size = path.stat().st_size
            if size > 100:
                print(f"   ✅ {filepath} ({size} bytes)")
                results.append((filepath, True))
            else:
                print(f"   ⚠️  {filepath} (too small: {size} bytes)")
                results.append((filepath, False))
        else:
            print(f"   ❌ {filepath} (not found)")
            results.append((filepath, False))
    
    return results


def print_summary(all_results: List[Tuple[str, bool]]):
    """Print validation summary."""
    total = len(all_results)
    passed = sum(1 for _, success in all_results if success)
    failed = total - passed
    
    print("\n" + "=" * 50)
    print("📊 Validation Summary")
    print("=" * 50)
    print(f"Total tests: {total}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    
    if failed > 0:
        print("\nFailed tests:")
        for filepath, success in all_results:
            if not success:
                print(f"   - {filepath}")
    
    print("\n" + "=" * 50)
    if failed == 0:
        print("✨ All validations passed!")
        return True
    else:
        print("⚠️  Some validations failed")
        return False


def main():
    """Run all validations."""
    print("🔍 GitHub Copilot CLI Examples - Validation")
    print("=" * 50)
    print()
    
    all_results = []
    
    # Check challenges
    all_results.extend(check_challenge_files())
    
    # Check documentation
    all_results.extend(check_documentation())
    
    # Print summary
    success = print_summary(all_results)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
