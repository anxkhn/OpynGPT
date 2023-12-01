import json
import requests
from json import JSONDecodeError


def prompt(input_message):
    url = "https://ai.fakeopen.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer pk-this-is-a-real-free-pool-token-for-everyone"
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

    if response.status_code == 200:
        for line in response.iter_lines():
            line_str = line.decode('utf-8')
            if "data:" not in line_str:
                continue

            json_str = line_str.split("data: ")[1]

            try:
                data_dict = json.loads(json_str)
                content = data_dict['choices'][0]['delta'].get('content', None)
                if content is not None:
                    return content
            except JSONDecodeError as e:
                pass
    elif response.status_code == 401:
        print(f"Error: {response.status_code}, Trying again")
        return prompt(input_message)
    else:
        return (f"Error: {response.status_code}, {response.text}")
