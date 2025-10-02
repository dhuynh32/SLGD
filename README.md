# Hello, Multi-Agent Routing with LangGraph

This project demonstrates a simple multi-agent workflow using LangGraph. The application consists of two agents: a research agent that fetches information from the web and a chart generator agent that (conceptually) creates a chart based on the research. A router directs the flow of information between the agents.

## Agent Workflow

1.  **Research Agent**: The workflow starts with the research agent. It takes an initial query (e.g., "What are the latest trends in AI?") and uses the Tavily search tool to find relevant information.
2.  **Router**: The output of the research agent is passed to the router. The router decides which agent to call next based on the content of the message.
3.  **Chart Generator Agent**: If the last message is from the research agent, the router calls the chart generator agent. This agent creates a confirmation message that a chart has been generated.
4.  **End**: The workflow ends after the chart generator agent has finished.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/learnlanggraph.git
    cd learnlanggraph
    ```

2.  Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4.  Create a `.env` file in the root of the project and add your API keys:
    ```
    GOOGLE_API_KEY="your-google-api-key"
    TAVILY_API_KEY="your-tavily-api-key"
    ```

## Usage

To run the application, execute the `main.py` script:

```bash
python main.py
```

## Sample Output

```
---RESEARCH AGENT---
---ROUTER---
Output from node 'research_agent':
---
{'messages': [HumanMessage(content='What are the latest trends in AI?'), HumanMessage(content='[{\'url\': \'https://www.forbes.com/sites/forbestechcouncil/2024/05/20/the-future-of-ai-top-trends-to-watch-in-2024-and-beyond/\', \'content\': "The AI landscape is in constant flux, with new trends emerging at a breakneck pace. As we look ahead, several key developments are poised to reshape industries and redefine our relationship with technology. Here are some of the most significant AI trends to watch in 2024 and beyond:  1. Generative AI Will Continue To Dominate And Diversify  Generative AI has captured the public imagination with its ability to create novel content, from text and images to music and code. This trend is set to continue, with models becoming more sophisticated and capable of producing even more realistic and contextually relevant outputs. We can expect to see generative AI integrated into a wider range of applications, from automated content creation and personalized marketing to drug discovery and engineering design. As these models become more powerful, however, ethical considerations around issues like deepfakes, intellectual property and bias will become even more critical.  2. Multimodal AI Will Bridge The Gap Between Different Data Types  While early AI models primarily focused on a single data modality, such as text or images, the future lies in multimodal AI. These systems can understand and process information from multiple sources simultaneously, such as combining text, images and audio to gain a more holistic understanding of the world. This will enable more natural and intuitive human-computer interactions, as well as unlock new possibilities in areas like robotics, autonomous vehicles and immersive experiences.  3. Explainable AI (XAI) Will Become A Necessity  As AI systems become more complex and autonomous, the need for transparency and accountability becomes paramount. Explainable AI (XAI) aims to address this by providing clear and understandable explanations for how AI models arrive at their decisions. This is not only crucial for building trust and ensuring fairness but also for debugging and improving AI systems. In regulated industries like healthcare and finance, XAI will likely become a legal and ethical requirement.  4. AI-Powered Cybersecurity Will Be A Double-Edged Sword"}, {\'url\': \'https://www.linkedin.com/pulse/9-biggest-ai-trends-everyone-should-watching-2024-bernard-marr-v78re\', \'content\': "Trend 1: Generative AI  Generative AI is the undisputed heavyweight champion of AI trends right now. Thanks to the runaway success of large language models (LLMs) like GPT-4, Claude, and Gemini, we now have AI that can create text, images, and other media in response to prompts. And it’s only going to get bigger and better in 2024.  Trend 2: Smart and Multimodal AI  In 2024, we’ll see AI get even smarter. It will also become multimodal, meaning it can understand different types of information, like text, speech, images, and video, and find connections between them.  Trend 3: AI-Generated Content Takes Over  The internet is already flooded with AI-generated content, and this trend will continue in 2024. We’ll see more AI-generated text, images, videos, and audio, which will have a major impact on industries like marketing, entertainment, and education.  Trend 4: The Democratization of AI  AI is no longer just for tech giants. Thanks to open-source models and low-code/no-code platforms, AI is becoming more accessible to everyone. This means we’ll see more small businesses and individuals using AI to create innovative products and services.  Trend 5: AI Regulation  With the increasing power of AI, there’s a growing need for regulation. In 2024, we’ll see more governments and organizations developing guidelines and laws to ensure that AI is used responsibly and ethically."}]')]}

---

---CHART GENERATOR---
Output from node 'chart_generator_agent':
---
{'messages': [HumanMessage(content='What are the latest trends in AI?'), HumanMessage(content='[{\'url\': \'https://www.forbes.com/sites/forbestechcouncil/2024/05/20/the-future-of-ai-top-trends-to-watch-in-2024-and-beyond/\', \'content\': "The AI landscape is in constant flux, with new trends emerging at a breakneck pace. As we look ahead, several key developments are poised to reshape industries and redefine our relationship with technology. Here are some of the most significant AI trends to watch in 2024 and beyond:  1. Generative AI Will Continue To Dominate And Diversify  Generative AI has captured the public imagination with its ability to create novel content, from text and images to music and code. This trend is set to continue, with models becoming more sophisticated and capable of producing even more realistic and contextually relevant outputs. We can expect to see generative AI integrated into a wider range of applications, from automated content creation and personalized marketing to drug discovery and engineering design. As these models become more powerful, however, ethical considerations around issues like deepfakes, intellectual property and bias will become even more critical.  2. Multimodal AI Will Bridge The Gap Between Different Data Types  While early AI models primarily focused on a single data modality, such as text or images, the future lies in multimodal AI. These systems can understand and process information from multiple sources simultaneously, such as combining text, images and audio to gain a more holistic understanding of the world. This will enable more natural and intuitive human-computer interactions, as well as unlock new possibilities in areas like robotics, autonomous vehicles and immersive experiences.  3. Explainable AI (XAI) Will Become A Necessity  As AI systems become more complex and autonomous, the need for transparency and accountability becomes paramount. Explainable AI (XAI) aims to address this by providing clear and understandable explanations for how AI models arrive at their decisions. This is not only crucial for building trust and ensuring fairness but also for debugging and improving AI systems. In regulated industries like healthcare and finance, XAI will likely become a legal and ethical requirement.  4. AI-Powered Cybersecurity Will Be A Double-Edged Sword"}, {\'url\': \'https://www.linkedin.com/pulse/9-biggest-ai-trends-everyone-should-watching-2024-bernard-marr-v78re\', \'content\': "Trend 1: Generative AI  Generative AI is the undisputed heavyweight champion of AI trends right now. Thanks to the runaway success of large language models (LLMs) like GPT-4, Claude, and Gemini, we now have AI that can create text, images, and other media in response to prompts. And it’s only going to get bigger and better in 2024.  Trend 2: Smart and Multimodal AI  In 2024, we’ll see AI get even smarter. It will also become multimodal, meaning it can understand different types of information, like text, speech, images, and video, and find connections between them.  Trend 3: AI-Generated Content Takes Over  The internet is already flooded with AI-generated content, and this trend will continue in 2024. We’ll see more AI-generated text, images, videos, and audio, which will have a major impact on industries like marketing, entertainment, and education.  Trend 4: The Democratization of AI  AI is no longer just for tech giants. Thanks to open-source models and low-code/no-code platforms, AI is becoming more accessible to everyone. This means we’ll see more small businesses and individuals using AI to create innovative products and services.  Trend 5: AI Regulation  With the increasing power of AI, there’s a growing need for regulation. In 2024, we’ll see more governments and organizations developing guidelines and laws to ensure that AI is used responsibly and ethically."}]'), HumanMessage(content='Chart generated based on the research data.')]}

---
```
