from typing_extensions import TypeDict


class State(TypeDict):
    """
    A dictionary that represents the state of an agent.
    message: The message that the agent is currently processing.
    next_agent: The name of the next agent that will process the message.
    retrived_docs: A list of documents that have been retrieved by the agent.
    tool_results: A dictionary of results from any tools that the agent has used.
    validation_status: A boolean indicating whether the message has been validated.
    hitl_approved: A boolean indicating whether the message has been approved by a human in the loop.
    """

    message: list
    next_agent: str
    retrived_docs: list
    tool_results: dict
    validation_status: bool
    hitl_approved: bool


