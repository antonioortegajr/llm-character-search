import requests
import json

def prompt_llama(prompt: str, model: str = "llama3") -> str:
    """
    Send a prompt to Ollama and get the response.
    
    Args:
        prompt (str): The input prompt to send to the model
        model (str): Name of the Ollama model to use (default: llama3)
        
    Returns:
        str: The model's response
    """
    try:
        # Ollama API endpoint
        url = "http://localhost:11434/api/generate"
        
        # Prepare the request payload
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        
        # Send request to Ollama
        llm_response = requests.post(url, json=payload)
        llm_response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse and return the response
        result = llm_response.json()
        return result["response"]
    
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Ollama: {str(e)}"
    except (KeyError, json.JSONDecodeError) as e:
        return f"Error processing response: {str(e)}"