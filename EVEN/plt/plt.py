import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
data = {
    'Model': ['GPT4', 'LLAMA', 'Kimi', 'ChatGLM'],
    'Numerical': [0.675675676, 0.567567568, 0.216216216, 0.972972973],
    'Proportional': [0.297297297, 0.594594595, 0.675675676, 0.081081081],
    'Equality': [0.72972973, 0.459459459, 0.405405405, 0.851351351],
    'Equity': [0.054054054, 0.013513514, 0.054054054, 0.72972973],
    'Bais': [0.013513514, 0.013513514, 0, 0.743243243]
}

# 创建DataFrame
df = pd.DataFrame(data)
df_heatmap = df.set_index('Model')

plt.rcParams.update({'font.size': 26})

# 设置图形样式
plt.figure(figsize=(15, 8))

# 创建掩码数组来决定文字颜色
text_colors = np.where(df_heatmap.values >= 0.5, 'white', 'black')

# 创建热力图
ax = sns.heatmap(df_heatmap,
                 cmap='YlOrRd',
                 annot=True,
                 fmt='.2f',
                 cbar_kws={'label': 'Value'},
                 linewidths=0.5,
                 square=True,
                 annot_kws={'size': 20},  # 数值大小
                 center=0.5,
                 xticklabels=True,
                 yticklabels=True)

# 遍历热力图的每个单元格并设置文字颜色
for text, color in zip(ax.texts, text_colors.flatten()):
    text.set_color(color)

# 调整坐标轴标签大小
ax.set_xticklabels(ax.get_xticklabels(), size=20)
ax.set_yticklabels(ax.get_yticklabels(), size=20)

# 获取 colorbar 并设置标签大小
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=20)
cbar.set_label('Value', size=26)

# 调整布局和标题
plt.title('Fairness Notion Spectrum', pad=20, size=26)  # 标题也相应增大
plt.xticks(rotation=0)
plt.tight_layout()

# 显示图形
plt.show()