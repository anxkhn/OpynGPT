# OpynGPT

![Picture1](https://github.com/anxkhn/OpynGPT/assets/83116240/be25ef97-9e61-42a4-bc2f-38cfecfc5c4c)

## Supercharge your projects with the Power of Large Language Models.

OpynGPT is a Python module that empowers developers to effortlessly harness the capabilities of large language models (LLMs) without the need for authentication or API keys. Designed with simplicity and accessibility in mind, OpynGPT supercharges your Python projects by providing natural language generation and understanding capabilities, making it an invaluable tool for developers of all skill levels.

## Key Features

- **No API Keys Required**: OpynGPT eliminates the hassle of acquiring and managing API keys, providing a seamless and straightforward integration with language models.
- **Natural Language Generation**: Leverage the power of LLMs to generate human-like text responses based on your input prompts, enabling a wide range of applications such as chatbots, content generation, and more.
- **Beginner-Friendly**: With its intuitive interface and easy-to-use functions, OpynGPT is the perfect starting point for developers new to language models, allowing them to explore and experiment with ease.
- **Phind Model Integration**: Inspired by the renowned [tgpt](https://github.com/aandrew-me/tgpt/) project, OpynGPT utilizes the powerful Phind Model, ensuring high-quality language generation and understanding capabilities.

## Getting Started

### Prerequisites

Before diving into OpynGPT, ensure you have the following prerequisites installed:

- Python 3.x
- The `requests` library (Install using `pip install requests`)

### Installation

Installing OpynGPT is as simple as running the following command:

```bash
pip install opyngpt
```

### Usage

Leveraging the power of OpynGPT is straightforward:

1. Import the `prompt` function from the OpynGPT module:

```python
from opyngpt import prompt
```

2. Use the `prompt` function to generate natural language responses based on your input:

```python
user_input = "Write a factorial code in Python."
response = prompt(user_input)
print(response)
```

OpynGPT will process your input and return a relevant response, empowering you to integrate language models into your projects seamlessly.

## Changelog

### Version 0.2.0

- Switched to Phind Model

### Version 0.1.4

- Bug free working version with proper error handling

### Version 0.1.0

- Initial release with basic functionality released as _FreeGPTpy_

## Contributing

We welcome contributions from the community to make OpynGPT even better. If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them
4. Push your changes to your forked repository
5. Submit a pull request to the main repository

## License

OpynGPT is licensed under the GPLv3 License. For more information about this license, please visit [this website](https://www.tldrlegal.com/license/gnu-general-public-license-v3-gpl-3).
