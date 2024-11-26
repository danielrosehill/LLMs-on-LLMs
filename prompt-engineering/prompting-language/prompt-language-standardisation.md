---
title: "Standardisation of natural language in prompting."
---

20-Nov-24

# Prompt

> Have there been any attempts to develop formal standards for the natural language which humans use to prompt LLMs? Have there been any attempts to develop systematic standards for writing prompting expressions?

# Output

Yes, there have been several attempts to develop formal and systematic approaches to writing prompts for large language models (LLMs), though the field is still evolving. These efforts aim to improve the effectiveness, reliability, and precision of interactions with LLMs. Below are some key developments and approaches:

## 1. **Prompt Engineering Frameworks**
Prompt engineering has emerged as a discipline focused on crafting effective prompts for LLMs. Although there are no universally formalized standards yet, various frameworks and best practices have been proposed to guide how prompts should be structured. These include:

- **CARE Framework (Context, Ask, Rules, Examples)**: This framework advocates for including four key components in prompts: context (background information), ask (specific request), rules (constraints or guidelines), and examples (demonstrations of desired outcomes). This structured approach helps ensure that the LLM generates more accurate and relevant responses[9].
  
- **Few-shot prompting**: This involves providing a few examples of input-output pairs to help the model understand how it should process similar inputs. It is a widely used method to guide LLMs in tasks without additional training[9].

- **Chain-of-thought prompting**: This technique encourages the model to reason through a problem step-by-step, which can improve performance on complex tasks by mimicking human logical reasoning[1][7].

## 2. **Formal-LLM Framework**
A more formal approach is seen in the **Formal-LLM** framework, which integrates natural language with formal languages (like context-free grammars) to control the behavior of LLM-based agents. This framework allows users to express constraints or requirements using formal methods like automata theory. The goal is to ensure that generated outputs are valid and adhere to predefined rules, particularly in multi-step planning tasks[10]. This represents an effort to formalize how prompts can be structured for more complex applications.

## 3. **Best Practices for Writing Prompts**
Several organizations and researchers have proposed best practices that serve as informal standards for writing prompts. These include:

- **Clarity and Specificity**: Clear instructions help reduce ambiguity in the model's output. Vague or open-ended prompts often lead to less useful responses[3][4][5].
  
- **Contextual Information**: Providing relevant background information helps the model generate more contextually appropriate responses[2][5].
  
- **Task Breakdown**: Breaking down complex tasks into simpler subtasks improves accuracy by reducing cognitive load on the model[5].

## 4. **Interactive Prompting Systems**
Some systems have been developed to iteratively refine prompts based on user feedback. For example, tools like **nl2spec** allow users to translate natural language into formal specifications iteratively, refining sub-translations until the desired output is achieved[7]. This iterative process could be seen as a step toward creating more systematic standards for prompt writing.

## 5. **Attempts at Standardization**
While there are no universal standards yet akin to programming languages or markup languages, several guidelines have been proposed that could evolve into more formalized standards over time:

- **Static Context Descriptions**: Some frameworks suggest using static context descriptions or system messages to establish the role or function of the LLM in a conversation (e.g., customer service agent)[6].
  
- **Output Primers**: Techniques like "output primers" involve starting the desired response within the prompt itself to guide the model's output more precisely[1].

## Summary
Although there are no fully formalized standards for writing natural language prompts for LLMs yet, significant efforts are being made to develop systematic approaches. These include frameworks like CARE, techniques such as few-shot prompting and chain-of-thought reasoning, and more formal methods like the Formal-LLM framework that integrates natural language with formal constraints. As research continues, these approaches may evolve into more widely accepted standards for interacting with LLMs effectively.

Citations:
 