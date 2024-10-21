from crewai_tools import BaseTool
from langchain_community.document_loaders.csv_loader import CSVLoader

class ReadCsvTool(BaseTool):
    name: str = "ReadCsvTool"
    description: str = (
        "This tool is used to load CSV files in a format that the data can be used by agents and tasks to analyze it"
    )

    def _run(self, input_file: str) -> str: 
        loader = CSVLoader(file_path=input_file)
        data = loader.load()
        return data
