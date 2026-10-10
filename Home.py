import streamlit as st

# ---------------------------------------------------------------------------
# Home.py — the main entry point of this multipage Streamlit app.
# Every .py file placed inside the "pages/" folder is added to the sidebar
# navigation automatically, so app.py shows up there as a second page.
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="World Cities Data App",
    page_icon="🌍",
    layout="wide",
)

st.title("World Cities Data App")

st.write(
    """
    Welcome! This app explores the **world cities** dataset, which contains
    every city in the world with a population of more than one million.

    On the next page you can:

    - filter cities by a minimum population,
    - choose which capital types to display,
    - look up a single country by name,
    - and view the results on an interactive map, a data table and a bar chart.
    """
)

st.divider()

# A button that takes the user to pages/app.py
if st.button("Open the World Cities app", type="primary"):
    st.switch_page("pages/app.py")
