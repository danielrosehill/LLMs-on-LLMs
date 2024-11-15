# Prompt

You've converted my resume, which was a PDF, into an optimised markdown file and into JSON. As I explained, the purpose of the exercise was to store the data as context so that I can use it in future prompting (so that I don't need to explain what I do and where I work every time). Which format is more useful for this purpose? If none of them, can you suggest a better format?

# Output

For the purpose of storing and referencing your resume information for future prompting, the **Markdown** format is generally more useful because it is human-readable and structured in a simple and clear way, making it easier to quickly interpret and modify if needed. It also works well in most text-based environments, including those for AI models like ChatGPT.

Here’s why Markdown might be preferable:

1. **Human-Friendly**: Markdown is simple to read and doesn't require specialized knowledge to understand the content.
2. **Prompt Compatibility**: When you're using LLMs like ChatGPT, a Markdown format is easy for the model to interpret, and it closely mirrors how text is structured for consumption.
3. **Adjustability**: You can easily adjust or update your information without needing complex syntax as in JSON.
4. **No Parsing Required**: Markdown doesn’t need to be parsed like JSON, so it directly serves as input in conversation without needing conversion.

**JSON**, while machine-readable and structured, may not be as easily editable or interpretable in real-time, unless you're dealing with structured data processing or API integration. If your context is primarily text-based interaction, JSON might add unnecessary complexity.

**Suggestion**: For the use case of keeping the resume as a reference for prompting, storing it in Markdown format (or similar simple text) would likely be the most efficient choice. If you are looking to add structured data for automation purposes or API calls, then JSON might be useful, but for general LLM prompting, Markdown will likely suffice.

Would you like me to store the content in Markdown format as your resume reference for future prompts?