# llm_config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

LLM_TYPE = "ollama"  # Options: 'llama_cpp', 'ollama'

# LLM settings for llama_cpp
MODEL_PATH = "/filepath/to/your/llama.cpp/model" # Replace with your llama.cpp models filepath

LLM_CONFIG_LLAMA_CPP = {
    "llm_type": "llama_cpp",
    "model_path": MODEL_PATH,
    "n_ctx": 20000,  # context size
    "n_gpu_layers": 0,  # number of layers to offload to GPU (-1 for all, 0 for none)
    "n_threads": 8,  # number of threads to use
    "temperature": 0.7,  # temperature for sampling
    "top_p": 0.9,  # top p for sampling
    "top_k": 40,  # top k for sampling
    "repeat_penalty": 1.1,  # repeat penalty
    "max_tokens": 1024,  # max tokens to generate
    "stop": ["User:", "\n\n"]  # stop sequences
}

# LLM settings for Ollama
LLM_CONFIG_OLLAMA = {
    "llm_type": "ollama",
    "base_url": "http://localhost:11434",  # default Ollama server URL
    "model_name": "gemma2:9b-instruct-q5_K_M",  # Replace with your Ollama model name
    "temperature": 0.7,
    "top_p": 0.9,
    "n_ctx": 20000,  # context size
    "stop": ["User:", "\n\n"]
}

def get_llm_config():
    """
    Returns the configuration for the LLM.
    Loads sensitive information from environment variables.
    """
    return {
        "llm_type": "custom_openai",
        
        # Load sensitive data from environment variables
        "base_url": os.getenv("LLM_BASE_URL"),
        "api_key": os.getenv("LLM_API_KEY"),
        "model_id": os.getenv("LLM_MODEL_ID"),
        
        # General LLM parameters
        "temperature": float(os.getenv("LLM_TEMPERATURE", "0.7")),
        "max_tokens": int(os.getenv("LLM_MAX_TOKENS", "1024")),
        "top_p": float(os.getenv("LLM_TOP_P", "0.9")),
        "stop": os.getenv("LLM_STOP", "").split(",") if os.getenv("LLM_STOP") else [],
        
        # Llama.cpp specific settings (if using llama_cpp)
        "model_path": "path/to/your/model.gguf",
        "n_ctx": 2048,
        "n_gpu_layers": 0,
        "n_threads": 8,
        
        # Ollama specific settings (if using ollama)
        "model_name": "your_model_name",
    }
