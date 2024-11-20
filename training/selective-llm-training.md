---
title: "Selective LLM training data
---

20-Nov-24

# Prompt

LLMs are typically described as having been trained on "vast" amounts of data. Have there been efforts to be more selective about what kind of data is included in the training?

# Output

You asked whether there have been efforts to be more selective about the kind of data included in training large language models (LLMs), given that they are typically described as being trained on vast amounts of data. Yes, there have been significant efforts to improve data selection for LLMs, particularly as the scale of these models and their training datasets has grown. These efforts aim to enhance model performance, reduce computational costs, and ensure that the data used aligns with specific objectives.

Here are some key approaches and trends in selective data inclusion for LLMs:

## **1. Data Curation for Pretraining**
In large-scale pretraining, it is not always optimal or feasible to train on all available data due to varying quality and relevance. Several methods have been developed to filter out low-quality or irrelevant data:
- **Data Filtering**: Many pretraining pipelines use filters to exclude noisy or low-quality data. For example, models like GPT-3 were trained on vast datasets but employed various filtering techniques to remove irrelevant or harmful content[4].
- **Model-based Curation**: Recent approaches involve using model-based criteria to curate data during pretraining. Instead of selecting individual examples, some methods optimize batch-level selection, which can accelerate training by choosing batches that provide better learning signals[1].

## **2. Data Selection for Fine-Tuning**
Fine-tuning LLMs on domain-specific tasks often requires more careful data selection:
- **Principled Data Selection**: Some methods focus on selecting data that best aligns with the target distribution or task at hand. For example, researchers have used Optimal Transport-based techniques to select samples that efficiently fine-tune models without needing vast amounts of domain-specific data[2]. This approach can significantly reduce the cost of fine-tuning while achieving high performance.
- **LESS Algorithm**: The LESS (Learning Efficient Sample Selection) algorithm is another example of an optimized approach for instruction-tuning LLMs. It selects a small portion (e.g., 5%) of the available dataset, which can outperform training on the full dataset by focusing on examples most relevant to the task[5].

## **3. Task-Specific and Values-Based Curation**
In some cases, LLMs are fine-tuned using highly curated datasets designed to align with specific behavioral or ethical values:
- **Values-Targeted Fine-Tuning**: OpenAI has explored fine-tuning models using small, curated datasets (e.g., fewer than 100 examples) that target specific behavioral values. This method allows models to better adhere to desired behaviors in specific contexts without compromising general performance[3].

## **4. Online and Dynamic Data Selection**
Another trend is *online* or *dynamic* data curation, where the relevance of training examples is reassessed throughout the training process:
- **Adaptive Curation**: Online methods adjust which data points are selected based on how much the model has already learned from previous examples. This dynamic approach ensures that the model focuses on harder or more informative examples as training progresses[1].

## **5. Reducing Redundancy and Semantic Overlap**
Efforts have also been made to reduce redundancy in training datasets:
- **Core-Set Selection**: Some methods prune datasets by identifying and removing semantically redundant examples. This helps reduce computational overhead and ensures that only diverse and informative samples are used during training[1].

In summary, while LLMs are initially trained on vast amounts of data, there is a growing emphasis on being selective about what kind of data is included at various stages of training—whether during pretraining, fine-tuning, or instruction-tuning. These efforts aim to improve efficiency, reduce costs, and ensure better alignment with task-specific goals or ethical considerations.

 