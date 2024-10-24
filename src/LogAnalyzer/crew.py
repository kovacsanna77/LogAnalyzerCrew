from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

# Uncomment the following line to use an example of a custom tool
from LogAnalyzer.tools.readcsv import ReadCsvTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperD evTool

@CrewBase
class LogAnalyzerCrew():
	"""Loganalyzer crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	
 
	def __init__(self) -> None:
		"""Define the LLM model used by the crew"""
		self.gpt_llm = ChatOpenAI( 
                    model="gpt-4o", #o1-perview és o1-mini modellekkel nem fut le a train :)))))))))
                    temperature=0, #ha o1 modellek, akkor az alap temperature = 1
    				max_tokens=None,
    				timeout=None)
	
	@agent
	def loader(self) ->Agent:   
		return Agent(
			config = self.agents_config['loader'],
			tools=[ReadCsvTool()],
			llm= self.gpt_llm,
   			verbose = True,
			allow_delegation=False
		)
	@agent
	def analyzer(self) -> Agent:
		return Agent(
			config=self.agents_config['analyzer'],
			llm = self.gpt_llm,
			verbose = True,
   			allow_delegation=False
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			llm = self.gpt_llm,
			verbose = True,
   			allow_delegation=False
		)

	@task
	def load_task(self) -> Task:
		return Task(
			config=self.tasks_config['load_task'],
   
		)
	@task
	def analyzer_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyzer_task'],
		)
  
	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
   			output_file= "report.md"
		)



	@crew
	def crew(self) -> Crew:
		"""Creates the Loganalyzer crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			
		)