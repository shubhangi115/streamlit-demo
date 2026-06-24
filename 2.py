import streamlit as st

st.title("Chai maker app")

if st.button("make chai"):
    st.success("you chair is being brewed")

add_masala=st.checkbox("add masala")

if add_masala:
    st.write("masala added")
else:
    st.write("oops")

tea_type=st.radio("pick your chai base: ",["milk","water","almond milk"])
st.write(f"selected {tea_type}")

flavour=st.selectbox("choose flavour: ", ["Adrak","kesar","tulsi"])
st.write(f"selected {flavour}")

sugar=st.slider("sugar leve",0,5,2)
st.write(f"selected {sugar}")

cups=st.number_input("how many cups",min_value=1,max_value=10,step=1)
st.write(f"selected sugar level {cups}")

name=st.text_input("enter your name")
if name:
    st.write(f"wlecome, {name}")

dob=st.date_input("select your date of birth")
st.write(f"date of birth {dob}")