
# app.py

import streamlit as st

from graph import graph


st.set_page_config(

    page_title="HR AI Assistant",

    layout="wide"

)


st.title(
    "Enterprise HR AI Assistant"
)



if "session_id" not in st.session_state:

    st.session_state.session_id = "default"



employee_id = st.text_input(

    "Employee ID",

    value="1001"

)



question = st.text_area(

    "Ask HR Assistant"

)



if st.button("Submit"):


    if question:


        state = {

            "employee_id":

                employee_id,


            "session_id":

                st.session_state.session_id,


            "question":

                question

        }



        result = graph.invoke(

            state

        )



        st.subheader(

            "Response"

        )


        response = result.get(

            "response",

            {}

        )


        st.json(

            response

        )
