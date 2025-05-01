# EVENS: Equality versus Equity Notion Spectrum of LLMs

The controversy surrounding COMPAS, a tool used to assess the risk of criminal recidivism, reveals a significant gap in the concept of bais between computer science and social science, highlighting the necessity of aligning computational fairness metrics with humanistic interpretations.

In response, we propose **EVENS** (*Equality versus Equity Notion Spectrum of LLMs*), a framework for evaluating the differential understanding of "equality" and "equity" in large language models. Our main contributions include:

1. Constructing an *equality–equity* conceptual spectrum based on logical statements and generating a corresponding dataset incorporating multiple key fairness issue scenarios.
2. Testing the initial stance of models by injecting this dataset and evaluating their stance adjustment under external legal regulations and internal organizational norms using Retrieval-Augmented Generation (*RAG*); introducing Chain-of-Thought (*CoT*) prompting to guide models in fairness reasoning; and adding an *uncertainty* option to observe its impact on model responses.

Our findings indicate that large language models initially favor equality over equity, as they focus on the formal unbiasedness of data and fail to deeply reason about substantive equity. Employing RAG to introduce equity-related external legal regulations and internal organizational norms can prompt models to adjust their stance and better understand the concept of equity. CoT significantly improves the equity reasoning of Chinese models but may also facilitate the rationalization of their own biases. The *uncertainty* option makes model responses more cautious.

The following sections introduce the data, environment setup, experiment execution, metric calculation, and significance testing methods.

## Data Acquisition and Introduction

**Step 1: Identification of Prohibited Discrimination Factors**

We began by referencing *The Universal Declaration of Human Rights* (UDHR) and national constitutions to identify commonly cited discriminatory factors. Through preliminary text analysis and synthesis, we identified 11 core discriminatory factors (e.g., race, gender, religion, disability). These factors represent the most frequently cited unreasonable elements in legal frameworks addressing equality and anti-discrimination.

**Step 2: Expert-Guided Scenario Identification**

A panel of four legal experts analyzed and extracted real-world fairness scenarios from Chinese and English resources, including:

- Legal literature and case law (e.g., international law journals, Supreme Court decisions)
- Judgment databases (e.g., Westlaw, China Judgments Online)
- News articles (e.g., Reuters, Xinhua News)

For each factor, experts identified at least three distinct fairness scenarios highlighting tensions between equality (same treatment) and equity (context-sensitive fairness), such as affirmative action, disability accommodations, and gender quotas.

**Step 3: Element  Extraction**

Legal experts extract **elements** from these materials, including:

**Reasonable Factors (XR)：**Differential standards directly relevant to decision-making objectives and verifiable through objective criteria.

**Examples**: Academic performance, professional competency, work experience.

**Unreasonable Factors (XU):** Differential standards that lack inherent relevance to decision-making objectives and are explicitly prohibited by law or social norms.

**Examples**: Race, gender, religion, disability (e.g., discriminatory factors prohibited under Article 2 of the *Universal Declaration of Human Rights*).

**Outcomes (Y):** Defined tangible results of resolving fairness conflicts (e.g., legal compliance, social backlash).The actual result of opportunity or resource allocation, reflecting how fairness principles are implemented in decision-making. 

Example：College admissions, hiring outcomes, Loan Eligibility 

**Scenario(S):**  For each Unreasonable factor, experts identify at least three distinct fairness scenarios where tensions or conflicts between equality and equity  are prominent.

Example：Workplace, education, housing. 

**Step 4: External Standard Retrieval**

Using a Retrieval-Augmented Generation (RAG) approach, we systematically retrieved legal standards related to equality and equity from:

- International conventions (e.g., UN treaties)
- Domestic statutory laws
- Regional precedents

**Step 5: Automated Data Augmentation**

By combining regular expressions and large language models (LLMs), we automated scenario element replacement to ensure structural consistency. For each factor, we generated:

- **3 unique scenarios per factor**, resulting in a baseline dataset of 333 entries.
- **Multi-layered evaluations**: Each scenario underwent 4 RAG, CoT (chain-of-thought), and choice-based detection methods across 4 models, yielding 9,324 data points.

**Step 6: Evaluation and Validation**

The expert panel verified:

1. **High-frequency relevance**: Scenarios reflect real-world contexts supported by legal/societal discourse.
2. **Strong factor associations**: Extracted factors (X) and outcomes (Y) exhibit high correlation with their respective scenarios.

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

### Code 1 **Model Dialogues**

This code aggregates and standardizes binary ("Yes"/"No") responses from four models（GPT 4, Llama, ChatGLM, Kimi）across various bias-related scenarios, outputs four files: `../model_result/{llm-name}.xlsx`

### Code 2 Notion ratio

Calculate the ratio of the fairness notion corresponding to each question number (e.g., Question 5 corresponds to "equality") by computing the number of responses categorized as "yes" or "uncertain" divided by the total number of questions for that notion. Exclude cases where there are conflicting notions (two contradictory notions). outputs four folders: `../metrics/{llm-name}`

### Code 3 Difference of RAG, COT and Choice

Calculate the difference to **comparing post-adjustment values** (e.g., after applying RAG, COT, or accounting for uncertain choices) against **baseline/original values** to quantify how specific fairness notions (equity/equality) are strengthened (+) or weakened (-) by each refinement approach

## Significance Testing Methods

Use **Significance Testing Methods** to further investigate whether there are statistically significant differences in the model's stances across different fairness notions, as well as whether significant changes occur after applying **RAG**, **COT**, and **Uncertain Choice**.

### **T0 Hypotheses (Null Hypotheses)**

1. **T0-1 (Equity vs. Equality Distribution Test)**
    
    There is **no significant difference** in the distributions of "Equity" and "Equality," meaning the model's stance on these two fairness concepts is consistent.
    
2. **T0-2 (RAG vs. Original Stance Association Test)**
    
    **RAG** (external regulations or internal norms) shows **no significant association** with the model's original stance ("Origin") in the distribution of "Equity/Equality," indicating RAG adjustments do not alter the model's fairness positions.
    
3. **T0-3 (COT vs. Original Stance Association Test)**
    
    **COT** (Chain-of-Thought) shows **no significant association** with the model's original stance ("Origin") in the distribution of "Equity/Equality," meaning COT adjustments do not change the model's fairness positions.
    
4. **T0-4 (Uncertain Choice vs. Original Stance Association Test)**
    
    The model's **Uncertain Choice** shows **no significant association** with the original stance ("Origin") in the distribution of "Equity/Equality," indicating uncertain choices do not affect fairness stances.
    

### **Key SPSS Operation Steps**

1. **Data Preparation**
    - Encode variables as categorical data (e.g., `Equity=1`, `Equality=0`; `RAG=1`, `Origin=0`).
    - For frequency-weighted data, use **Data > Weight Cases** to apply weighting.
2. **Chi-Square Test Execution**
    - Navigate to **Analyze > Descriptive Statistics > Crosstabs**.
    - Place the fairness variable (e.g., `Equity/Equality`) in **Rows** and the adjustment method variable (e.g., `RAG/Origin`) in **Columns**.
    - Click **Statistics**, check **Chi-square** and **Phi/Cramer’s V** (effect size).
3. **Result Interpretation**
    - **`p ≤ 0.01`** → Label as **`**`** (Highly significant, strong evidence to reject the null hypothesis)
    - **`0.01 < p ≤ 0.05`** → Label as **`*`** (Statistically significant, moderate evidence)
    - **`0.05 < p ≤ 0.1`** → Label as  (Marginally significant, weak evidence)
    - **`p > 0.1`** → No annotation (No statistical significance)
