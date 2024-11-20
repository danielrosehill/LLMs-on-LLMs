---
title: "Major LLM Evaluation Frameworks"
---

20-Nov-24

| **Benchmark/Framework**       | **Description**                                                                 | **Metrics**                                      |
|-------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------|
| **MMLU (Massive Multitask Language Understanding)** | Evaluates multitask accuracy across 57 tasks from diverse domains.                       | Coherence, relevance, detail, clarity             |
| **GLUE (General Language Understanding Evaluation)** | Tests language understanding through nine tasks like sentiment analysis and QA.          | Accuracy, F1 score                               |
| **SuperGLUE**                  | Extension of GLUE with more complex reasoning and comprehension tasks.           | Accuracy, F1 score                               |
| **TruthfulQA**                 | Evaluates the truthfulness of LLMs by testing their ability to avoid falsehoods. | Truthfulness percentage, informativeness         |
| **HellaSwag**                  | Tests commonsense reasoning by asking models to complete logically consistent sequences. | Accuracy                                         |
| **DeepEval**                   | Open-source framework with 14+ evaluation metrics for summarization and hallucination detection. | Answer relevancy, contextual recall/precision, hallucination detection |
| **RAGAs (Retrieval-Augmented Generation Assessment)** | Evaluates RAG pipelines focusing on faithfulness and contextual relevancy.               | Faithfulness, contextual precision/recall        |
| **Eleuther AI**                | Supports 200+ evaluation tasks and powers Hugging Face’s Open LLM Leaderboard.   | Task-specific accuracy                           |
| **MLFlow LLM Evaluate**        | Modular framework for evaluating LLMs with support for RAG pipelines and QA tasks. | QA correctness, answer relevancy                 |
| **HumanEval (OpenAI)**         | Assesses code generation by testing generated code against predefined test cases. | Code correctness (pass/fail rate)                |
