from llm import llm

response = llm.invoke(
    "employe 1001 salary ?"
)

print(response.content)
