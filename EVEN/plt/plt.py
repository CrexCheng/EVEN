import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
data_origin = {
    'Model': ['gpt4', 'llama', 'kimi', 'chatglm'],
    'Numerical': [0.675676, 0.567568, 0.216216, 0.972973],
    'Proportional': [0.702703, 0.405405, 0.324324, 0.918919],
    'Equality': [0.945946, 0.837838, 0.756757, 0.945946],
    'Equity': [0.108108, 0.013514, 0.054054, 0.72973],
    'Bais': [0.040541, 0.013514, 0, 0.756757]
}

data_Choice = {
    'Model': ['gpt4', 'llama', 'kimi', 'chatglm'],
    'Numerical': [0.297297, 0.027027, 0.459459, 0.027027],
    'Proportional': [0.162162, 0.027027, 0.10808, -0.02703],
    'Equality': [0.027027, 0.081081, 0, 0.054054],
    'Equity': [0.202703, 0.013514, 0.013514, -0.04054],
    'Bais': [0.175676, 0.013514, 0.040541, -0.04054]
}

data_COT = {
    'Model': ['gpt4', 'llama', 'kimi', 'chatglm'],
    'Numerical': [-0.08108, -0.13514, 0.756757, 0.027027],
    'Proportional': [-0.08108, -0.10811, 0.675676, 0.081081],
    'Equality': [0.027027, -0.24324, 0.216216, 0.054054],
    'Equity': [0.081081, 0.013514, 0.905405, 0.256757],
    'Bais': [0.040541, 0, 0.891892, 0.243243]
}

data_RAG2 = {
    'Model': ['gpt4', 'llama', 'kimi', 'chatglm'],
    'Numerical': [0.162162, -0.13514, 0.189189, 0.027027],
    'Proportional': [-0.13514, -0.2973, -0.24324, -0.13514],
    'Equality': [-0.05405, -0.2973, -0.05405, 0.027027],
    'Equity': [0.243243, 0.081081, 0.067568, 0.121622],
    'Bais': [0.040541, -0.01351, 0.013514, 0.081081]
}

data_RAG3 = {
    'Model': ['gpt4', 'llama', 'kimi', 'chatglm'],
    'Numerical': [0.027027, -0.37838, 0.054054, -0.13514],
    'Proportional': [-0.21622, -0.37838, -0.27027, -0.24324],
    'Equality': [-0.21622, -0.45946, -0.24324, -0.05405],
    'Equity': [0.135135, 0.027027, -0.01351, -0.05405],
    'Bais': [0.094595, 0, 0.013514, -0.01351]
}

data_RAG4 = {
    'Model': ['gpt4', 'llama', 'kimi', 'chatglm'],
    'Numerical': [-0.18919, -0.2973, 0.108108, -0.02703],
    'Proportional': [-0.48649, -0.40541, -0.21622, -0.08108],
    'Equality': [-0.32432, -0.43243, -0.2973, 0.054054],
    'Equity': [0.067568, -0.01351, -0.02703, 0.121622],
    'Bais': [-0.02703, -0.01351, 0, 0]
}

data_RAG5 = {
    'Model': ['gpt4', 'llama', 'kimi', 'chatglm'],
    'Numerical': [0.054054, 0.189189, 0.324324, 0.027027],
    'Proportional': [-0.02703, -0.10811, 0.10808, 0.081081],
    'Equality': [0, 0.081081, 0.081081, 0.054054],
    'Equity': [0.027027, 0.094595, 0.013514, 0.22973],
    'Bais': [0.054054, 0.297297, 0.094595, 0.162162]
}
# 设置全局字体大小
plt.rcParams.update({'font.size': 26})


# 函数：生成热力图
def create_heatmap(data, title, vmin, vmax, center, cmap, figsize=(15, 8)):
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
                     cbar_kws={'label': 'Value'},
                     linewidths=0.5,
                     square=True,
                     annot_kws={'size': 20, 'color': 'black'},
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

    # 获取 colorbar 并设置标签大小
    cbar = ax.collections[0].colorbar
    cbar.ax.tick_params(labelsize=20)
    cbar.set_label('Value', size=26)

    # 调整布局和标题
    plt.title(title, pad=20, size=26)
    plt.xticks(rotation=0)
    plt.tight_layout()

    return plt


# 创建原始数据热力图 (0-1范围)
heatmap1 = create_heatmap(
    data=data_origin,
    title='Fairness Notion Spectrum (Original)',
    vmin=0,
    vmax=1,
    center=0.5,
    cmap='YlOrRd'
)

# 显示原始数据热力图
heatmap1.show()

# 创建差异数据热力图 (-1到1范围，冷暖色调)
datasets = {
    'Choice': data_Choice,
    'COT': data_COT,
    'RAG2': data_RAG2,
    'RAG3': data_RAG3,
    'RAG4': data_RAG4,
    'RAG5': data_RAG5
}

for name, data in datasets.items():
    heatmap = create_heatmap(
        data=data,
        title=f'Fairness Notion Spectrum Difference',
        vmin=-1,
        vmax=1,
        center=0,
        cmap='coolwarm'  # 冷暖色调，蓝色表示负值，红色表示正值
    )
    heatmap.show()
