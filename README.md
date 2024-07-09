# OpynGPT

![Picture1](https://github.com/anxkhn/OpynGPT/assets/83116240/be25ef97-9e61-42a4-bc2f-38cfecfc5c4c)

## Supercharge your projects with the Power of Large Language Models.

[![Current Version : ](https://img.shields.io/badge/Version-0.4.0-blue.svg)](https://pypi.org/project/opyngpt/0.4.0/)
[![Downloads](https://img.shields.io/pepy/dt/opyngpt?label=Downloads)](https://pepy.tech/project/opyngpt)


OpynGPT is a Python module that empowers developers to effortlessly harness the capabilities of large language models (LLMs) without the need for authentication or API keys. Designed with simplicity and accessibility in mind, OpynGPT supercharges your Python projects by providing natural language generation and understanding capabilities, making it an invaluable tool for developers of all skill levels.

## Key Features

- **No API Keys Required**: OpynGPT eliminates the hassle of acquiring and managing API keys, providing a seamless and straightforward integration with language models.
- **Natural Language Generation**: Leverage the power of LLMs to generate human-like text responses based on your input prompts, enabling a wide range of applications such as chatbots, content generation, and more.
- **Beginner-Friendly**: With its intuitive interface and easy-to-use functions, OpynGPT is the perfect starting point for developers new to language models, allowing them to explore and experiment with ease.
- **Command-Line Interface**: Interact with OpynGPT via the command line for both interactive sessions and single queries, providing flexibility and ease of use directly from the terminal.
- **Phind Model Integration**: Inspired by the renowned [tgpt](https://github.com/aandrew-me/tgpt/) project, OpynGPT utilizes the powerful Phind Model, ensuring high-quality language generation and understanding capabilities.
- **Open-Source**: OpynGPT is an open-source project, allowing developers to contribute, customize, and extend its functionality to suit their specific needs and requirements.

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

To install the latest version from the GitHub repository, use:

```bash
pip install git+https://github.com/anxkhn/OpynGPT.git
```

## Usage

### OpynGPT in python applications is straightforward and easy.

Here's a quick guide to get you started:

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

### OpynGPT Command Line Interface

### Interactive Mode:

To enter the interactive mode, simply open your terminal and type `opyngpt`. Then you can enter your messages and receive responses interactively. Type `exit` or press `Ctrl+C` to quit the interactive mode.

Example:

```
$ opyngpt
Enter your message (type 'exit' to quit): Hello, how are you?
[OpynGPT]: I'm doing well, thank you for asking. How can I assist you today?
Enter your message (type 'exit' to quit): What is the capital of France?
[OpynGPT]: The capital of France is Paris.
Enter your message (type 'exit' to quit): exit
```

### Single Query:

To make a single query, use `opyngpt "your query"` in your terminal, replacing `"your query"` with your actual query.

Example:

```bash
$ opyngpt "What is the capital of Japan?"
[OpynGPT]: The capital of Japan is Tokyo.
```

## Changelog

### Version 0.4.0

- Added support for prompt with context
- Interactive Mode now supports context
- Special thanks to [@devout-coder](https://github.com/devout-coder/) for the contribution

### Version 0.3.0

- Added Command Line Interface (CLI)
- Added Interactive Mode to CLI
- Improved error handling

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
