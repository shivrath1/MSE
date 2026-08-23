import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. LOAD DATA
df = pd.read_csv('world_happiness_dataset.csv')

# Identify top 3 happiest & lowest
top3 = df.nlargest(3, 'Happiness_Score')
lowest = df.nsmallest(1, 'Happiness_Score').iloc[0]

# 2. MATPLOTLIB DASHBOARD (2x2 grid)
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
colors = ['#2E86AB', '#A23B72', '#F18F01']

# Bar chart: Top 3 happiness scores
ax1 = axes[0, 0]
bars = ax1.bar(top3['Country'], top3['Happiness_Score'], color=colors, edgecolor='black')
ax1.set_title('Top 3 Happiest Countries', fontweight='bold')
for bar, s in zip(bars, top3['Happiness_Score']):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15, f'{s:.2f}',
             ha='center', fontsize=12, fontweight='bold')

# Grouped horizontal bar: Metrics comparison
ax2 = axes[0, 1]
metrics = ['GDP_per_Capita', 'Social_Support', 'Freedom_to_Make_Choices', 'Generosity']
x = np.arange(len(metrics))
for i, (_, row) in enumerate(top3.iterrows()):
    ax2.barh(x + i*0.25, [row[m] for m in metrics], 0.25, label=row['Country'], color=colors[i])
ax2.set_yticks(x + 0.25)
ax2.set_yticklabels(['GDP/Capita', 'Social Support', 'Freedom', 'Generosity'])
ax2.set_title('Top 3: Key Metrics Comparison', fontweight='bold')
ax2.legend()

# Pie chart: South Africa freedom breakdown
ax3 = axes[1, 0]
sa_f = lowest['Freedom_to_Make_Choices']
ax3.pie([sa_f, 1-sa_f], explode=(0.05,0), labels=['Freedom Score','Remaining'],
        autopct='%1.0f%%', colors=['#E63946','#F1FAEE'], shadow=True)
ax3.set_title(f"South Africa Freedom Score\n(Happiness: {lowest['Happiness_Score']:.2f})", fontweight='bold')

# Radar chart: South Africa normalized profile
ax4 = fig.add_subplot(2, 2, 4, polar=True)
cats = ['Happiness','GDP','Social\nSupport','Health','Freedom','Generosity','Low\nCorruption']
vals = [
    lowest['Happiness_Score']/df['Happiness_Score'].max(),
    lowest['GDP_per_Capita']/df['GDP_per_Capita'].max(),
    lowest['Social_Support']/df['Social_Support'].max(),
    lowest['Healthy_Life_Expectancy']/df['Healthy_Life_Expectancy'].max(),
    lowest['Freedom_to_Make_Choices']/df['Freedom_to_Make_Choices'].max(),
    lowest['Generosity']/df['Generosity'].max(),
    1 - lowest['Perceptions_of_Corruption']/df['Perceptions_of_Corruption'].max()
]
vals += vals[:1]
ang = np.linspace(0, 2*np.pi, len(cats), endpoint=False).tolist() + [0]
ax4.plot(ang, vals, 'o-', color='#E63946')
ax4.fill(ang, vals, alpha=0.25, color='#E63946')
ax4.set_xticks(ang[:-1])
ax4.set_xticklabels(cats, fontsize=9)
ax4.set_title('South Africa: Normalized Profile', fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('happiness_dashboard_matplotlib.png', dpi=150, bbox_inches='tight')

# 3. PLOTLY DASHBOARD (Interactive)
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Top 3 Happiest Countries', 'Top 3: Detailed Metrics',
                    'South Africa: Freedom Breakdown', 'South Africa: Radar Profile'),
    specs=[[{"type":"bar"},{"type":"bar"}],[{"type":"pie"},{"type":"polar"}]]
)

fig.add_trace(go.Bar(x=top3['Country'], y=top3['Happiness_Score'],
    text=[f'{s:.2f}' for s in top3['Happiness_Score']], textposition='outside',
    marker_color=colors, marker_line_color='black', marker_line_width=1.5), row=1, col=1)

for i, (_, row) in enumerate(top3.iterrows()):
    fig.add_trace(go.Bar(x=['GDP','Social','Freedom','Generosity'],
        y=[row[m] for m in metrics], name=row['Country'], marker_color=colors[i]), row=1, col=2)

fig.add_trace(go.Pie(labels=['Freedom (0.90)','Remaining (0.10)'],
    values=[sa_f, 1-sa_f], hole=0.4, marker_colors=['#E63946','#F1FAEE'],
    textinfo='percent+label', pull=[0.05,0]), row=2, col=1)

fig.add_trace(go.Scatterpolar(
    r=vals, theta=cats+[cats[0]], fill='toself',
    fillcolor='rgba(230,57,70,0.3)', line=dict(color='#E63946', width=2)), row=2, col=2)

fig.update_layout(title_text='<b>World Happiness Dashboard (Plotly)</b>',
    title_x=0.5, height=750, width=1100, template='plotly_white',
    legend=dict(orientation='h', y=-0.15, x=0.5, xanchor='center'))
fig.write_html('happiness_dashboard_plotly.html')