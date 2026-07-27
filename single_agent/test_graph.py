from graph import graph

response = graph.invoke(
    {
        "question": "How much leave do I have?"
    }
)

print(response["answer"])
