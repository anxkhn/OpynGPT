# OpynGPT

![Picture1](https://github.com/anxkhn/OpynGPT/assets/83116240/be25ef97-9e61-42a4-bc2f-38cfecfc5c4c)

OpynGPT is a Python module that facilitates interactions with the OpenAI GPT-3.5 Turbo API to generate natural language responses based on user input. Notably, OpynGPT operates without requiring authentication or API keys, providing a straightforward and accessible tool for natural language generation.

## Prerequisites

Before using OpynGPT, ensure you have the following:

- Python 3.x installed
- The `requests` library installed. You can install it using:

  ```bash
  pip install requests
  ```

## Installation

You can install OpynGPT using pip:

```bash
pip install opyngpt
```

## Usage

1. Import the `prompt` function from OpynGPT:

   ```python
   from opyngpt import prompt
   ```

2. Use the `prompt` function to generate natural language responses:

   ```python
   user_input = "Write a factorial code in python."
   response = prompt(user_input)

   print(response)
   ```

## Features

- Sends user input to the GPT-3.5 Turbo API and receives natural language responses.
- No authentication or API keys required, making it hassle-free to use.
- Inspired by [tgpt](https://github.com/aandrew-me/tgpt/), OpynGPT utilizes a pool of users' data and the API from fakeopen.com.

## Contributing

If you'd like to contribute to OpynGPT, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the GPLv3 License - check out [this website](https://www.tldrlegal.com/license/gnu-general-public-license-v3-gpl-3) for more information.
