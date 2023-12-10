import requests
import json
from json import JSONDecodeError


def get_user_input():
    return input("Enter your input message: ")


def prompt(input_message):
    url = "https://ai.fakeopen.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer pk-this-is-a-real-free-pool-token-for-everyone",
        "Origin": "https://chat.geekgpt.org",
        "Referrer": "https://chat.geekgpt.org/"
    }
    payload = {
        "frequency_penalty": 0,
        "messages": [
            {
                "content": input_message,
                "role": "user"
            }
        ],
        "model": "gpt-3.5-turbo",
        "presence_penalty": 0,
        "stream": True,
        "temperature": 1,
        "top_p": 1
    }
    payload_json = json.dumps(payload)
    response = requests.post(url, headers=headers,
                             data=payload_json, stream=True)
    return response


def extract_content(line):
    line_str = line.decode('utf-8')

    if "data:" not in line_str:
        return None

    json_str = line_str.split("data: ")[1]

    try:
        data_dict = json.loads(json_str)
        content = data_dict['choices'][0]['delta'].get('content', None)
        return content
    except JSONDecodeError as e:
        pass

    return None


def main():
    prmopt_message = get_user_input()
    response = prompt(prmopt_message)

    if response.status_code == 200:
        for line in response.iter_lines():
            content = extract_content(line)
            if content is not None:
                print(content, end="")
    elif response.status_code == 401 or response.status_code == 429:
        print(f"Error: {response.status_code}, Trying again.")
        response = prompt(input_message)
    else:
        print(f"Error: {response.status_code}, {response.text}")


if __name__ == "__main__":
    main()

# github.com/anxkhn/FreeGPTpy
