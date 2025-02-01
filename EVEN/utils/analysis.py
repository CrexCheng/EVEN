import openpyxl
import re


# 读取xlsx文件
def count_punctuation(file_path):
    # 打开xlsx文件
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active  # 默认选择第一个工作表

    # 定义中文逗号和问号的正则表达式
    comma_pattern = re.compile(r'，')  # 中文逗号
    question_pattern = re.compile(r'？')  # 中文问号

    # 获取列名为 'question' 的列索引
    header_row = sheet[1]  # 假设第一行为表头
    question_col_index = None

    # 查找'question'列
    for idx, cell in enumerate(header_row, start=1):  # start=1确保从第1列开始
        if cell.value == 'question':
            question_col_index = idx
            break

    if question_col_index is None:
        print("未找到 'question' 列")
        return

    # 遍历从第二行开始的数据
    for row in sheet.iter_rows(min_row=2, min_col=question_col_index, max_col=question_col_index):
        question_text = row[0].value  # 获取该单元格的值

        if question_text:  # 如果单元格不为空
            comma_count = len(comma_pattern.findall(question_text))  # 统计中文逗号的数量
            question_count = len(question_pattern.findall(question_text))  # 统计中文问号的数量

            # 检查逗号和问号的数量是否符合要求
            if comma_count != 3 or question_count != 1:
                # 输出行号（行号是基于1的）
                row_num = row[0].row
                print(f'第 {row_num} 行：中文逗号数量为 {comma_count}，中文问号数量为 {question_count}')


# 调用函数并传入文件路径
file_path = '../data/data.xlsx'  # 请替换为你的文件路径
count_punctuation(file_path)
