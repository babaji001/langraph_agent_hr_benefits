import streamlit as st

from langchain_core.messages import HumanMessage

from graph import graph


st.set_page_config(
    page_title="Enterprise HR AI Assistant",
    page_icon="🤖",
    layout="wide"
)


####################################################
# Session State
####################################################

if "messages" not in st.session_state:
    st.session_state.messages = []

if "emp_id" not in st.session_state:
    st.session_state.emp_id = "1001"


####################################################
# Sidebar
####################################################

with st.sidebar:

    st.title("Enterprise HR AI")

    st.session_state.emp_id = st.text_input(
        "Employee ID",
        value=st.session_state.emp_id
    )

    st.markdown("---")

    st.subheader("Sample Questions")

    st.markdown("""
- Who is my manager?
- Show my profile
- Show my PTO balance
- Show my leave history
- Show my salary
- Show my benefits
- Show my latest medical claim
- Show my dependents
- Explain FMLA
- Explain LTD
- Explain COBRA
- What medical plans are available?
- What is Open Enrollment?
- I'm resigning next month
- I'm having a baby
""")

    if st.button("Clear Conversation"):

        st.session_state.messages = []

        st.rerun()


####################################################
# Header
####################################################

st.title("🤖 Enterprise HR AI Assistant")

st.caption("Powered by LangGraph + Ollama + FastAPI + SQLite + ChromaDB")


####################################################
# Chat History
####################################################

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])


####################################################
# User Input
####################################################

question = st.chat_input("Ask an HR question...")


####################################################
# Process Question
####################################################

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # Append employee id to help the LLM.
            # Later we'll replace this with memory.
            prompt = f"""
Employee ID: {st.session_state.emp_id}

User Question:
{question}
"""

            response = graph.invoke(

                {

                    "messages":[

                        HumanMessage(
                            content=prompt
                        )

                    ]

                }

            )

            answer = response["messages"][-1].content

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
