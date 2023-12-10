from setuptools import setup, find_packages

setup(
    name='opyngpt',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='Python module for interacting with the OpenAI GPT-3.5 Turbo API without authentication.',
    long_description="""
OpynGPT is a Python module that facilitates interactions with the OpenAI GPT-3.5 Turbo API to generate natural language responses based on user input. Notably, OpynGPT operates without requiring authentication or API keys, providing a straightforward and accessible tool for natural language generation.

Prerequisites
-------------

Before using OpynGPT, ensure you have the following:

- Python 3.x installed
- The `requests` library installed. You can manually install it using:

  ::
  
    pip install requests

Installation
------------

You can install OpynGPT using pip:

::

  pip install opyngpt

Usage
-----

1. Import the `prompt` function from OpynGPT:

::

  from opyngpt import prompt

2. Use the `prompt` function to generate natural language responses:

::

  user_input = "Write a factorial code in python."
  response = prompt(user_input)

  print(response)

Features
--------

- Sends user input to the GPT-3.5 Turbo API and receives natural language responses.
- No authentication or API keys required, making it hassle-free to use.
- Inspired by [tgpt](https://github.com/aandrew-me/tgpt/), OpynGPT utilizes a pool of users' data and the API from fakeopen.com.

Contributing
------------

If you'd like to contribute to OpynGPT, feel free to fork the repository and submit a pull request.

License
-------

This project is licensed under the GPLv3 License - check out [this website](https://www.tldrlegal.com/license/gnu-general-public-license-v3-gpl-3) for more information.

GitHub Repository
-----------------

`GitHub Repository <https://github.com/anxkhn/OpynGPT>`_
""",
    long_description_content_type='text/x-rst',
    author='Anas Khan',
)
