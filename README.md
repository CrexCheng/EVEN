# EVENS: Equality versus Equity Notion Spectrum of LLMs

EVENS summary xxxxxxxxxxxxxxxxxxxxxxxx.

The following sections introduce the data, environment setup, experiment execution, metric calculation, and significance testing methods.

## Data Acquisition and Introduction

The data can be obtained from xxxx, primarily containing five columns: scenario, X1-unreasonable factor, question, legal basis, and internal standards.

## Environment Setup

You can set up the required Python environment for experiments and metric calculations by running the following code:

```bash
pip install -r ../requirements.txt
```

## Experiment Execution

The experiment execution includes two steps: data processing and experiment running.

### Data Processing

First, please place the acquired data in `../data/data.xlsx`.
Next, run the `../utils/data_handler.py` file to obtain the required data format for the next step. The output will be `../data/output_data.xlsx`.

### Running Experiments

First, replace the API keys and endpoints for GPT, LLAMA, CHATGLM, and KIMI in the `../config/config.py` file. Then run `../main.py` to get the experimental results, which will output four files: `../model_result/result_{llm-name}.xlsx`.

## Metric Calculation

Run three code blocks in `../calculate/calculate.py`:

Code 1 xxxxxxxxxxxxxxxxxxxx, outputs four files: `../model_result/{llm-name}.xlsx`

Code 2 xxxxxxxxxxxxxxxxxxxx, outputs four folders: `../metrics/{llm-name}`

Code 3 xxxxxxxxxxxxxxxxxxxx

## Significance Testing Methods

xxxxxxxxxxxxxxxxxxxx
