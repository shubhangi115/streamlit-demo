import streamlit as st

st.title("Hello")
st.subheader("made with streamlit")
st.text("welcome")
st.write("choose you fav chai")

chai=st.selectbox("Your favourite chai:", {"masala chai", "lemon tea","adrak chai"})
st.write(f"you choose {chai}, excellent choice")

st.success("your chai has been brewed")