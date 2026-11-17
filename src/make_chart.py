# Builds reports/figures/life-expectancy-1950-<year>.png from data/raw/life-expectancy.csv
# Run from the project root: python src/make_chart.py
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # draw to a file, no window needed
import matplotlib.pyplot as plt

DATA = 'data/raw/life-expectancy.csv'
VALUE = 'Life expectancy'  # column name in the Our World in Data CSV

# colour, line width, line style for each entity
E = {
    'Israel': ('#0B5CAD', 3.2, '-'),
    'United Kingdom': ('#9AA5B1', 1.8, '-'),
    'United States': ('#C0786B', 1.8, '-'),
    'World': ('#5F6B76', 1.8, (0, (4, 3))),
}

# 1. Load and reshape: one row per year, one column per entity
d = pd.read_csv(DATA)
p = d[d.Entity.isin(E) & (d.Year >= 1950)].pivot(index='Year', columns='Entity', values=VALUE)
last = p.index.max()

# 2. The key numbers (also printed, so the README can be checked against them)
g0 = p.loc[1950, 'Israel'] - p.loc[1950, 'World']
g1 = p.loc[last, 'Israel'] - p.loc[last, 'World']
print(f"Israel 1950: {p.loc[1950, 'Israel']:.1f}  World 1950: {p.loc[1950, 'World']:.1f}  gap: {g0:.1f}")
print(f"Israel {last}: {p.loc[last, 'Israel']:.1f}  World {last}: {p.loc[last, 'World']:.1f}  gap: {g1:.1f}")

# 3. Lines
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(12, 6.75), dpi=150)
fig.patch.set_facecolor('white')
order = ['World', 'United Kingdom', 'United States', 'Israel']  # Israel last = drawn on top
for e in order:
    c, w, ls = E[e]
    ax.plot(p.index, p[e], color=c, lw=w, ls=ls, zorder=3 if e == 'Israel' else 2, solid_capstyle='round')

# 4. End-of-line labels instead of a legend
ypos = {
    'Israel': p.loc[last, 'Israel'] + 1.2,
    'United Kingdom': p.loc[last, 'United Kingdom'] - 0.2,
    'United States': p.loc[last, 'United States'] - 1.4,
    'World': p.loc[last, 'World'],
}
for e in order:
    c = E[e][0]
    v = p.loc[last, e]
    ax.scatter([last], [v], color=c, s=40 if e == 'Israel' else 22, zorder=4)
    ax.text(last + 1.2, ypos[e], f"{e} {v:.1f}", color=c, va='center',
            fontsize=13 if e == 'Israel' else 11.5, fontweight='bold' if e == 'Israel' else 'normal')

# 5. Gap arrows, first and last year
for yr in (1950, last):
    ax.annotate('', xy=(yr, p.loc[yr, 'World']), xytext=(yr, p.loc[yr, 'Israel']),
                arrowprops=dict(arrowstyle='<->', color='#0B5CAD', lw=1.2, alpha=.7))
ax.text(1951, (p.loc[1950, 'Israel'] + p.loc[1950, 'World']) / 2, f"gap {g0:.1f} yrs", color='#0B5CAD', fontsize=11, va='center')
ax.text(last + 1.2, 75.4, f"gap {g1:.1f} yrs", color='#0B5CAD', fontsize=11, va='center')

# 6. Context annotations
ax.annotate('Mass immigration and transit camps: infant mortality\nrose from 29 (1947) to 52 (1949) per 1,000 births',
            xy=(1952, p.loc[1952, 'Israel']), xytext=(1962, 67.2), fontsize=10, color='#0B5CAD', va='center',
            arrowprops=dict(arrowstyle='-', color='#0B5CAD', lw=.8))
ax.annotate('Famine in China, 1959 to 1961', xy=(1960, p.loc[1960, 'World']), xytext=(1964, 44.5),
            fontsize=10, color='#5F6B76', arrowprops=dict(arrowstyle='-', color='#5F6B76', lw=.8))
ax.text(2018.3, 74.4, 'COVID-19', fontsize=10, color='#8A5A50', ha='center')

# 7. Axes and styling
ax.set_xlim(1949, last + 17)
ax.set_ylim(40, 88)
ax.set_xticks(range(1950, 2021, 10))
ax.set_yticks(range(40, 90, 10))
ax.grid(axis='y', color='#E6EAEE', lw=1)
ax.set_axisbelow(True)
for s in ['top', 'right', 'left']:
    ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#9AA5B1')
ax.tick_params(colors='#4A5560', length=0)
ax.set_ylabel('Years', color='#4A5560')

# 8. Title, subtitle, source
fig.text(0.06, 0.95, f"Israel's life expectancy rose from {p.loc[1950, 'Israel']:.0f} to {p.loc[last, 'Israel']:.0f} years since 1950",
         fontsize=19, fontweight='bold', color='#12355B')
fig.text(0.06, 0.905, f"Life expectancy at birth, 1950 to {last}. The gap to the world average narrowed from {g0:.1f} to {g1:.1f} years.",
         fontsize=12.5, color='#4A5560')
fig.text(0.06, 0.025, "Source: Our World in Data (CC BY 4.0); infant mortality: Israel CBS Statistical Abstract 1952 and Ministry of Health"
         "  ·  Chart: Eshed Lin", fontsize=9.5, color='#7A8590')
plt.subplots_adjust(left=0.07, right=0.97, top=0.85, bottom=0.1)

out = f'reports/figures/life-expectancy-1950-{last}.png'
fig.savefig(out, facecolor='white')
print('saved', out)
