import unittest
from unittest.mock import MagicMock, patch
from main import research_agent, chart_generator_agent, router, GraphState
from langchain_core.messages import HumanMessage, ToolMessage

class TestResearchAgent(unittest.TestCase):
    @patch('main.TavilySearch')
    def test_research_agent_success(self, MockTavilySearch):
        # Arrange
        mock_tavily = MockTavilySearch.return_value
        mock_tavily.invoke.return_value = "Mocked search results"

        initial_state = GraphState(messages=[HumanMessage(content="What are the latest trends in AI?")])

        # Act
        result_state = research_agent(initial_state)

        # Assert
        self.assertIsInstance(result_state, dict)
        self.assertIn("messages", result_state)
        
        messages = result_state["messages"]
        self.assertEqual(len(messages), 2)
        
        self.assertIsInstance(messages[0], HumanMessage)
        self.assertEqual(messages[0].content, "What are the latest trends in AI?")
        
        self.assertIsInstance(messages[1], ToolMessage)
        self.assertEqual(messages[1].content, "Mocked search results")
        self.assertEqual(messages[1].tool_call_id, "tavily_search_results_json")

class TestChartGeneratorAgent(unittest.TestCase):
    def test_chart_generator_agent(self):
        # Arrange
        initial_state = GraphState(messages=[
            HumanMessage(content="What are the latest trends in AI?"),
            ToolMessage(content="Some research data", tool_call_id="123")
        ])

        # Act
        result_state = chart_generator_agent(initial_state)

        # Assert
        self.assertIsInstance(result_state, dict)
        self.assertIn("messages", result_state)
        
        messages = result_state["messages"]
        self.assertEqual(len(messages), 3)
        self.assertIsInstance(messages[2], HumanMessage)
        self.assertEqual(messages[2].content, "Chart generated based on the research data.")

class TestRouter(unittest.TestCase):
    def test_router_to_chart_generator(self):
        # Arrange
        state = GraphState(messages=[
            HumanMessage(content="Initial query"),
            ToolMessage(content="Research results", tool_call_id="123")
        ])

        # Act
        result = router(state)

        # Assert
        self.assertEqual(result, "chart_generator_agent")

    def test_router_to_end(self):
        # Arrange
        state = GraphState(messages=[
            HumanMessage(content="Initial query"),
            ToolMessage(content="Research results", tool_call_id="123"),
            HumanMessage(content="Chart generated based on the research data.")
        ])

        # Act
        result = router(state)

        # Assert
        self.assertEqual(result, "end")

class TestIntegration(unittest.TestCase):
    @patch('main.TavilySearch')
    def test_full_graph_workflow(self, MockTavilySearch):
        # Arrange
        from main import app 

        mock_tavily = MockTavilySearch.return_value
        mock_tavily.invoke.return_value = "[{'url': 'http://test.com', 'content': 'Test content'}]"

        inputs = {"messages": [HumanMessage(content="What are the latest trends in AI?")]}

        # Act
        final_state = app.invoke(inputs)

        # Assert
        self.assertIn("messages", final_state)
        messages = final_state["messages"]
        
        self.assertEqual(len(messages), 3)
        self.assertIsInstance(messages[0], HumanMessage)
        self.assertEqual(messages[0].content, "What are the latest trends in AI?")
        
        self.assertIsInstance(messages[1], ToolMessage)
        self.assertEqual(messages[1].content, "[{'url': 'http://test.com', 'content': 'Test content'}]")
        
        self.assertIsInstance(messages[2], HumanMessage)
        self.assertEqual(messages[2].content, "Chart generated based on the research data.")

if __name__ == '__main__':
    unittest.main()
