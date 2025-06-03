from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task
from hitl_example.models import PersonalInformationOutput
from hitl_example.tools.human_tool import HumanInputContextTool

@CrewBase
class HitlExample():
    """HitlExample crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def information_collector(self) -> Agent:
        human_tool = HumanInputContextTool()
        return Agent(
            config=self.agents_config['information_collector'],
            tools=[human_tool],
            verbose=True
        )

    @agent
    def information_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['information_summarizer'],
            verbose=True
        )

    @task
    def collector_task(self) -> Task:
        personal_information = PersonalInformationOutput
        return Task(
            config=self.tasks_config['collector_task'], # type: ignore[index]
            output_json=personal_information,
            context_prompt="Before asking for personal information, check if you already have this information in your memory. If you already have complete information about the person (first_name, last_name, country, city, company, and email), acknowledge that you remember them and continue with the conversation without asking for these details again. Only collect missing information if some fields are empty or unknown."
        )

    @task
    def summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarizer_task'],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the HitlExample crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True,  # Enable memory capabilities
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
