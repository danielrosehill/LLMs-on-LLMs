---
title: "Is training data always open source?"
---

20-Nov-24

# Prompt

Is the training data that LLMs are trained on open source or do vendors have to buy it? Do both kinds exist?

# Output

The training data used to develop large language models (LLMs) can be either open-source or proprietary, and both types are commonly used depending on the model and its intended application.

### **Open-Source Training Data**
Many LLMs are trained on open-source datasets, which are freely available to the public. These datasets are often sourced from publicly accessible web pages, books, research papers, and other forms of text. Open-source datasets are crucial for democratizing AI development, enabling researchers and developers to train and fine-tune models without relying on proprietary data. Examples of widely used open-source datasets include:

- **Common Crawl**: A massive dataset of web pages scraped from the internet, frequently used in LLM training[3][4].
- **The Pile**: An 800 GB dataset curated from diverse sources like academic papers, GitHub repositories, and Wikipedia[3].
- **C4 (Colossal Clean Crawled Corpus)**: A 750 GB dataset derived from Common Crawl but heavily cleaned to remove gibberish and low-quality text[3].
- **RedPajama**: A dataset designed to replicate the training data used for Meta's LLaMA model, consisting of over 1.2 trillion tokens from sources like Common Crawl, GitHub, and Wikipedia[4].

These datasets provide a broad range of linguistic styles and contexts, helping models generalize across different domains. Open-source data is particularly valuable for academic research and smaller organizations that need cost-effective solutions.

### **Proprietary Training Data**
Some LLMs are trained on proprietary datasets that vendors either create or purchase. Proprietary data can include high-quality, curated text from sources that are not publicly available or require licensing fees. This type of data is often used by companies that want to maintain a competitive edge by training their models on unique or specialized content. For example:

- **GPT models by OpenAI**: Although OpenAI initially started as an open-source project, it has since transitioned to using proprietary data for its GPT models[1].
- **Claude by Anthropic**: Another example of a closed-source model where the training data is not publicly disclosed[1].

Proprietary datasets may also be purchased from third-party providers who specialize in collecting and cleaning large volumes of text data. These vendors often offer comprehensive solutions that include regularly updated and validated data for LLM training[6].

### **Hybrid Approach**
In practice, many LLMs use a combination of both open-source and proprietary datasets. For instance, some models might be trained on publicly available web data but fine-tuned using specialized proprietary datasets to improve performance in specific domains like legal or medical texts.

### **Conclusion**
There are both open-source and proprietary types of training data for LLMs. Open-source datasets are widely used and accessible to the public, fostering innovation and collaboration in AI development. However, proprietary datasets are also common, especially for commercial applications where companies seek higher-quality or domain-specific training data that gives them a competitive advantage.

 