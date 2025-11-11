from google.adk.agents.llm_agent import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents import SequentialAgent

#Define sub agents for Each Pipeline Stages

#Code writer agent -- 1
code_writer_agent = LlmAgent(
    name="CodeWriterAgent",
    model="gemini-2.5-flash",
    #Add Instructions for the Agent
    instruction="""You are a Python Code Generator.
Based *only* on the user's request, write Python code that fulfills the requirement.
Output *only* the complete Python code block, enclosed in triple backticks (```python ... ```). 
Do not add any other text before or after the code block.
""",
description="Writes initial python code based on a specification.",
output_key="generated_code" #Stores output in a State
)

#Code Reviewer Agent -- 2
code_reviewer_agent = LlmAgent(
    name="CodeReviewerAgent",
    model="gemini-2.5-flash",
    #Add Instructions for the Agent
    instruction="""You are an expert Python Code Reviewer. 
    Your task is to provide constructive feedback on the provided code.

    **Code to Review:**
    ```python
    {generated_code}
    ```

**Review Criteria:**
1.  **Correctness:** Does the code work as intended? Are there logic errors?
2.  **Readability:** Is the code clear and easy to understand? Follows PEP 8 style guidelines?
3.  **Efficiency:** Is the code reasonably efficient? Any obvious performance bottlenecks?
4.  **Edge Cases:** Does the code handle potential edge cases or invalid inputs gracefully?
5.  **Best Practices:** Does the code follow common Python best practices?

**Output:**
Provide your feedback as a concise, bulleted list. Focus on the most important points for improvement.
If the code is excellent and requires no changes, simply state: "No major issues found."
Output *only* the review comments or the "No major issues" statement.
""",
description="Reviews code and provides feedback.",
output_key="review_comments" #Stores review in a state
)

#Code Refactorer Agent -- 3
code_refactorer_agent=LlmAgent(
    name="CodeRefactorerAgent",
    model="gemini-2.5-flash",
    instruction="""You are a Python Code Refactoring AI.
Your goal is to improve the given Python code based on the provided review comments.

  **Original Code:**
  ```python
  {generated_code}
  ```

  **Review Comments:**
  {review_comments}

**Task:**
Carefully apply the suggestions from the review comments to refactor the original code.
If the review comments state "No major issues found," return the original code unchanged.
Ensure the final code is complete, functional, and includes necessary imports and docstrings.

**Output:**
Output *only* the final, refactored Python code block, enclosed in triple backticks (```python ... ```). 
Do not add any other text before or after the code block.
""",
description="Refactors code based on review comments.",
output_key="refactored_code" #Stores refactored code in a state
)

#Cerate a Sequential Agent to chain the sub agents -- 4
code_pipeline_Agent = SequentialAgent(
    name="CodePipelineAgent",
    sub_agents=[code_writer_agent, code_reviewer_agent, code_refactorer_agent],
    description="Executes a sequence of code writing, reviewing, and refactoring."
)

root_agent = code_pipeline_Agent