import streamlit as st
st.title("chai taste poll")

col1,col2=st.columns(2)

with col1:
    st.header("masala chai")
    st.image("https://images.pexels.com/photos/34324342/pexels-photo-34324342.jpeg?_gl=1*18iq0xt*_ga*OTA0ODA0MTg1LjE3ODIyOTcwOTc.*_ga_8JE65Q40S6*czE3ODIyOTcwOTYkbzEkZzEkdDE3ODIyOTc0NzkkajYwJGwwJGgw", width=200)
    vote1=st.button("vote masala chai")
    
with col2:
    st.header("kesar chai")
    st.image("https://images.pexels.com/photos/33430555/pexels-photo-33430555.jpeg?_gl=1*lz696y*_ga*OTA0ODA0MTg1LjE3ODIyOTcwOTc.*_ga_8JE65Q40S6*czE3ODIyOTcwOTYkbzEkZzEkdDE3ODIyOTc1NzYkajM0JGwwJGgw", width=200)
    vote2=st.button("vote kesar chai")
    
if vote1:
    st.success("thanks for voting masala chai")

if vote2:
    st.success("thanks for voting kesar chai")

name=st.sidebar.text_input("enter your name")
tea=st.sidebar.selectbox("choose your chai: ",["masala","kesar","adrak"])

st.write(f"welcome")
st.write(f"chai is getting ready")

with st.expander("show chai making instruction"):
    st.write("""
    1. biol water
    2. add milk and spices
     """)
    
st.markdown("### welcome to chai app ")
st.markdown("> blockquote")

