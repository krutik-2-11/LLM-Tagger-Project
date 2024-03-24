import replicate
from getpass import getpass
import os


# get a token: https://replicate.com/account/api-tokens
REPLICATE_API_TOKEN = "r8_I2em6xyX8PUXr1RILjH8pd9psm5HkSo2PyDMN"
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN


#input file
file_path = 'llm_part2_input_json.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    prompt_content = file.read()

#input system prompt
file_path = 'llm_part2_input_prompt.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    system_prompt_content = file.read()


# The meta/llama-2-70b-chat model can stream output as it's running.
with open('llm_part2_output.txt', 'w', encoding='utf-8') as file:
    for event in replicate.stream(
        "meta/llama-2-70b-chat",
        input={
            "prompt": prompt_content,
            "system_prompt": system_prompt_content,
            "max_new_tokens": 2000
        },
    ):
        
        file.write(str(event) + "")  
