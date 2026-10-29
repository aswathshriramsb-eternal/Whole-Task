"""
generate_charts.py
Generate publication-quality Seaborn and Matplotlib visualizations for Project 02.
Saves all charts into the outputs/ directory using a modern dark navy theme.
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'tips.csv')
OUTPUT_DIR = os.path.join(BASE_DIR, 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)

# Setup Theme colors matching the website's dark navy palette
BG_DARK = "#0d1527"
BG_CARD = "#152238"
TEXT_COLOR = "#e2e8f0"
TEXT_MUTED = "#94a3b8"
ACCENT_BLUE = "#38bdf8"
ACCENT_CYAN = "#22d3ee"
ACCENT_INDIGO = "#818cf8"
ACCENT_AMBER = "#fbbf24"
GRID_COLOR = "#1e293b"

def apply_custom_theme():
    plt.style.use('dark_background')
    plt.rcParams.update({
        'figure.facecolor': BG_DARK,
        'axes.facecolor': BG_CARD,
        'savefig.facecolor': BG_DARK,
        'axes.edgecolor': '#334155',
        'axes.labelcolor': TEXT_COLOR,
        'xtick.color': TEXT_MUTED,
        'ytick.color': TEXT_MUTED,
        'grid.color': GRID_COLOR,
        'grid.linestyle': '--',
        'grid.alpha': 0.6,
        'text.color': TEXT_COLOR,
        'font.family': 'sans-serif',
        'font.size': 11
    })

apply_custom_theme()

print("Generating Seaborn & Matplotlib charts...")

# -------------------------------------------------------------
# Chart 1: Distribution of Restaurant Bills (Histogram + KDE)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=200)
sns.histplot(
    df['total_bill'],
    kde=True,
    bins=20,
    color=ACCENT_BLUE,
    edgecolor="#0f172a",
    alpha=0.75,
    ax=ax
)
mean_val = df['total_bill'].mean()
median_val = df['total_bill'].median()
ax.axvline(mean_val, color=ACCENT_AMBER, linestyle='--', linewidth=2, label=f'Mean (${mean_val:.2f})')
ax.axvline(median_val, color=ACCENT_CYAN, linestyle=':', linewidth=2, label=f'Median (${median_val:.2f})')

ax.set_title("Distribution of Restaurant Bills", fontsize=15, fontweight='bold', pad=15, color=TEXT_COLOR)
ax.set_xlabel("Total Bill ($)", fontsize=12, labelpad=10)
ax.set_ylabel("Frequency (Receipt Count)", fontsize=12, labelpad=10)
ax.legend(frameon=True, facecolor=BG_DARK, edgecolor='#334155', fontsize=10)
ax.grid(True)
plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'dist_bills.png'))
plt.close(fig)
print("Saved outputs/dist_bills.png")

# -------------------------------------------------------------
# Chart 2: Average Tip by Day (Bar Chart)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=200)
day_order = ['Thur', 'Fri', 'Sat', 'Sun']
avg_tips = df.groupby('day', observed=False)['tip'].mean().reindex(day_order)

bars = ax.bar(
    day_order,
    avg_tips,
    color=['#38bdf8', '#818cf8', '#a855f7', '#ec4899'],
    edgecolor='#0f172a',
    width=0.55,
    alpha=0.9
)

# Annotate exact bar values
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"${height:.2f}",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 6),
        textcoords="offset points",
        ha='center', va='bottom',
        fontsize=11, fontweight='bold',
        color=TEXT_COLOR
    )

ax.set_title("Average Tip by Day", fontsize=15, fontweight='bold', pad=15, color=TEXT_COLOR)
ax.set_xlabel("Day of the Week", fontsize=12, labelpad=10)
ax.set_ylabel("Average Tip ($)", fontsize=12, labelpad=10)
ax.set_ylim(0, 4.0)
ax.grid(axis='y')
plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'avg_tip_day.png'))
plt.close(fig)
print("Saved outputs/avg_tip_day.png")

# -------------------------------------------------------------
# Chart 3: Distribution of Tips Across Days (Box Plot)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=200)
palette = {'Thur': '#38bdf8', 'Fri': '#818cf8', 'Sat': '#a855f7', 'Sun': '#ec4899'}
sns.boxplot(
    data=df,
    x='day',
    y='tip',
    hue='day',
    legend=False,
    order=day_order,
    palette=palette,
    boxprops=dict(alpha=0.8, edgecolor=TEXT_COLOR),
    medianprops=dict(color='#ffffff', linewidth=2.5),
    whiskerprops=dict(color=TEXT_MUTED, linewidth=1.5),
    capprops=dict(color=TEXT_MUTED, linewidth=1.5),
    flierprops=dict(marker='o', markerfacecolor=ACCENT_AMBER, markeredgecolor='none', markersize=6),
    ax=ax
)

ax.set_title("Distribution of Tips Across Days", fontsize=15, fontweight='bold', pad=15, color=TEXT_COLOR)
ax.set_xlabel("Day of the Week", fontsize=12, labelpad=10)
ax.set_ylabel("Tip ($)", fontsize=12, labelpad=10)
ax.grid(axis='y')
plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'box_tips_day.png'))
plt.close(fig)
print("Saved outputs/box_tips_day.png")

# -------------------------------------------------------------
# Chart 4: Relationship Between Total Bill and Tip (Scatter Plot)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9.5, 5.5), dpi=200)
time_colors = {'Dinner': '#38bdf8', 'Lunch': '#f59e0b'}

sns.scatterplot(
    data=df,
    x='total_bill',
    y='tip',
    hue='time',
    palette=time_colors,
    alpha=0.85,
    s=70,
    edgecolor='#0f172a',
    linewidth=0.8,
    ax=ax
)

# Linear regression trend line overall
sns.regplot(
    data=df,
    x='total_bill',
    y='tip',
    scatter=False,
    color='#cbd5e1',
    line_kws={'linestyle': '--', 'linewidth': 1.8, 'label': 'Overall Trend (r = 0.68)'},
    ax=ax
)

ax.set_title("Relationship Between Total Bill and Tip", fontsize=15, fontweight='bold', pad=15, color=TEXT_COLOR)
ax.set_xlabel("Total Bill ($)", fontsize=12, labelpad=10)
ax.set_ylabel("Tip ($)", fontsize=12, labelpad=10)
ax.legend(frameon=True, facecolor=BG_DARK, edgecolor='#334155', fontsize=10)
ax.grid(True)
plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'scatter_bill_tip.png'))
plt.close(fig)
print("Saved outputs/scatter_bill_tip.png")

# -------------------------------------------------------------
# Chart 5: Correlation Heatmap
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 6), dpi=200)
num_cols = ['total_bill', 'tip', 'size']
corr_matrix = df[num_cols].corr()

# Rename for presentation
corr_matrix.columns = ['Total Bill', 'Tip', 'Party Size']
corr_matrix.index = ['Total Bill', 'Tip', 'Party Size']

cmap = sns.diverging_palette(220, 20, as_cmap=True)

sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".3f",
    cmap="mako",
    vmin=-0.2,
    vmax=1.0,
    cbar_kws={'label': 'Pearson Correlation (r)'},
    linewidths=1.5,
    linecolor='#1e293b',
    annot_kws={'size': 13, 'weight': 'bold'},
    ax=ax
)

ax.set_title("Correlation Heatmap (Numerical Variables)", fontsize=15, fontweight='bold', pad=15, color=TEXT_COLOR)
plt.tight_layout()
fig.savefig(os.path.join(OUTPUT_DIR, 'correlation_heatmap.png'))
plt.close(fig)
print("Saved outputs/correlation_heatmap.png")

print("All Seaborn/Matplotlib charts generated successfully in DataVisualizationWebsite/outputs/!")
