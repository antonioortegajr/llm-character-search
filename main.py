from prompt_llm import prompt_llama

# will hook up to marvel when their api let's me back in
# https://github.com/antonioortegajr/llm-character-search/issues/1
data = ""

#prompt for dr. doom
prompt = f"""
given the data below, is the marvel character Dr. Doom in any of these comic books?

Data: 
{{data}}
"""

result = prompt_llama("")
print(result)
# Or specify a different model:
result = prompt_llama("What is the capital of France?", model="llama3")
