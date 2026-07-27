from graph import graph

from langchain_core.messages import HumanMessage

response = graph.invoke(

    {
        "messages":[
            HumanMessage(
                content="Who is eligible for FMLA?"
            )
        ]
    }

)

for m in response["messages"]:

    print("\n-------------------------")

    print(type(m).__name__)

    print(m)
