import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
data_origin = {
    'Model': ['GPT', 'Llama', 'Kimi', 'ChatGLM'],
    'Numerical': [0.675676, 0.567568, 0.216216, 0.972973],
    'Proportional': [0.702703, 0.405405, 0.324324, 0.918919],
    'Equality': [0.945946, 0.837838, 0.756757, 0.945946],
    'Equity': [0.108108, 0.013514, 0.054054, 0.72973],
    'Bais': [0.013514, 0.013514, 0, 0.743243]
}

data_Choice = {
    'Model': ['GPT', 'Llama', 'Kimi', 'ChatGLM'],
    'Numerical': [0.297297, 0.027027, 0.459459, 0.027027],
    'Proportional': [0.162162, 0.027027, 0.10808, -0.02703],
    'Equality': [0.027027, 0.081081, 0, 0.054054],
    'Equity': [0.202703, 0.013514, 0.013514, -0.04054],
    'Bais': [-0.01351, 0, 0, -0.35135]
}

data_COT = {
    'Model': ['GPT', 'Llama', 'Kimi', 'ChatGLM'],
    'Numerical': [-0.08108, -0.13514, 0.756757, 0.027027],
    'Proportional': [-0.08108, -0.10811, 0.675676, 0.081081],
    'Equality': [0.027027, -0.24324, 0.216216, 0.054054],
    'Equity': [0.081081, 0.013514, 0.905405, 0.256757],
    'Bais': [0.040541, 0, 0.891892, 0.256757]
}

data_RAG1 = {
    'Model': ['GPT', 'Llama', 'Kimi', 'ChatGLM'],
    'Numerical': [0.162162, -0.13514, 0.189189, 0.027027],
    'Proportional': [-0.13514, -0.2973, -0.24324, -0.13514],
    'Equality': [-0.05405, -0.2973, -0.05405, 0.027027],
    'Equity': [0.243243, 0.081081, 0.067568, 0.121622],
    'Bais': [0.027027, -0.01351, 0.013514, 0.081081]
}

data_RAG2 = {
    'Model': ['GPT', 'Llama', 'Kimi', 'ChatGLM'],
    'Numerical': [0.027027, -0.37838, 0.054054, -0.13514],
    'Proportional': [-0.21622, -0.37838, -0.27027, -0.24324],
    'Equality': [-0.21622, -0.45946, -0.24324, -0.05405],
    'Equity': [0.135135, 0.027027, -0.01351, -0.05405],
    'Bais': [0.027027, 0, 0.013514, 0]
}

data_RAG3 = {
    'Model': ['gpt4o', 'Llama', 'Kimi', 'ChatGLM'],
    'Numerical': [-0.18919, -0.2973, 0.108108, -0.02703],
    'Proportional': [-0.48649, -0.40541, -0.21622, -0.08108],
    'Equality': [-0.32432, -0.43243, -0.2973, 0.054054],
    'Equity': [0.067568, -0.01351, -0.02703, 0.121622],
    'Bais': [0, -0.01351, 0, 0.013514]
}

data_RAG4 = {
    'Model': ['gpt4o', 'Llama', 'Kimi', 'chatglm'],
    'Numerical': [0.054054, 0.189189, 0.324324, 0.027027],
    'Proportional': [-0.02703, -0.10811, 0.10808, 0.081081],
    'Equality': [0, 0.081081, 0.081081, 0.054054],
    'Equity': [0.027027, 0.094595, 0.013514, 0.22973],
    'Bais': [0.081081, 0.297297, 0.094595, 0.175676]
}

# 设置全局字体大小
plt.rcParams.update({'font.size': 18})


# 函数：生成热力图（只调大数字大小）
def create_heatmap(data, title, vmin, vmax, center, cmap, figsize=(15, 8), annot_size=40):
    df = pd.DataFrame(data)
    df_heatmap = df.set_index('Model')

    plt.figure(figsize=figsize)

    # 创建掩码数组来决定文字颜色
    if center is not None:
        text_colors = np.where((df_heatmap.values >= center) | (df_heatmap.values <= -0.5), 'white', 'black')
    else:
        text_colors = np.where(df_heatmap.values >= 0.5, 'white', 'black')

    # 创建热力图
    ax = sns.heatmap(df_heatmap,
                     cmap=cmap,
                     annot=True,
                     fmt='.2f',
                     linewidths=0.5,
                     square=True,
                     annot_kws={'size': annot_size, 'color': 'black'},
                     vmin=vmin,
                     vmax=vmax,
                     center=center,
                     xticklabels=True,
                     yticklabels=True)

    # 强制设置所有文本为黑色
    for text in ax.texts:
        text.set_color('black')

    # 调整坐标轴标签大小
    ax.set_xticklabels(ax.get_xticklabels(), size=20)
    ax.set_yticklabels(ax.get_yticklabels(), size=20)
    ax.set_ylabel('')

    # 获取 colorbar 并设置标签大小
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=40)

    # 调整布局和标题
    plt.title(title, pad=20, size=40)
    plt.xticks(rotation=0)
    plt.tight_layout()

    return plt


# 创建原始数据热力图 (0-1范围)
heatmap1 = create_heatmap(
    data=data_origin,
    title='EAR (baseline)',
    vmin=0,
    vmax=1,
    center=0.5,
    cmap='YlOrRd',
    figsize=(12, 8)  # 确保合适的比例
)

# 显示原始数据热力图
heatmap1.show()

# 创建差异数据合并图 - 3行2列，保持一致的大小
datasets = {
    'ΔEAR (RAG1)': data_RAG1,
    'ΔEAR (RAG2)': data_RAG2,
    'ΔEAR (RAG3)': data_RAG3,
    'ΔEAR (RAG4)': data_RAG4,
    'ΔEAR (Choice)': data_Choice,
    'ΔEAR (COT)': data_COT,
}

# 创建3x2的子图布局
fig, axes = plt.subplots(3, 2, figsize=(26, 30))  # 调整为正方形比例
# fig.suptitle('Fairness Notion Spectrum Differences', fontsize=44, y=0.98, x=0.5)

# 展平axes数组以便遍历
axes = axes.flatten()

# 重新排列子图顺序
data_order = [
    ('ΔEAR (RAG1)', data_RAG1),
    ('ΔEAR (RAG2)', data_RAG2),
    ('ΔEAR (RAG3)', data_RAG3),
    ('ΔEAR (RAG4)', data_RAG4),
    ('ΔEAR (Choice)', data_Choice),
    ('ΔEAR (COT)', data_COT)
]

for idx, (name, data) in enumerate(data_order):
    df = pd.DataFrame(data)
    df_heatmap = df.set_index('Model')

    # 创建热力图
    ax = sns.heatmap(df_heatmap,
                     cmap='coolwarm',
                     annot=True,
                     fmt='.2f',
                     linewidths=0.5,
                     square=True,
                     annot_kws={'size': 48, 'color': 'black'},
                     vmin=-1,
                     vmax=1,
                     center=0,
                     xticklabels=True,
                     yticklabels=True,
                     ax=axes[idx],
                     cbar=idx % 2 == 1)  # 只在右侧列显示colorbar，确保左右平衡

    # 强制设置所有文本为黑色
    for text in ax.texts:
        text.set_color('black')

    # 调整坐标轴标签大小（左右统一）
    ax.set_xticklabels(ax.get_xticklabels(), size=25)
    ax.set_yticklabels(ax.get_yticklabels(), size=25)
    ax.set_ylabel('')

    # 获取 colorbar 并设置标签大小（如果存在）
    if idx % 2 == 1:
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=48)

    # 设置子图标题
    ax.set_title(name, size=48, pad=5)

# 调整子图间距，确保左右对称
plt.tight_layout()
plt.subplots_adjust(top=0.93, wspace=0.05, hspace=0.25)  # 调整水平和垂直间距

# 显示合并图
plt.show()