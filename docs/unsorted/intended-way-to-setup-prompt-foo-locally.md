**Promptfoo** is a tool designed for testing, evaluating, and improving prompts used with Large Language Models (LLMs). The intended way to use it in a local environment involves several key steps:

### 1. Installation

You can install Promptfoo in multiple ways depending on your preferences:

- **Using npm**: Install it globally with `npm install -g promptfoo` or locally in your project directory with `npm install promptfoo`.
- **Using npx**: Run `npx promptfoo@latest init` to use it without installation.
- **Using Homebrew**: If you prefer Homebrew, run `brew install promptfoo`.
- **From source**: Clone the repository from GitHub and build it locally for development purposes.

### 2. Setup

Once installed, the first step is to initialize a configuration file in your project directory by running:

```bash
npx promptfoo@latest init
```

This generates a placeholder `promptfooconfig.yaml` file, which you will customize based on your prompts, variables, and test cases.

### 3. Defining Prompts and Tests

- **Prompts**: Define your prompts in separate text files (e.g., `prompt1.txt`). You can use templating engines like Nunjucks to include variables in the prompts.
- **Tests**: In the `promptfooconfig.yaml`, specify the prompts, LLM providers (e.g., OpenAI, local models), and the test cases. For each test case, you can define variables and assertions to evaluate the output quality.

Example of a simple test configuration in `promptfooconfig.yaml`:

```yaml
description: "Creative Storytelling"
prompts: [prompt1.txt]
providers:
  - id: "openai:gpt-3.5-turbo"
    config:
      temperature: 0.7
      max_tokens: 1000
tests:
  - vars:
      topic: "a mysterious island"
    assert:
      - type: cost
      - type: content
```

### 4. Running Evaluations

Once your configuration is ready, run the evaluation using:

```bash
npx promptfoo@latest eval
```

This command will execute the tests defined in your configuration file and evaluate the outputs based on the criteria you set (e.g., cost, content relevance). You can also specify additional options such as output format (`csv`, `json`, etc.) or concurrency limits.

### 5. Viewing Results

Promptfoo supports different output formats for viewing results. You can output results as CSV, JSON, YAML, or even HTML for easy visualization of side-by-side comparisons of LLM outputs.

```bash
npx promptfoo@latest eval --output results.html
```

### 6. Advanced Usage

For more advanced setups:

- Use Docker to self-host Promptfoo if you want to centralize evaluations across teams.
- Integrate Promptfoo into CI/CD pipelines for continuous testing of LLMs.
- Customize provider configurations and manage API keys directly through environment variables or configuration files.

By following these steps, you can effectively use Promptfoo to test and refine your LLM prompts locally\[1]\[2]\[4].

Citations:\
&#x20;






