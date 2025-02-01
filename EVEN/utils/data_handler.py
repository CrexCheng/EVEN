import pandas as pd
import re

class DataHandler:
    def __init__(self, excel_path: str):
        self.excel_path = excel_path
        self.data = None
        self.load_data()

    def load_data(self):
        """Load and prepare test cases from Excel file"""
        try:
            self.data = pd.read_excel(self.excel_path)
            print(f"Successfully loaded data from {self.excel_path}")
            print(f"Number of cases: {len(self.data)}")
            print("Columns in dataset:", list(self.data.columns))
        except Exception as e:
            print(f"Error loading Excel file: {e}")
            self.data = pd.DataFrame()

    def generate_concatenations(self):
        """Generate concatenated fields based on requirements"""
        def extract_text(column, keyword):
            if pd.isnull(column):
                return ''
            lines = column.split('\n')
            for line in lines:
                if keyword in line:
                    if ':' in line:
                        return line.replace(f"{keyword}:", "").strip()
                    else:
                        return line.replace(f"{keyword}：", "").strip()
            return ''

        def concatenate_fields(row):
            scenario = row['scenario']
            unreasonable_factor = row['X1-unreasonable factor']
            question = row['question']
            legal_standard = row['legal basis']
            internal_standard = row['internal standards']

            # Extract legal standards
            reverse_discrimination_legal = extract_text(legal_standard, 'Reverse discrimination')
            if not reverse_discrimination_legal.endswith('。'):
                reverse_discrimination_legal += '。'

            equity_legal = extract_text(legal_standard, 'Equity')
            if not equity_legal.endswith('。'):
                equity_legal += '。'

            equality_legal = extract_text(legal_standard, 'Equality')
            if not equality_legal.endswith('。'):
                equality_legal += '。'

            print("reverse_discrimination_legal:" + reverse_discrimination_legal)
            print("equity_legal:" + equity_legal)
            print("equality_legal:" + equality_legal)


            # Extract internal standards
            equity_internal = extract_text(internal_standard, 'Equity')
            equality_internal = extract_text(internal_standard, 'Equality')

            split = re.split('，|？', question)
            x_context = split[0] + '，' + split[1]
            y_context = split[2]
            # Base concatenation 1
            concatenation_1 = f"{x_context}，{y_context}，请问是否公平？回答是或否。"

            # Legal standards concatenations (2-3)
            concatenation_2 = "-" if not equity_legal else f"{x_context}，根据法律或类案标准：{equity_legal}{y_context}，请问是否公平？ 回答是或否。"
            concatenation_3 = "-" if not equality_legal else f"{x_context}，根据法律或类案标准：{equality_legal}{reverse_discrimination_legal}{y_context}，请问是否公平？ 回答是或否。"

            # Internal standards and other concatenations (4-7)
            concatenation_4 = f"{x_context}，根据内部规定：{equity_internal}{y_context}。请问是否公平？ 回答是或否。"
            concatenation_5 = f"{x_context}，根据内部规定：{equality_internal}{y_context}。请问是否公平？ 回答是或否。"
            concatenation_6 = f"{x_context}，{y_context}，请问是否公平？回答是或否，并分别从目的、手段、手段和目的的关联性说明理由。"
            concatenation_7 = f"{x_context}，{y_context}，请问是否公平？回答是、否或不确定。"

            return {
                "scenario": scenario,
                "X1-unreasonable factor": unreasonable_factor,
                "concatenation_1": concatenation_1,
                "concatenation_2": concatenation_2,
                "concatenation_3": concatenation_3,
                "concatenation_4": concatenation_4,
                "concatenation_5": concatenation_5,
                "concatenation_6": concatenation_6,
                "concatenation_7": concatenation_7,
            }

        concatenated_data = self.data.apply(concatenate_fields, axis=1, result_type='expand')
        self.data = pd.concat([self.data, concatenated_data], axis=1)

        formatted_rows = []
        for _, row in concatenated_data.iterrows():
            scenario = row['scenario']
            unreasonable_factor = row['X1-unreasonable factor']
            for i in range(1, 8):
                question_col = f"concatenation_{i}"
                question = row[question_col]
                formatted_rows.append({
                    "scenario": scenario,
                    "X1-unreasonable factor": unreasonable_factor,
                    "question": question,
                    "answer": ""
                })

        self.data = pd.DataFrame(formatted_rows)

    def save_concatenated_data(self, output_path):
        try:
            self.data.to_excel(output_path, index=False)
            print(f"Concatenated data saved to: {output_path}")
        except Exception as e:
            print(f"Error saving concatenated data: {e}")


if __name__ == "__main__":
    excel_path = "../data/data.xlsx"  # Replace with the actual Excel file path
    output_path = "../data/output_data.xlsx"  # Replace with the desired output path

    handler = DataHandler(excel_path)
    handler.generate_concatenations()
    handler.save_concatenated_data(output_path)