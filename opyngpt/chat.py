import json

import requests


def prompt(input_message):
    url = "https://https.extension.phind.com/agent/"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "",
        "Accept": "*/*",
        "Accept-Encoding": "Identity",
    }

    payload = {
        "additional_extension_context": "",
        "allow_magic_buttons": True,
        "is_vscode_extension": True,
        "message_history": [{"content": input_message, "role": "user"}],
        "requested_model": "Phind Model",
        "user_input": input_message,
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        response_content = response.content
        # Split response content into lines
        lines = response_content.decode("utf-8").split("\r\n\r\n")
        # Extract content values from each line
        content_values = []
        for line in lines:
            try:
                data = json.loads(line.split("data: ")[1])
                choices = data.get("choices", [])
                for choice in choices:
                    content = choice.get("delta", {}).get("content")
                    if content:
                        content_values.append(content)
            except IndexError:
                pass
        return "".join(content_values)
    elif response.status_code == 401 or response.status_code == 429:
        print(f"Error: {response.status_code}, Trying again.")
        response = prompt(input_message)
    else:
        return f"Error: {response.status_code}, {response.text}"
