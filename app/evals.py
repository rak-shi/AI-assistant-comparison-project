import json

with open("evaluation/prompts.json") as f:
    prompts = json.load(f)

print(prompts)