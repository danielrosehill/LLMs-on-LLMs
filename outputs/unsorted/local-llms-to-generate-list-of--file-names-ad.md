# Prompt

Suggest some LLMs I could run locally on this computer and which have an unusually long max output length / context size. I am trying to get the LLM to generate a list of 500 suggested file names for a project. Also tell me how to configure the frontend to enable an output of this length. I have available: LM Studio, Any LLM Desktop, Jan.

# Output

You are looking for local LLMs that can generate long outputs, specifically to produce a list of 500 suggested file names for a project. Based on your hardware setup and the available tools (LM Studio, Any LLM Desktop, and Jan), here are some suggestions:

## LLMs with Long Max Output Length

1. **Mistral 7B**: This model is known for its efficiency and can handle relatively long outputs. With its 7 billion parameters, it has been optimized for local use and works well with quantization (e.g., Q4 or Q6), which reduces memory usage while maintaining performance\[7]. It should be able to handle generating a list of 500 file names easily.
2. **LLaMA 3**: LLaMA models, especially the newer versions (e.g., LLaMA 3), are capable of handling longer context windows. You can run models like LLaMA 7B or even larger ones if your GPU has sufficient VRAM. LLaMA models are popular for local deployment and can be fine-tuned to extend their output length\[2]\[8].
3. **LongWriter (LLaMa 3.1 or GLM-9B)**: This is a specialized variant of LLaMa that is fine-tuned for generating long outputs (up to 20K tokens). It is designed specifically for tasks like generating large amounts of text in one go\[2].
4. **Claude (if available locally)**: While Claude is typically used via API, some users have managed to get it to output up to 50K tokens in one go. If you can find a local version of Claude or similar models, it could be worth trying\[2].

## Configuring Frontend for Long Outputs

To configure your frontend tools (LM Studio, Any LLM Desktop, or Jan) to handle long outputs, follow these steps:

### LM Studio

1. **Increase Max Tokens**: In LM Studio, you can adjust the maximum token limit in the settings. Ensure you set this high enough to accommodate the length of your output (e.g., set it to at least 2000 tokens for generating a list of 500 file names).
2. **Use Flash Attention**: Enable Flash Attention in the "Model Initialization" settings. This improves token generation speed and efficiency when working with large outputs\[7].
3. **Monitor Token Generation Speed**: LM Studio provides real-time feedback on token generation speed (tokens per second). If you're using GPU offloading, ensure it's enabled to maximize performance.

### Any LLM Desktop

1. **Adjust Token Limit**: Similar to LM Studio, Any LLM Desktop allows you to set a maximum token limit for output generation. Set this value according to your needs.
2. **Enable GPU Offloading**: If you're using a model that supports GPU acceleration, make sure GPU offloading is enabled in the settings to improve performance and handle larger outputs more efficiently.

### Jan

1. **Token Configuration**: Check if Jan allows you to customize the maximum token output in its settings or configuration files. Set this value high enough for your task.
2. **Chunking Long Outputs (if needed)**: If Jan struggles with very long outputs at once, consider breaking down the task into smaller chunks by prompting it multiple times and concatenating the results.

## Hardware Considerations

Your hardware setup (Intel i7-12700F CPU, AMD Radeon RX 7700 XT GPU, 64GB DDR5 RAM) is powerful enough to handle models like Mistral 7B and LLaMA 7B with GPU offloading\[1]. However, keep an eye on VRAM usage when running larger models or generating very long outputs since memory limitations can affect performance.

By configuring your frontend tools properly and selecting an appropriate model, you should be able to generate the list of 500 file names efficiently on your local machine.

Citations:\
&#x20;
