import pandas as pd
from typing import List, Dict
from config.config import Config
from models.chat_llm import GPT4Model, LLaMAModel, ChatGLMModel, KimiModel


def process_model_questions(model_name: str, questions: List[Dict]) -> List[str]:
    """Process questions using specified model"""
    model_map = {
        # "gpt4": GPT4Model(Config.GPT4_API_KEY, Config.GPT4_ENDPOINT),
        "llama": LLaMAModel(Config.LLAMA_API_KEY, Config.LLAMA_ENDPOINT),
        # "chatglm": ChatGLMModel(Config.CHATGLM_API_KEY, Config.CHATGLM_ENDPOINT),
        # "kimi": KimiModel(Config.KIMI_API_KEY, Config.KIMI_ENDPOINT)
    }

    model = model_map.get(model_name)
    if not model:
        raise ValueError(f"Unknown model: {model_name}")

    answers = []

    for i, q in enumerate(questions):
        if q["question"] == "-":
            answers.append("-")
            continue

        print(f"Processing question {i + 1}/{len(questions)}: {q['question']}")
        try:
            response = model.generate_response(q["question"])
            print(f"Response: {response}")
            processed_response = model.preprocess_response(response)
            answers.append(processed_response)
        except Exception as e:
            print(f"Error processing question {i + 1}/{len(questions)} with {model_name}: {e}")
            answers.append("不确定")

    return answers


def process_all_models(input_path: str):
    """Process questions with all models and save results"""
    try:
        df = pd.read_excel(input_path)
        if df.empty:
            raise ValueError("Input file is empty")
        questions = df.to_dict('records')
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    for model_name in Config.MODELS:
        print(f"\nProcessing {model_name}...")
        try:
            answers = process_model_questions(model_name, questions)
            print(answers)

            result_df = df.copy()
            result_df['answer'] = answers

            output_path = f"result3_{model_name}.xlsx"
            result_df.to_excel(output_path, index=False)
            print(f"Results saved for {model_name} at {output_path}")

        except Exception as e:
            print(f"Error processing {model_name}: {e}")


def main():
    input_path = "/data/output_data.xlsx"
    process_all_models(input_path)


if __name__ == "__main__":
    main()