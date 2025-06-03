# CrewAI Memory Example

This project demonstrates how to implement memory capabilities in a CrewAI agent system to remember personal information across conversations.

## Features

- Agent that collects personal information from users
- Memory persistence across conversations
- Only asks for personal data the first time
- Summarizes user information in natural language

## Project Structure

- `src/hitl_example/crew.py`: Main implementation of the CrewAI agents and tasks
- `src/hitl_example/models/crew_models.py`: Pydantic models for data structure
- `src/hitl_example/tools/human_tool.py`: Tool for human-in-the-loop interaction
- `src/hitl_example/config/`: YAML configuration files for agents and tasks

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/crewai-memory-example.git
   cd crewai-memory-example
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   Create a `.env` file in the root directory with your OpenAI API key:
   ```
   MODEL=gpt-4o-mini
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

Run the example:

```
chainlit run ./src/hitl_example/main.py
```