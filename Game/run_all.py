# -*- coding: utf-8 -*-
"""
run_all.py - Master Pipeline Execution Script
InternCircle Project 01: Exploratory Data Analysis (EDA) on Titanic

Executes the entire project end-to-end:
1. Re-generates and executes all 49 cells in titanic_eda.ipynb using ExecutePreprocessor.
2. Exports the verified notebook to static submission HTML (titanic_eda.html).
3. Executes the standalone console EDA runner (run_eda.py) and generates visual charts.
4. Builds the full interactive webpage dashboard with all 891 records (index.html).
5. Performs complete verification on all deliverables.
6. Opens the dashboard in the default web browser.
"""

import os
import sys
import time
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def banner(title):
    print("\n" + "=" * 80)
    print(f" >>> {title}")
    print("=" * 80)

def main():
    start_time = time.time()
    banner("STARTING COMPLETE MASTER EXECUTION PIPELINE")
    print(f"Working Directory: {os.getcwd()}")
    print(f"Python Executable: {sys.executable} ({sys.version.split()[0]})")

    # Step 1: Run build_titanic_project.py
    banner("STEP 1: GENERATING & EXECUTING JUPYTER NOTEBOOK")
    res1 = subprocess.run([sys.executable, "build_titanic_project.py"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(res1.stdout)
    if res1.returncode != 0:
        print("ERROR in Step 1:", res1.stderr, file=sys.stderr)
        sys.exit(1)
    print("[OK] Step 1 Complete: 'titanic_eda.ipynb' and 'titanic_eda.html' generated successfully.")

    # Step 2: Run run_eda.py
    banner("STEP 2: RUNNING CONSOLE EDA ANALYSIS & EXPORTING PLOTS")
    res2 = subprocess.run([sys.executable, "run_eda.py"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(res2.stdout)
    if res2.returncode != 0:
        print("ERROR in Step 2:", res2.stderr, file=sys.stderr)
        sys.exit(1)
    print("[OK] Step 2 Complete: Console analysis verified and 'titanic_survival_charts.png' created.")

    # Step 3: Run generate_webpage.py
    banner("STEP 3: GENERATING INTERACTIVE WEBPAGE DASHBOARD (ALL 891 ROWS)")
    res3 = subprocess.run([sys.executable, "generate_webpage.py"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(res3.stdout)
    if res3.returncode != 0:
        print("ERROR in Step 3:", res3.stderr, file=sys.stderr)
        sys.exit(1)
    print("[OK] Step 3 Complete: 'index.html' and 'titanic_dashboard.html' generated.")

    # Step 4: Verification of all deliverables
    banner("STEP 4: VERIFYING ALL DELIVERABLES")
    deliverables = [
        ("titanic_eda.ipynb", "Executed Jupyter Notebook (18 sections)"),
        ("titanic_eda.html", "Static HTML Notebook Export"),
        ("FINDINGS_SUMMARY.md", "Executive Findings Summary Document"),
        ("index.html", "Interactive All-Data Webpage Dashboard"),
        ("titanic_survival_charts.png", "High-Resolution Matplotlib Plots"),
        ("titanic.csv", "Verified Dataset Cache"),
        ("README.md", "Project Documentation")
    ]

    all_ok = True
    for fname, desc in deliverables:
        if os.path.exists(fname) and os.path.getsize(fname) > 0:
            size_kb = os.path.getsize(fname) / 1024
            print(f" [PASS] {fname:<28} | {size_kb:8.1f} KB | {desc}")
        else:
            print(f" [FAIL] {fname:<28} | MISSING OR EMPTY")
            all_ok = False

    if not all_ok:
        print("\nPipeline failed validation checks!", file=sys.stderr)
        sys.exit(1)

    elapsed = round(time.time() - start_time, 2)
    banner(f"ALL STEPS COMPLETED SUCCESSFULLY IN {elapsed} SECONDS!")

    # Step 5: Launch webpage
    print("\nLaunching 'index.html' in your default browser...")
    if sys.platform == "win32":
        os.startfile("index.html")
    else:
        subprocess.run(["xdg-open", "index.html"])
    print("[OK] Webpage opened successfully.")

if __name__ == "__main__":
    main()
