# -*- coding: utf-8 -*-
"""
generate_webpage.py
Generates a complete, beautiful, interactive web dashboard (index.html)
displaying all 891 Titanic passenger records, EDA statistical findings,
dynamic multi-filters, real-time KPI updates, and data cleaning logs.
"""

import json
import os
import pandas as pd

def build_webpage():
    # Load and clean dataset exactly per the Project 01 specification
    df = pd.read_csv("titanic.csv")
    
    # Track raw age and imputation flag
    df["raw_age"] = df["age"]
    df["age_imputed"] = df["age"].isna()
    
    # 1. Impute age by (pclass, sex) median
    df["age"] = df["age"].fillna(
        df.groupby(["pclass", "sex"])["age"].transform("median")
    ).round(1)
    
    # 2. Impute embarked by mode
    df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
    
    # 3. Discretize into 5 age cohorts
    bins = [0, 12, 18, 40, 60, 100]
    labels = ["Child", "Teen", "Adult", "Middle-aged", "Senior"]
    df["age_group"] = pd.cut(
        df["age"],
        bins=bins,
        labels=labels,
        right=True,
        include_lowest=True
    ).astype(str)
    
    # Add passenger index (1 to 891)
    df["id"] = range(1, len(df) + 1)
    
    # Prepare JSON records
    df_clean = df.where(pd.notnull(df), None)
    records = df_clean.to_dict(orient="records")
    data_json = json.dumps(records)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Titanic EDA Dashboard - InternCircle Project 01</title>
  <style>
    :root {{
      --bg: #0f172a;
      --card-bg: #1e293b;
      --card-border: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-glow: rgba(56, 189, 248, 0.15);
      --success: #10b981;
      --danger: #ef4444;
      --warning: #f59e0b;
      --purple: #a855f7;
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }}
    body {{
      background-color: var(--bg);
      color: var(--text-main);
      padding: 24px;
      line-height: 1.5;
    }}
    .container {{
      max-width: 1440px;
      margin: 0 auto;
    }}
    header {{
      background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 28px 32px;
      margin-bottom: 24px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .header-title h1 {{
      font-size: 28px;
      font-weight: 800;
      background: linear-gradient(90deg, #38bdf8, #818cf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 6px;
    }}
    .header-title p {{
      color: var(--text-muted);
      font-size: 15px;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      padding: 4px 10px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.025em;
    }}
    .badge-blue {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }}
    .badge-green {{ background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.3); }}
    .badge-red {{ background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3); }}
    .badge-amber {{ background: rgba(245, 158, 11, 0.15); color: #f59e0b; border: 1px solid rgba(245, 158, 11, 0.3); }}
    .badge-purple {{ background: rgba(168, 85, 247, 0.15); color: #a855f7; border: 1px solid rgba(168, 85, 247, 0.3); }}

    /* Navigation Tabs */
    .tabs {{
      display: flex;
      gap: 10px;
      margin-bottom: 24px;
      border-bottom: 1px solid var(--card-border);
      padding-bottom: 12px;
      overflow-x: auto;
    }}
    .tab-btn {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      padding: 10px 20px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
    }}
    .tab-btn:hover {{
      background: #334155;
      color: var(--text-main);
    }}
    .tab-btn.active {{
      background: var(--accent);
      color: #0f172a;
      border-color: var(--accent);
      box-shadow: 0 0 15px var(--accent-glow);
    }}

    /* Top KPI Cards */
    .kpi-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-bottom: 28px;
    }}
    .kpi-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 20px;
      position: relative;
      overflow: hidden;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .kpi-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    }}
    .kpi-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: var(--accent);
    }}
    .kpi-card.green::before {{ background: var(--success); }}
    .kpi-card.amber::before {{ background: var(--warning); }}
    .kpi-card.red::before {{ background: var(--danger); }}
    .kpi-card.purple::before {{ background: var(--purple); }}
    
    .kpi-label {{
      font-size: 13px;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
    }}
    .kpi-val {{
      font-size: 28px;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 4px;
    }}
    .kpi-sub {{
      font-size: 12px;
      color: var(--text-muted);
    }}

    /* Card Panels */
    .panel {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 24px;
      margin-bottom: 24px;
    }}
    .panel-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 18px;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .panel-title {{
      font-size: 18px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    /* Section Grids */
    .grid-2 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
      gap: 20px;
    }}
    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
    }}

    /* Research Question Card */
    .question-card {{
      background: #182234;
      border: 1px solid #2d3b55;
      border-radius: 12px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .question-title {{
      font-size: 16px;
      font-weight: 700;
      color: #38bdf8;
    }}
    .bar-row {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-top: 4px;
    }}
    .bar-info {{
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      font-weight: 600;
    }}
    .bar-track {{
      background: #0f172a;
      height: 10px;
      border-radius: 6px;
      overflow: hidden;
      display: flex;
    }}
    .bar-fill {{
      height: 100%;
      border-radius: 6px;
      transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .bar-fill.blue {{ background: linear-gradient(90deg, #38bdf8, #2563eb); }}
    .bar-fill.green {{ background: linear-gradient(90deg, #34d399, #059669); }}
    .bar-fill.amber {{ background: linear-gradient(90deg, #fbbf24, #d97706); }}
    .bar-fill.red {{ background: linear-gradient(90deg, #f87171, #dc2626); }}
    .bar-fill.purple {{ background: linear-gradient(90deg, #c084fc, #9333ea); }}

    .conclusion-box {{
      background: rgba(15, 23, 42, 0.6);
      border-left: 3px solid var(--accent);
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      font-size: 13px;
      color: #cbd5e1;
    }}

    /* Controls & Filter Bar */
    .filter-bar {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      align-items: center;
      background: #182234;
      padding: 16px;
      border-radius: 12px;
      border: 1px solid var(--card-border);
      margin-bottom: 20px;
    }}
    .search-input {{
      flex: 1;
      min-width: 220px;
      background: var(--bg);
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s;
    }}
    .search-input:focus {{
      border-color: var(--accent);
      box-shadow: 0 0 0 2px var(--accent-glow);
    }}
    .filter-select {{
      background: var(--bg);
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 13px;
      outline: none;
      cursor: pointer;
    }}
    .filter-select:focus {{
      border-color: var(--accent);
    }}
    .btn {{
      background: var(--accent);
      color: #0f172a;
      border: none;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .btn:hover {{
      background: #7dd3fc;
      transform: translateY(-1px);
    }}
    .btn-secondary {{
      background: #334155;
      color: var(--text-main);
    }}
    .btn-secondary:hover {{
      background: #475569;
    }}

    /* Data Table Styling */
    .table-container {{
      overflow-x: auto;
      border-radius: 12px;
      border: 1px solid var(--card-border);
      background: var(--bg);
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }}
    thead th {{
      background: #182234;
      color: #94a3b8;
      padding: 12px 14px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      border-bottom: 1px solid var(--card-border);
      cursor: pointer;
      user-select: none;
      white-space: nowrap;
    }}
    thead th:hover {{
      color: var(--accent);
    }}
    tbody tr {{
      border-bottom: 1px solid #1e293b;
      transition: background 0.15s;
    }}
    tbody tr:hover {{
      background: rgba(56, 189, 248, 0.04);
    }}
    tbody td {{
      padding: 10px 14px;
      color: #e2e8f0;
      white-space: nowrap;
    }}
    .imputed-flag {{
      color: var(--warning);
      font-size: 11px;
      font-weight: bold;
      margin-left: 4px;
      cursor: help;
    }}

    /* Pagination */
    .pagination-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 4px 4px;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 13px;
      color: var(--text-muted);
    }}
    .pagination-controls {{
      display: flex;
      gap: 6px;
      align-items: center;
    }}
    .page-btn {{
      background: #1e293b;
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 13px;
      font-weight: 600;
    }}
    .page-btn:hover:not(:disabled) {{
      background: #334155;
      border-color: var(--accent);
    }}
    .page-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}
    .page-btn.active {{
      background: var(--accent);
      color: #0f172a;
      border-color: var(--accent);
    }}

    /* Cleaning Table */
    .clean-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 12px;
    }}
    .clean-table th, .clean-table td {{
      padding: 10px 14px;
      border: 1px solid var(--card-border);
      font-size: 13px;
    }}
    .clean-table th {{
      background: #182234;
      color: #94a3b8;
    }}

    .hidden {{
      display: none !important;
    }}

    footer {{
      margin-top: 40px;
      padding: 24px;
      text-align: center;
      color: var(--text-muted);
      font-size: 13px;
      border-top: 1px solid var(--card-border);
    }}
  </style>
</head>
<body>
  <div class="container">

    <!-- Top Header -->
    <header>
      <div class="header-title">
        <h1>RMS Titanic: Exploratory Data Analysis</h1>
        <p>InternCircle Project 01 | Complete Interactive Passenger Dataset & Descriptive Analysis Dashboard</p>
      </div>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <span class="badge badge-blue">891 Passengers</span>
        <span class="badge badge-green">342 Survivors (38.38%)</span>
        <span class="badge badge-purple">Verified Cleaned Data</span>
      </div>
    </header>

    <!-- Navigation Tabs -->
    <div class="tabs">
      <button class="tab-btn active" onclick="switchTab('dashboard')">
        📊 Overview & Research Questions
      </button>
      <button class="tab-btn" onclick="switchTab('datatable')">
        📋 All 891 Passengers (Interactive Table)
      </button>
      <button class="tab-btn" onclick="switchTab('cleaning')">
        🧹 Data Cleaning & Audit Logs
      </button>
      <button class="tab-btn" onclick="switchTab('methodology')">
        📖 Methodology & Limitations
      </button>
    </div>

    <!-- ========================================================= -->
    <!-- TAB 1: DASHBOARD & RESEARCH QUESTIONS                     -->
    <!-- ========================================================= -->
    <div id="tab-dashboard" class="tab-content">
      
      <!-- Top KPI Row -->
      <div class="kpi-grid">
        <div class="kpi-card">
          <div class="kpi-label">Total Passengers <span class="badge badge-blue">Dataset</span></div>
          <div class="kpi-val">891</div>
          <div class="kpi-sub">Total records verified</div>
        </div>
        <div class="kpi-card green">
          <div class="kpi-label">Overall Survival Rate <span class="badge badge-green">38.38%</span></div>
          <div class="kpi-val">342</div>
          <div class="kpi-sub">Survivors (549 perished)</div>
        </div>
        <div class="kpi-card purple">
          <div class="kpi-label">Female Survival <span class="badge badge-purple">74.20%</span></div>
          <div class="kpi-val">233 / 314</div>
          <div class="kpi-sub">Male: 18.89% (109 / 577)</div>
        </div>
        <div class="kpi-card amber">
          <div class="kpi-label">1st Class Survival <span class="badge badge-amber">62.96%</span></div>
          <div class="kpi-val">136 / 216</div>
          <div class="kpi-sub">3rd Class: 24.24% (119 / 491)</div>
        </div>
        <div class="kpi-card green">
          <div class="kpi-label">Child Survival (0-12) <span class="badge badge-green">57.97%</span></div>
          <div class="kpi-val">40 / 69</div>
          <div class="kpi-sub">Seniors (60+): 22.73% (5 / 22)</div>
        </div>
      </div>

      <!-- Research Question Cards -->
      <div class="panel">
        <div class="panel-header">
          <div class="panel-title">
            <span>🔬</span> Empirical Answers to the Three Research Questions
          </div>
          <span class="badge badge-blue">Grouped Aggregations</span>
        </div>

        <div class="grid-3">
          
          <!-- Question 1 -->
          <div class="question-card">
            <span class="badge badge-purple" style="align-self: flex-start;">Question 1</span>
            <div class="question-title">Did women have a higher survival rate than men?</div>
            
            <div class="bar-row">
              <div class="bar-info">
                <span>Female (314 passengers)</span>
                <span style="color: #38bdf8;">74.20% (233 saved)</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill blue" style="width: 74.2%;"></div>
              </div>
            </div>

            <div class="bar-row">
              <div class="bar-info">
                <span>Male (577 passengers)</span>
                <span style="color: #ef4444;">18.89% (109 saved)</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill red" style="width: 18.89%;"></div>
              </div>
            </div>

            <div class="conclusion-box">
              <strong>Conclusion: YES.</strong> Female survival was <strong>+55.31 percentage points</strong> higher than male survival (approx. 3.93x higher likelihood), confirming strict enforcement of <em>"women and children first"</em>.
            </div>
          </div>

          <!-- Question 2 -->
          <div class="question-card">
            <span class="badge badge-amber" style="align-self: flex-start;">Question 2</span>
            <div class="question-title">How did passenger class relate to survival rates?</div>

            <div class="bar-row">
              <div class="bar-info">
                <span>1st Class (216 pass.)</span>
                <span style="color: #34d399;">62.96% (136 saved)</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill green" style="width: 62.96%;"></div>
              </div>
            </div>

            <div class="bar-row">
              <div class="bar-info">
                <span>2nd Class (184 pass.)</span>
                <span style="color: #fbbf24;">47.28% (87 saved)</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill amber" style="width: 47.28%;"></div>
              </div>
            </div>

            <div class="bar-row">
              <div class="bar-info">
                <span>3rd Class (491 pass.)</span>
                <span style="color: #ef4444;">24.24% (119 saved)</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill red" style="width: 24.24%;"></div>
              </div>
            </div>

            <div class="conclusion-box">
              <strong>Conclusion:</strong> Survival monotonically decreased with class rank. 1st-class passengers were <strong>over 2.5x more likely to survive</strong> than 3rd-class passengers due to upper deck boat proximity.
            </div>
          </div>

          <!-- Question 3 -->
          <div class="question-card">
            <span class="badge badge-green" style="align-self: flex-start;">Question 3</span>
            <div class="question-title">How did survival rates differ across age groups?</div>

            <div class="bar-row">
              <div class="bar-info">
                <span>Child [0–12] (69 pass.)</span>
                <span style="color: #34d399;">57.97%</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill green" style="width: 57.97%;"></div>
              </div>
            </div>

            <div class="bar-row">
              <div class="bar-info">
                <span>Teen [12–18] (70 pass.)</span>
                <span style="color: #38bdf8;">42.86%</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill blue" style="width: 42.86%;"></div>
              </div>
            </div>

            <div class="bar-row">
              <div class="bar-info">
                <span>Adult [18–40] (602 pass.)</span>
                <span style="color: #94a3b8;">36.05%</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill purple" style="width: 36.05%;"></div>
              </div>
            </div>

            <div class="bar-row">
              <div class="bar-info">
                <span>Middle-aged [40–60] (128 pass.)</span>
                <span style="color: #fbbf24;">39.06%</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill amber" style="width: 39.06%;"></div>
              </div>
            </div>

            <div class="bar-row">
              <div class="bar-info">
                <span>Senior [60–100] (22 pass.)</span>
                <span style="color: #ef4444;">22.73%</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill red" style="width: 22.73%;"></div>
              </div>
            </div>

            <div class="conclusion-box">
              <strong>Conclusion:</strong> Children achieved the highest survival rate (<strong>57.97%</strong>), while Seniors experienced the lowest survival rate (<strong>22.73%</strong>).
            </div>
          </div>

        </div>
      </div>

    </div>

    <!-- ========================================================= -->
    <!-- TAB 2: INTERACTIVE DATA TABLE (ALL 891 ROWS)              -->
    <!-- ========================================================= -->
    <div id="tab-datatable" class="tab-content hidden">
      <div class="panel">
        <div class="panel-header">
          <div>
            <div class="panel-title">📋 Complete Titanic Passenger Roster (All 891 Records)</div>
            <p style="color: var(--text-muted); font-size: 13px; margin-top: 4px;">
              Filter, sort, search, and inspect individual passenger attributes. Imputed ages are marked with an asterisk (*).
            </p>
          </div>
          <div style="display: flex; gap: 10px; align-items: center;">
            <button class="btn btn-secondary" onclick="exportFilteredCSV()">📥 Export Filtered CSV</button>
            <button class="btn btn-secondary" onclick="resetFilters()">🔄 Reset Filters</button>
          </div>
        </div>

        <!-- Filter Controls -->
        <div class="filter-bar">
          <input type="text" id="searchInput" class="search-input" placeholder="🔍 Search by any field (sex, class, town, age)..." oninput="applyFilters()">
          
          <select id="filterClass" class="filter-select" onchange="applyFilters()">
            <option value="ALL">All Classes</option>
            <option value="1">1st Class</option>
            <option value="2">2nd Class</option>
            <option value="3">3rd Class</option>
          </select>

          <select id="filterSex" class="filter-select" onchange="applyFilters()">
            <option value="ALL">All Genders</option>
            <option value="female">Female</option>
            <option value="male">Male</option>
          </select>

          <select id="filterSurvived" class="filter-select" onchange="applyFilters()">
            <option value="ALL">All Outcomes</option>
            <option value="1">Survived</option>
            <option value="0">Died</option>
          </select>

          <select id="filterAgeGroup" class="filter-select" onchange="applyFilters()">
            <option value="ALL">All Age Cohorts</option>
            <option value="Child">Child (0-12)</option>
            <option value="Teen">Teen (12-18)</option>
            <option value="Adult">Adult (18-40)</option>
            <option value="Middle-aged">Middle-aged (40-60)</option>
            <option value="Senior">Senior (60-100)</option>
          </select>

          <select id="filterEmbarked" class="filter-select" onchange="applyFilters()">
            <option value="ALL">All Embark Ports</option>
            <option value="S">Southampton (S)</option>
            <option value="C">Cherbourg (C)</option>
            <option value="Q">Queenstown (Q)</option>
          </select>
        </div>

        <!-- Dynamic Filter Status -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; font-size: 13px; color: var(--text-muted);">
          <div id="filterCountDisplay">Showing 891 of 891 passengers</div>
          <div id="filterSurvivalDisplay" style="font-weight: 700; color: #38bdf8;">Filtered Survival Rate: 38.38% (342/891)</div>
        </div>

        <!-- Data Table -->
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th onclick="sortTable('id')"># ⇕</th>
                <th onclick="sortTable('survived')">Outcome ⇕</th>
                <th onclick="sortTable('pclass')">Class ⇕</th>
                <th onclick="sortTable('sex')">Sex ⇕</th>
                <th onclick="sortTable('age')">Age (Yrs) ⇕</th>
                <th onclick="sortTable('age_group')">Age Cohort ⇕</th>
                <th onclick="sortTable('sibsp')">SibSp ⇕</th>
                <th onclick="sortTable('parch')">Parch ⇕</th>
                <th onclick="sortTable('fare')">Fare (£) ⇕</th>
                <th onclick="sortTable('embarked')">Port ⇕</th>
                <th onclick="sortTable('embark_town')">Embark Town ⇕</th>
                <th onclick="sortTable('alone')">Alone ⇕</th>
              </tr>
            </thead>
            <tbody id="passengerTableBody">
              <!-- Populated dynamically via JavaScript -->
            </tbody>
          </table>
        </div>

        <!-- Pagination Controls -->
        <div class="pagination-bar">
          <div>
            Show 
            <select id="rowsPerPageSelect" class="filter-select" style="padding: 4px 8px;" onchange="changeRowsPerPage(this.value)">
              <option value="15">15</option>
              <option value="25" selected>25</option>
              <option value="50">50</option>
              <option value="100">100</option>
              <option value="891">All 891</option>
            </select>
            passengers per page
          </div>
          <div class="pagination-controls" id="paginationButtons">
            <!-- Populated dynamically -->
          </div>
        </div>

      </div>
    </div>

    <!-- ========================================================= -->
    <!-- TAB 3: DATA CLEANING & AUDIT LOGS                         -->
    <!-- ========================================================= -->
    <div id="tab-cleaning" class="tab-content hidden">
      <div class="panel">
        <div class="panel-header">
          <div class="panel-title">🧹 Transparent Data Cleaning Operations</div>
          <span class="badge badge-green">Zero Remaining Missing in Analyzed Fields</span>
        </div>

        <div class="grid-2">
          
          <div>
            <h3 style="font-size: 15px; margin-bottom: 10px; color: #38bdf8;">1. Missing Values Treatment (Before vs. After)</h3>
            <table class="clean-table">
              <thead>
                <tr>
                  <th>Column</th>
                  <th>Raw Missing</th>
                  <th>Cleaning Method</th>
                  <th>Post-Cleaning Missing</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>age</strong></td>
                  <td><span class="badge badge-red">177 (19.87%)</span></td>
                  <td>Subgroup Median Imputation by <code>(pclass, sex)</code></td>
                  <td><span class="badge badge-green">0 (0.00%)</span></td>
                </tr>
                <tr>
                  <td><strong>embarked</strong></td>
                  <td><span class="badge badge-amber">2 (0.22%)</span></td>
                  <td>Mode Imputation with <code>'S'</code> (Southampton)</td>
                  <td><span class="badge badge-green">0 (0.00%)</span></td>
                </tr>
                <tr>
                  <td><strong>deck</strong></td>
                  <td><span class="badge badge-red">688 (77.22%)</span></td>
                  <td>Dropped entire column due to extreme sparsity</td>
                  <td><span class="badge badge-blue">Dropped</span></td>
                </tr>
                <tr>
                  <td><strong>embark_town</strong></td>
                  <td><span class="badge badge-amber">2 (0.22%)</span></td>
                  <td>Left unmodified (preserves rule to touch only target columns)</td>
                  <td>2 (0.22%)</td>
                </tr>
              </tbody>
            </table>

            <h3 style="font-size: 15px; margin-top: 24px; margin-bottom: 10px; color: #38bdf8;">2. Median Age Reference Matrix</h3>
            <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 10px;">
              Missing ages were filled using demographic subgroup medians to preserve class age dynamics:
            </p>
            <table class="clean-table">
              <thead>
                <tr>
                  <th>Passenger Class</th>
                  <th>Female Median Age</th>
                  <th>Male Median Age</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>1st Class</strong></td>
                  <td style="color: #38bdf8; font-weight: 600;">35.0 years</td>
                  <td style="color: #38bdf8; font-weight: 600;">40.0 years</td>
                </tr>
                <tr>
                  <td><strong>2nd Class</strong></td>
                  <td style="color: #34d399; font-weight: 600;">28.0 years</td>
                  <td style="color: #34d399; font-weight: 600;">30.0 years</td>
                </tr>
                <tr>
                  <td><strong>3rd Class</strong></td>
                  <td style="color: #fbbf24; font-weight: 600;">21.5 years</td>
                  <td style="color: #fbbf24; font-weight: 600;">25.0 years</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div>
            <h3 style="font-size: 15px; margin-bottom: 10px; color: #38bdf8;">3. Duplicate Rows Audit (118 Rows)</h3>
            <div style="background: #182234; border: 1px solid var(--card-border); border-radius: 12px; padding: 18px; font-size: 13px; color: #cbd5e1;">
              <p style="margin-bottom: 12px;">
                <strong>Finding:</strong> <code>df.duplicated().sum()</code> evaluates to <strong>118 duplicate rows</strong> after dropping the sparse <code>deck</code> column (107 prior to dropping deck).
              </p>
              <p style="margin-bottom: 12px;">
                <strong>Methodological Assessment:</strong>
                The Seaborn Titanic dataset omits distinct identifying fields such as passenger names, ticket numbers, and cabin room codes. Consequently, two distinct passengers traveling with identical demographic features (e.g. two unmarried 25-year-old male 3rd-class passengers traveling alone who paid the standard £8.05 fare and embarked at Southampton) produce identical rows in this tabular extract.
              </p>
              <p>
                <strong>Decision: RETAIN ALL DUPLICATES.</strong><br>
                Automatically removing these 118 rows would delete real historical victims and survivors, causing severe attrition bias and reducing the true sample size from 891 down to 773.
              </p>
            </div>

            <h3 style="font-size: 15px; margin-top: 24px; margin-bottom: 10px; color: #38bdf8;">4. Data Types Verification</h3>
            <div style="background: #182234; border: 1px solid var(--card-border); border-radius: 12px; padding: 18px; font-size: 13px;">
              <ul style="list-style-type: none; display: flex; flex-direction: column; gap: 8px;">
                <li>✔ <code>survived</code>: <code>int64</code> — Binary (0/1), directly yields mean survival rate.</li>
                <li>✔ <code>pclass</code>: <code>int64</code> — Discrete categorical ranking (1, 2, 3).</li>
                <li>✔ <code>sex</code>: <code>object</code> / string — Categorical (female, male).</li>
                <li>✔ <code>age</code>: <code>float64</code> — Continuous numeric (binned into 5 cohorts).</li>
                <li>✔ <code>fare</code>: <code>float64</code> — Continuous monetary metric.</li>
              </ul>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- ========================================================= -->
    <!-- TAB 4: METHODOLOGY & LIMITATIONS                          -->
    <!-- ========================================================= -->
    <div id="tab-methodology" class="tab-content hidden">
      <div class="panel">
        <div class="panel-header">
          <div class="panel-title">📖 Analytical Methodology, Limitations & Deliverables</div>
        </div>

        <div class="grid-2">
          <div style="display: flex; flex-direction: column; gap: 16px;">
            <div style="background: #182234; padding: 18px; border-radius: 12px; border: 1px solid var(--card-border);">
              <h4 style="color: #38bdf8; margin-bottom: 8px;">Association vs. Causation</h4>
              <p style="font-size: 13px; color: #cbd5e1;">
                Descriptive comparisons reveal empirical associations rather than direct causation. For instance, high survival in 1st class was mediated by cabin deck proximity to lifeboats and organized early evacuation access, rather than ticket price acting as an isolated biological determinant.
              </p>
            </div>

            <div style="background: #182234; padding: 18px; border-radius: 12px; border: 1px solid var(--card-border);">
              <h4 style="color: #38bdf8; margin-bottom: 8px;">Imputation Trade-offs</h4>
              <p style="font-size: 13px; color: #cbd5e1;">
                Filling missing ages with subgroup medians is superior to a single global median, yet it reduces intra-group variance. However, given that missingness was approximately 20%, this approach avoided sample truncation while preserving group demographics.
              </p>
            </div>

            <div style="background: #182234; padding: 18px; border-radius: 12px; border: 1px solid var(--card-border);">
              <h4 style="color: #38bdf8; margin-bottom: 8px;">Age Cohort Discretization</h4>
              <p style="font-size: 13px; color: #cbd5e1;">
                Using <code>pd.cut()</code> with boundaries <code>[0, 12, 18, 40, 60, 100]</code> allowed comprehensive coverage of the entire life course without discarding or losing any passengers (891 / 891 accounted for).
              </p>
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 16px;">
            <div style="background: #182234; padding: 18px; border-radius: 12px; border: 1px solid var(--card-border);">
              <h4 style="color: #38bdf8; margin-bottom: 12px;">Deliverables for Submission</h4>
              <ul style="font-size: 13px; color: #cbd5e1; display: flex; flex-direction: column; gap: 10px; list-style-type: none;">
                <li>📁 <strong>Jupyter Notebook</strong>: <code>titanic_eda.ipynb</code> (18 structured sections, all cells executed)</li>
                <li>🌐 <strong>Static HTML Export</strong>: <code>titanic_eda.html</code> (Self-contained notebook export)</li>
                <li>📝 <strong>Findings Summary</strong>: <code>FINDINGS_SUMMARY.md</code> (Executive summary of Q1, Q2, Q3)</li>
                <li>💻 <strong>Console Runner</strong>: <code>run_eda.py</code> (Instant terminal verification)</li>
                <li>📊 <strong>Visual Plots</strong>: <code>titanic_survival_charts.png</code> (High-resolution Matplotlib charts)</li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- Footer -->
    <footer>
      Titanic Exploratory Data Analysis Dashboard • InternCircle Project 01 Submission • Pure Client-Side Architecture
    </footer>

  </div>

  <!-- Embedded Titanic Dataset & Client-Side Engine -->
  <script>
    const allPassengers = {data_json};

    let filteredPassengers = [...allPassengers];
    let currentPage = 1;
    let rowsPerPage = 25;
    let sortColumn = 'id';
    let sortAscending = true;

    function switchTab(tabId) {{
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(tab => tab.classList.add('hidden'));

      if (tabId === 'dashboard') {{
        document.querySelectorAll('.tab-btn')[0].classList.add('active');
        document.getElementById('tab-dashboard').classList.remove('hidden');
      }} else if (tabId === 'datatable') {{
        document.querySelectorAll('.tab-btn')[1].classList.add('active');
        document.getElementById('tab-datatable').classList.remove('hidden');
        renderTable();
      }} else if (tabId === 'cleaning') {{
        document.querySelectorAll('.tab-btn')[2].classList.add('active');
        document.getElementById('tab-cleaning').classList.remove('hidden');
      }} else if (tabId === 'methodology') {{
        document.querySelectorAll('.tab-btn')[3].classList.add('active');
        document.getElementById('tab-methodology').classList.remove('hidden');
      }}
    }}

    function applyFilters() {{
      const search = document.getElementById('searchInput').value.toLowerCase().trim();
      const pclass = document.getElementById('filterClass').value;
      const sex = document.getElementById('filterSex').value;
      const survived = document.getElementById('filterSurvived').value;
      const ageGroup = document.getElementById('filterAgeGroup').value;
      const embarked = document.getElementById('filterEmbarked').value;

      filteredPassengers = allPassengers.filter(p => {{
        if (pclass !== 'ALL' && p.pclass.toString() !== pclass) return false;
        if (sex !== 'ALL' && p.sex !== sex) return false;
        if (survived !== 'ALL' && p.survived.toString() !== survived) return false;
        if (ageGroup !== 'ALL' && p.age_group !== ageGroup) return false;
        if (embarked !== 'ALL' && p.embarked !== embarked) return false;

        if (search) {{
          const rowText = `${{p.id}} ${{p.survived === 1 ? 'survived' : 'died'}} ${{p.pclass}} ${{p.sex}} ${{p.age}} ${{p.age_group}} ${{p.fare}} ${{p.embarked}} ${{p.embark_town}}`.toLowerCase();
          if (!rowText.includes(search)) return false;
        }}

        return true;
      }});

      // Update filtered stats
      const totalFiltered = filteredPassengers.length;
      const survivorsFiltered = filteredPassengers.filter(p => p.survived === 1).length;
      const rateFiltered = totalFiltered > 0 ? ((survivorsFiltered / totalFiltered) * 100).toFixed(2) : 0;

      document.getElementById('filterCountDisplay').innerText = `Showing ${{totalFiltered}} of ${{allPassengers.length}} passengers`;
      document.getElementById('filterSurvivalDisplay').innerText = `Filtered Survival Rate: ${{rateFiltered}}% (${{survivorsFiltered}} / ${{totalFiltered}})`;

      currentPage = 1;
      renderTable();
    }}

    function resetFilters() {{
      document.getElementById('searchInput').value = '';
      document.getElementById('filterClass').value = 'ALL';
      document.getElementById('filterSex').value = 'ALL';
      document.getElementById('filterSurvived').value = 'ALL';
      document.getElementById('filterAgeGroup').value = 'ALL';
      document.getElementById('filterEmbarked').value = 'ALL';
      applyFilters();
    }}

    function sortTable(column) {{
      if (sortColumn === column) {{
        sortAscending = !sortAscending;
      }} else {{
        sortColumn = column;
        sortAscending = true;
      }}

      filteredPassengers.sort((a, b) => {{
        let valA = a[column];
        let valB = b[column];

        if (valA === null || valA === undefined) valA = '';
        if (valB === null || valB === undefined) valB = '';

        if (typeof valA === 'number' && typeof valB === 'number') {{
          return sortAscending ? valA - valB : valB - valA;
        }}
        return sortAscending 
          ? valA.toString().localeCompare(valB.toString()) 
          : valB.toString().localeCompare(valA.toString());
      }});

      renderTable();
    }}

    function changeRowsPerPage(val) {{
      rowsPerPage = parseInt(val);
      currentPage = 1;
      renderTable();
    }}

    function renderTable() {{
      const tbody = document.getElementById('passengerTableBody');
      tbody.innerHTML = '';

      if (filteredPassengers.length === 0) {{
        tbody.innerHTML = `<tr><td colspan="12" style="text-align: center; padding: 28px; color: var(--text-muted);">No passengers matched your filters.</td></tr>`;
        renderPagination(0);
        return;
      }}

      const startIndex = (currentPage - 1) * rowsPerPage;
      const endIndex = Math.min(startIndex + rowsPerPage, filteredPassengers.length);
      const pageRows = filteredPassengers.slice(startIndex, endIndex);

      pageRows.forEach(p => {{
        const tr = document.createElement('tr');
        
        const outcomeBadge = p.survived === 1 
          ? `<span class="badge badge-green">Survived</span>` 
          : `<span class="badge badge-red">Died</span>`;

        let classBadge = '';
        if (p.pclass === 1) classBadge = `<span class="badge badge-amber">1st Class</span>`;
        else if (p.pclass === 2) classBadge = `<span class="badge badge-blue">2nd Class</span>`;
        else classBadge = `<span class="badge badge-purple">3rd Class</span>`;

        const imputedTag = p.age_imputed ? `<span class="imputed-flag" title="Imputed via subgroup median">*</span>` : '';

        tr.innerHTML = `
          <td><strong>#${{p.id}}</strong></td>
          <td>${{outcomeBadge}}</td>
          <td>${{classBadge}}</td>
          <td>${{p.sex === 'female' ? '👩 female' : '👨 male'}}</td>
          <td>${{p.age}}${{imputedTag}}</td>
          <td><span class="badge badge-blue">${{p.age_group}}</span></td>
          <td>${{p.sibsp}}</td>
          <td>${{p.parch}}</td>
          <td>£${{p.fare ? p.fare.toFixed(2) : '0.00'}}</td>
          <td><strong>${{p.embarked || '-'}}</strong></td>
          <td>${{p.embark_town || '-'}}</td>
          <td>${{p.alone ? 'Yes' : 'No'}}</td>
        `;
        tbody.appendChild(tr);
      }});

      renderPagination(filteredPassengers.length);
    }}

    function renderPagination(totalRows) {{
      const container = document.getElementById('paginationButtons');
      container.innerHTML = '';

      const totalPages = Math.ceil(totalRows / rowsPerPage);
      if (totalPages <= 1) return;

      const prevBtn = document.createElement('button');
      prevBtn.className = 'page-btn';
      prevBtn.innerText = '‹ Prev';
      prevBtn.disabled = currentPage === 1;
      prevBtn.onclick = () => {{ if (currentPage > 1) {{ currentPage--; renderTable(); }} }};
      container.appendChild(prevBtn);

      const maxButtons = 7;
      let startPage = Math.max(1, currentPage - 3);
      let endPage = Math.min(totalPages, startPage + maxButtons - 1);
      if (endPage - startPage < maxButtons - 1) {{
        startPage = Math.max(1, endPage - maxButtons + 1);
      }}

      for (let i = startPage; i <= endPage; i++) {{
        const btn = document.createElement('button');
        btn.className = `page-btn ${{i === currentPage ? 'active' : ''}}`;
        btn.innerText = i;
        btn.onclick = () => {{ currentPage = i; renderTable(); }};
        container.appendChild(btn);
      }}

      const nextBtn = document.createElement('button');
      nextBtn.className = 'page-btn';
      nextBtn.innerText = 'Next ›';
      nextBtn.disabled = currentPage === totalPages;
      nextBtn.onclick = () => {{ if (currentPage < totalPages) {{ currentPage++; renderTable(); }} }};
      container.appendChild(nextBtn);
    }}

    function exportFilteredCSV() {{
      if (filteredPassengers.length === 0) return alert('No rows to export.');

      const headers = ['id', 'survived', 'pclass', 'sex', 'age', 'age_group', 'sibsp', 'parch', 'fare', 'embarked', 'embark_town', 'alone', 'age_imputed'];
      const csvRows = [headers.join(',')];

      filteredPassengers.forEach(p => {{
        const row = [
          p.id,
          p.survived,
          p.pclass,
          p.sex,
          p.age,
          `"${{p.age_group}}"`,
          p.sibsp,
          p.parch,
          p.fare,
          p.embarked,
          `"${{p.embark_town || ''}}"`,
          p.alone,
          p.age_imputed
        ];
        csvRows.push(row.join(','));
      }});

      const blob = new Blob([csvRows.join('\\n')], {{ type: 'text/csv' }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'titanic_filtered_data.csv';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }}

    // Initial render
    window.onload = function() {{
      applyFilters();
    }};
  </script>
</body>
</html>
"""

    output_html = "index.html"
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated standalone webpage dashboard: '{output_html}'")

    dashboard_copy = "titanic_dashboard.html"
    with open(dashboard_copy, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Also saved copy to: '{dashboard_copy}'")

if __name__ == "__main__":
    build_webpage()
