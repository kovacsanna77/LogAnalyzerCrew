# Log Analyzer with CrewAi and GPT-4

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Facing errors](#facing-errors)
- [Features](#features)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kovacsanna77/loganalyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd project
   ```

Since the new update CrewAi does not use poetry anymore, installs dependencies when running the crew.

## Usage

    Then run the crewai, and after that we can move on to train the crew.
    ```bash
    crewai run
    ```
- If you want to train the agents then run this first: 
    - Replace the '2' if you want to train it for more iterations.
    ```bash
    crewai train -n 2
    ```
- To test the crew:
    ``` bash
    crewai test -n 2
    ```
    
## Facing errors
- The train does not run with the new O1 GPT models
- Make sure Python and every other package is up to date 
    - poetry automatically updates the packeges, so it is important to run that before moving on to running the crew

### For more information: 
- [CrewAiDocumentation](https://docs.crewai.com)
