import os
from crewai import Agent, Task, Crew, Process

os.environ['OPENAI_API_KEY'] = ""

#Define agents with roles and goals
researcher = Agent(
    role = 'Researcher',
    goal='Discover new technologies',
    backstory='I am a researcher who is passionate about discovering new technologies.',
    verbose=True,
    allow_delegation=True
)

writer = Agent(
    role='Writer',
    goal='Write a research paper',
    backstory='I am a writer who is passionate about writing research papers.',
    verbose=True,
    allow_delegation=False
)

# Create tasks for agents
research_task = Task(
    name='Research new technologies',
    description='Research new technologies in the field of AI',
    agent=researcher,
    verbose=True
)

write_task = Task(
    name='Write a research paper',
    description='Write a research paper on new technologies in the field of AI',
    agent=writer,
    verbose=True
)

# Instantiate your crew with a sequential process
crew = Crew(
    name='AI Research Crew',
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()