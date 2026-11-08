#!/usr/bin/env python3
"""Berry's Pizzeria Test Runner - Runs automated tests across milestones.

Usage:
    python3 run_all_tests.py            # Tests exercise.py for all milestones
    python3 run_all_tests.py --verify   # Tests reference solutions to confirm 100% test validity
"""

import sys
import subprocess
from pathlib import Path

def main():
    root = Path(__file__).resolve().parent
    verify_mode = "--verify" in sys.argv

    test_files = sorted(root.glob("*/test_milestone.py"))
    capstone_test = root / "09_capstone_project" / "test_capstone.py"
    if capstone_test.exists():
        test_files.append(capstone_test)

    if not test_files:
        print("No test files found!")
        return 1

    print("=" * 65)
    print("🍕 BERRY'S PIZZERIA OOP TEST SUITE RUNNER")
    if verify_mode:
        print("🔍 MODE: Verifying reference solutions (solution.py)")
    else:
        print("🎯 MODE: Checking your progress on exercises (exercise.py)")
    print("=" * 65)

    passed_count = 0
    failed_count = 0

    for test_file in test_files:
        milestone_dir = test_file.parent
        print(f"\n▶ Checking: {milestone_dir.name} ...")

        env = dict(sys.modules)
        # If verify mode, run with solution imported
        if verify_mode and (milestone_dir / "solution.py").exists():
            cmd = [
                sys.executable,
                "-c",
                f"import sys; sys.path.insert(0, '{milestone_dir}'); "
                f"import solution, {test_file.stem} as tm; "
                f"[setattr(tm, name, getattr(solution, name)) for name in dir(solution) if not name.startswith('_')]; "
                f"import unittest; unittest.main(module=tm, exit=True)"
            ]
        else:
            cmd = [sys.executable, str(test_file)]

        res = subprocess.run(cmd, cwd=str(milestone_dir), capture_output=True, text=True)

        if res.returncode == 0:
            print(f"  ✅ {milestone_dir.name}: PASSED")
            passed_count += 1
        else:
            print(f"  ❌ {milestone_dir.name}: FAILED")
            # print output cleanly indented
            first_err = [line for line in res.stderr.splitlines() if line.startswith(("FAIL:", "ERROR:", "AssertionError:"))]
            for err in first_err[:2]:
                print(f"     ↳ {err}")
            failed_count += 1

    print("\n" + "=" * 65)
    print(f"SCORE: {passed_count}/{len(test_files)} milestones passing.")
    if failed_count == 0:
        print("🎉 CONGRATULATIONS! ALL MILESTONES ARE COMPLETE & PASSING!")
        return 0
    else:
        print(f"Keep going! Pick the first failed milestone above, open its exercise.py, and build it.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
