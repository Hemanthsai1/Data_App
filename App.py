import streamlit as st
#st.title(":blue[hi]")
st.title(":blue[Innomatics] Data App")
st.subheader("Feb-2023")
st.caption(':green[On Progress...]')
st.snow()

btn_click = st.button("Just Click Me!")

if btn_click == True:
    st.subheader("You clicked me :smile:")
    st.balloons()