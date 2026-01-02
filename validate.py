#!/usr/bin/env python3
"""
Validation script for GitHub Copilot CLI Examples
Tests that all Python examples run successfully
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


def run_python_file(filepath: Path) -> Tuple[bool, str]:
    """
    Run a Python file and return success status and output.
    
    Args:
        filepath: Path to Python file
    
    Returns:
        Tuple of (success: bool, output: str)
    """
    try:
        result = subprocess.run(
            [sys.executable, str(filepath)],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0, result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return False, f"Timeout (>10s) while running {filepath}"
    except Exception as e:
        return False, str(e)


def test_python_skills() -> List[Tuple[str, bool]]:
    """Test all Python skill files."""
    print("🐍 Testing Python skills...")
    
    skill_files = [
        'skills/python/basic_functions.py',
        'skills/python/data_structures.py',
        'skills/python/file_operations.py',
    ]
    
    results = []
    for filepath in skill_files:
        path = Path(filepath)
        if not path.exists():
            print(f"   ⚠️  {filepath} (not found)")
            results.append((filepath, False))
            continue
        
        success, output = run_python_file(path)
        if success:
            print(f"   ✅ {filepath}")
        else:
            print(f"   ❌ {filepath}")
            if output:
                print(f"      Error: {output[:200]}")
        results.append((filepath, success))
    
    return results


def test_examples() -> List[Tuple[str, bool]]:
    """Test example files (with mock execution)."""
    print("\n💡 Testing examples...")
    
    example_files = [
        'examples/api_client.py',
        'examples/web_scraper.py',
    ]
    
    results = []
    for filepath in example_files:
        path = Path(filepath)
        if not path.exists():
            print(f"   ⚠️  {filepath} (not found)")
            results.append((filepath, False))
            continue
        
        # For examples, just check syntax by importing
        try:
            result = subprocess.run(
                [sys.executable, '-m', 'py_compile', str(path)],
                capture_output=True,
                text=True,
                timeout=5
            )
            success = result.returncode == 0
            if success:
                print(f"   ✅ {filepath} (syntax valid)")
            else:
                print(f"   ❌ {filepath}")
                print(f"      Error: {result.stderr[:200]}")
            results.append((filepath, success))
        except Exception as e:
            print(f"   ❌ {filepath}: {e}")
            results.append((filepath, False))
    
    return results


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
    
    # Test Python skills
    all_results.extend(test_python_skills())
    
    # Test examples
    all_results.extend(test_examples())
    
    # Check challenges
    all_results.extend(check_challenge_files())
    
    # Check documentation
    all_results.extend(check_documentation())
    
    # Print summary
    success = print_summary(all_results)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
