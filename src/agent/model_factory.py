import os

from dotenv import load_dotenv
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_ollama import ChatOllama

load_dotenv(override = True)
provider = os.getenv("PROVIDER")
print(f"provider is {provider}")

def get_llm(provider: str = None) -> BaseChatModel:
    """

    This function provides the possibility to switch between different LLM 
    provider like, ollama, open_ai, ...

    """
    model_name = os.getenv("LLM_MODEL")

    if provider == "Ollama":
        try :
            return ChatOllama(model= model_name ,  
                              base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
                              temperature=0.2)
        except Exception as e:
            raise ValueError(f"Failed to initialize Ollama: {e}")
        raise ValueError(f"Unsupported or missing LLM provider: '{provider}'")
        