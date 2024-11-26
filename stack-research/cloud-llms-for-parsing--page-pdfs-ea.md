# Prompt

> Let's go back to my example of a 100 page PDF. This is towards the upper length of a corporate sustainability report, but it's not totally atypical. It would be useful to mine documents like this for insights - particularly to extract facts and figures. However, I would need an LLM that could not only pull those out, but also specify which page they appeared on, so that I could verify that the info was correct. Can you suggest cloud LLMs that would be suitable for this task and what approximate costs for running workloads like this might be?

# Output

To mine a 100-page corporate sustainability report for facts and figures, and ensure that the extracted information is linked back to specific pages for verification, you would need a large language model (LLM) with strong capabilities in text extraction, contextual understanding, and document segmentation. Below are some suitable cloud-based LLMs and their approximate costs:

## Suggested Cloud LLMs

### 1. OpenAI GPT-4

OpenAI's GPT-4 is highly effective for extracting facts and figures from PDFs due to its advanced natural language understanding and ability to handle complex queries. It can process large amounts of text while maintaining context across document sections. GPT-4 also allows for customizable outputs, such as specifying the page number where information was found.

- **Cost**:
  - GPT-4 (8K context): $0.06 per 1,000 input tokens and $0.12 per 1,000 output tokens.
  - GPT-4 (32K context): $0.12 per 1,000 input tokens and $0.24 per 1,000 output tokens.
  - For a 100-page PDF (\~50,000 tokens), processing could cost between $3 to $6 depending on the context size used\[4]\[5].

### 2. Google Gemini

Google's Gemini API offers advanced multimodal capabilities, including text extraction from PDFs. It excels at maintaining context over large documents and can integrate with Google's ecosystem for further processing (e.g., storing extracted data in BigQuery). Gemini is particularly useful if you're already working within Google's Cloud infrastructure.

- **Cost**:
  - Input: $0.075 per million tokens.
  - Output: $0.30 per million tokens.
  - For a 100-page document (\~50,000 tokens), the cost would be approximately $0.02 for input and $0.15 for output\[8]\[10].

### 3. Anthropic Claude 2

Claude models, particularly Claude 2, are designed to handle long documents with up to 100K token contexts. They are known for their safety features and contextual understanding, making them suitable for extracting structured data from complex documents like sustainability reports.

- **Cost**:
  - Claude Instant (100K context): $0.0016 per 1,000 input tokens and $0.0055 per 1,000 output tokens.
  - Claude 2 (100K context): $0.011 per 1,000 input tokens and $0.0327 per 1,000 output tokens.
  - Processing a typical report could cost around $2 to $3\[5].

### 4. Google Document AI

Google’s Document AI is specifically designed for extracting structured data from PDFs, including tables and figures. It integrates well with other Google Cloud services and can extract metadata like page numbers.

- **Cost**:
  - Layout Parser: $10 per 1,000 pages.
  - Summarizer: $25 per 1,000 pages.
  - For a single report of around 100 pages, this would cost approximately $1 to $2\[9].

## Other Considerations

### Preprocessing Tools

Before feeding your document into an LLM, you may need to preprocess the PDF using tools like `pdfplumber` or `PyMuPDF` to extract text while preserving formatting such as page numbers\[1]. This ensures that the LLM can correctly reference the location of extracted information.

### Chunking Large Documents

For very large documents (like those exceeding token limits), it’s important to chunk the text into manageable sections while maintaining contextual integrity. Tools like LlamaIndex or LayoutPDFReader can help by intelligently chunking sections based on headings or paragraphs\[6].

## Conclusion

For extracting facts and figures from a corporate sustainability report while linking them back to specific pages:

- **OpenAI GPT-4** is a strong option for detailed extraction with high accuracy.
- **Google Gemini** offers cost-effective processing with seamless integration into Google Cloud services.
- **Anthropic Claude** provides excellent long-context handling at competitive prices.

Costs will vary depending on the model used but expect to pay between **$2 to $6** per document based on token usage and model selection.

&#x20;






