**Summary of the prompt:** You are asking for recommendations of image generation programs with **GUIs** that are compatible with **Fedora**.

Here are some of the best **GUI-based image generation programs** for **Fedora Linux**:

### 1. InvokeAI

**InvokeAI** is one of the most popular GUI-based tools for **Stable Diffusion** and other AI image generation models. It provides a simple interface for text-to-image generation and image manipulation.

#### Features:

- User-friendly **web-based GUI** and **command-line interface** (CLI).
- Supports **inpainting**, **outpainting**, and **image editing**.
- Local installation ensures you don’t need to rely on cloud-based services.
- **Stable Diffusion** support for generating high-quality images.

#### Installation on Fedora:

InvokeAI is a Python-based tool that runs on Fedora.

1. Install Python 3 and dependencies:
   ```bash
   sudo dnf install python3 python3-pip git
   ```
2. Clone the InvokeAI repository and set it up:
   ```bash
   git clone https://github.com/invoke-ai/InvokeAI.git
   cd InvokeAI
   pip install -r requirements.txt
   ```
3. Run the application and access the GUI via your browser:
   ```bash
   python3 scripts/invoke.py --web
   ```

#### Use Case:

InvokeAI is perfect if you are looking for a **fully local image generation tool** that allows you to experiment with different models and do image editing as well.

#### Link:

- [InvokeAI GitHub](https://github.com/invoke-ai/InvokeAI)


### 3. DiffusionBee (Linux Alternative: InvokeAI)

**DiffusionBee** is popular on macOS, but for Fedora Linux, the best alternative would be **InvokeAI**, which provides similar functionality for **Stable Diffusion** with a GUI. Since InvokeAI has been mentioned earlier, DiffusionBee doesn’t directly support Linux.


### \*\*5. Artbreeder (Web-based AI Art Generator)

**Artbreeder** is a web-based AI image generation tool that lets users create images by combining or "breeding" images. While it is not a local application, it runs smoothly on Linux through any browser and offers a fun, visual interface for creating AI-generated art.

#### Features:

- Browser-based, so no need for installation.
- Allows mixing and evolving images using **AI models**.
- Supports fine-tuning parameters like face generation, landscapes, and abstract art.

#### Use Case:

Artbreeder is ideal if you are looking for a **lightweight and creative** tool that runs directly in your browser on Fedora, without needing any heavy installations.

#### Link:

- [Artbreeder](https://www.artbreeder.com/)






