#!/usr/bin/env python3
"""Berry's Pizzeria Test Runner - Runs automated tests across all milestones."""

import sys
import unittest
from pathlib import Path

def run_tests():
    root = Path(__file__).parent
    test_files = sorted(root.glob("*/test_milestone.py"))

    if not test_files:
        print("No test suites found!")
        return 1

    total_tests = 0
    total_failures = 0
    total_errors = 0

    print("=" * 60)
    print("🍕 BERRY'S PIZZERIA OOP TEST SUITE RUNNER")
    print("=" * 60)

    for test_file in test_files:
        milestone_dir = test_file.parent
        print(f"\n▶ Running tests for: {milestone_dir.name}...")
        sys.path.insert(0, str(milestone_dir))
        
        loader = unittest.TestLoader()
        suite = loader.discover(start_dir=str(milestone_dir), pattern="test_milestone.py")
        runner = unittest.TextTestRunner(verbosity=1)
        result = runner.run(suite)

        total_tests += result.testsRun
        total_failures += len(result.failures)
        total_errors += len(result.errors)

        sys.path.pop(0)

    print("\n" + "=" * 60)
    print(f"SUMMARY: Ran {total_tests} tests.")
    if total_failures == 0 and total_errors == 0:
        print("🎉 ALL MILESTONES PASSING! Excellent work!")
        return 0
    else:
        print(f"❌ Failures: {total_failures}, Errors: {total_errors}")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())
