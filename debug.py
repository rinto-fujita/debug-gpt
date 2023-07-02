import os
import subprocess
import openai
import api_key

openai.api_key = api_key.api_key


# Content_list and activate_file is only thing you are suppposed to change
content_list = ['test.py', 'ask.py']
activate_file = "test.py"
# Content_list and activate_file is only thing you are suppposed to change



code_dict = {}
messages = [
    {"role": "system", "content": "You are an assistant that helps with Python debugging."}
]

# Folder tree structure
tree_structure = subprocess.run(['tree', '-L', '3'], capture_output=True, text=True).stdout
messages.append({"role": "assistant", "content": f'Project file structure:\n\n{tree_structure}\n\n'})

# Read file contents
def read_code(file_name):
    with open(file_name, 'r') as file:
        code = file.read()
    return code

for file_name in content_list:
    with open(file_name, 'r') as file:
        code = read_code(file_name)
        code_dict[file_name] = code

messages.append({"role": "assistant", "content": f'Content of each file:\n\n{code_dict}\n\n'})

# Get error code
try:
    result = subprocess.run(['python3', '-c', activate_file], capture_output=True, text=True, check=True)
    stdout = result.stdout
    print(stdout)
except subprocess.CalledProcessError as e:
    stderr = e.stderr

messages.append({"role": "assistant", "content": f'Error code generated by executing {activate_file}:\n\n{stderr}\n\n'})
messages.append({"role": "user", "content": 'Please provide a really short summary of why the error occurred and a possible solution.'})

chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=messages
)

response = chat_completion["choices"][0]["message"]["content"]
print(response)