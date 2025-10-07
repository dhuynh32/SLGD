from typing import List, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, ToolMessage
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
from langgraph.graph import StateGraph

load_dotenv()

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        messages: A list of messages that are passed between nodes.
    """
    messages: List[BaseMessage]

def research_agent(state: GraphState):
    """
    A research agent that uses Tavily Search to find information.

    Args:
        state: The current graph state.

    Returns:
        The updated state with the research findings.
    """
    messages = state["messages"]
    last_message = messages[-1]

    # Initialize the tool
    tool = TavilySearch(max_results=2)
    # Invoke the tool with the last message content
    response = tool.invoke(last_message.content)
    # Create a new message with the response
    new_message = ToolMessage(
        content=response,
        tool_call_id="tavily_search_results_json"  # A unique ID for the tool call
    )
    # Append the new message to the state
    messages.append(new_message)
    return {"messages": messages}

def chart_generator_agent(state: GraphState):
    """
    A chart generator agent that creates a chart based on the research findings.

    Args:
        state: The current graph state.

    Returns:
        The updated state with a message indicating the chart has been generated.
    """
    messages = state["messages"]
    last_message = messages[-1]

    # For this simple example, we'll just create a confirmation message.
    # In a real-world scenario, this agent would generate a chart.
    new_message = HumanMessage(content="Chart generated based on the research data.")
    messages.append(new_message)
    return {"messages": messages}

def router(state: GraphState):
    """
    A router that decides which agent to call next.

    Args:
        state: The current graph state.

    Returns:
        A string indicating the next agent to call.
    """
    messages = state["messages"]
    last_message = messages[-1]
    # If the last message is from the research agent, call the chart generator
    if isinstance(last_message, ToolMessage):
        return "chart_generator_agent"
    else:
        return "end"

# Create the graph
workflow = StateGraph(GraphState)

# Add the nodes
workflow.add_node("research_agent", research_agent)
workflow.add_node("chart_generator_agent", chart_generator_agent)

# Set the entry point
workflow.set_entry_point("research_agent")

# Add the edges
workflow.add_conditional_edges(
    "research_agent",
    router,
    {
        "chart_generator_agent": "chart_generator_agent",
        "__end__": "__end__"
    }
)
workflow.add_edge("chart_generator_agent", "__end__")

# Compile the graph
app = workflow.compile()

if __name__ == '__main__':
    # Define the initial input
    initial_input = {"messages": [HumanMessage(content="What are the latest trends in AI?")]}

    # Stream the graph
    for output in app.stream(initial_input):
        # The output is a dictionary with the agent name as the key
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print("---")
            print(value)
        print("\n---\n")
