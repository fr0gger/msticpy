import streamlit as st
import pandas as pd

from pathlib import Path

def main() -> None:
    st.title("🤖 MSTICPy AI Ally")

    with st.expander("Expand to Read more about the Project"):
        st.write(Path("README.md").read_text())

    st.subheader("Reach out to Project team via Github")
    st.subheader("Github: https://github.com/fr0gger/msticpy")

    st.write(
        "If you would like to submit feature requests, open a issue on Github"
    )


if __name__ == "__main__":
    main()