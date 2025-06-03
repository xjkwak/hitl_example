#!/usr/bin/env python
import asyncio
import sys
import warnings
from datetime import datetime

import chainlit as cl
from dotenv import load_dotenv

from hitl_example.crew import HitlExample
from hitl_example.models import CrewInput

load_dotenv(override=True)

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        HitlExample().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        HitlExample().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        HitlExample().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        HitlExample().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

my_crew = HitlExample().crew()
if __name__ == "__main__":
    try:
        input_data = CrewInput(initial_message="Hi I am Cristian")
        result = my_crew.kickoff(inputs=input_data.model_dump())
        print(result)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="Hello I am your personal Assistant. How can I help?").send()


@cl.on_message
async def on_message(message: cl.Message):
    # This function will be called when user sends their first and subsequent messages
    input_data = CrewInput(initial_message=message.content)
    result = await asyncio.to_thread(lambda: my_crew.kickoff(inputs=input_data.model_dump()))

    await cl.Message(content=str(result)).send()