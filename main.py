from prompt_llm import prompt_llama

result = prompt_llama("What is the capital of France?")
print(result)
# Or specify a different model:
result = prompt_llama("What is the capital of France?", model="llama3")
