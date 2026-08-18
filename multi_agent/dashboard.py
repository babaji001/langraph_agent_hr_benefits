import streamlit as st

from metrics import metrics
from audit_logger import audit_logger
from feedback_service import feedback_service
from notification_service import notification_service

st.set_page_config(

    page_title="Enterprise AI Dashboard",

    layout="wide"

)

st.title("Enterprise AI Operations Dashboard")

###############################################################

summary = metrics.summary()

###############################################################

c1,c2,c3,c4 = st.columns(4)

c1.metric(

    "Requests",

    summary["Total Requests"]

)

c2.metric(

    "Avg Latency",

    f'{summary["Average Latency"]:.2f} sec'

)

c3.metric(

    "LLM Calls",

    summary["LLM Calls"]

)

c4.metric(

    "HR Escalations",

    summary["HR Escalations"]

)

###############################################################

st.divider()

###############################################################

left,right = st.columns(2)

###############################################################

with left:

    st.subheader("Agent Usage")

    st.bar_chart(

        summary["Agent Usage"]

    )

###############################################################

with right:

    st.subheader("Tool Usage")

    st.bar_chart(

        summary["Tool Usage"]

    )

###############################################################

st.divider()

###############################################################

st.subheader("Recent Audit Logs")

logs = audit_logger.history()

st.dataframe(

    logs,

    use_container_width=True

)

###############################################################

st.divider()

###############################################################

st.subheader("Pending Notifications")

notifications = notification_service.pending_notifications()

st.dataframe(

    notifications,

    use_container_width=True

)

###############################################################

st.divider()

###############################################################

st.subheader("Negative Feedback")

feedback = feedback_service.low_ratings()

st.dataframe(

    feedback,

    use_container_width=True

)
