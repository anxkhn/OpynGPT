import json
import requests


def get_user_input():
    return input("Enter your input message: ")


def prompt(user_input):
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
        "message_history": [{"content": user_input, "role": "user"}],
        "requested_model": "Phind Model",
        "user_input": user_input,
    }

    response = requests.post(url, json=payload, headers=headers)
    return response


def extract_content(response):
    # Split response content into lines
    response_content = response.content
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
    return content_values


def main():
    prmopt_message = get_user_input()
    response = prompt(prmopt_message)

    if response.status_code == 200:
        content = extract_content(response)
        for i in content:
            print(i, end="")
    elif response.status_code == 401 or response.status_code == 429:
        print(f"Error: {response.status_code}, Trying again.")
        response = prompt(prmopt_message)
    else:
        print(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    main()

# github.com/anxkhn/OpynGPT
