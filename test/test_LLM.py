import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

from src.agent.model_factory import get_llm

load_dotenv(override=True)
provider = os.getenv("PROVIDER")
model_to_use = get_llm (provider)
messages = [HumanMessage(content="What is the results of 12*12?, just return the numerical answer without anything more.")]

# Pass messages directly as the input argument
response = model_to_use.invoke(messages)

print(response.content)
print("Test works well!")
