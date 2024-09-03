import pet_chain as pc
import streamlit as st
st.title("Pets name generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat","Cow","Hamster","Dog"))

if animal_type == "Cat":
    animal_color = st.sidebar.text_area("What Color is your Cat?", max_chars= 15 )

if animal_type == "Cow":
    animal_color = st.sidebar.text_area("What Color is your Cow?", max_chars=15)
if animal_type == "Hamster":
    animal_color = st.sidebar.text_area("What Color is your Hamster?", max_chars=15)
if animal_type == "Dog":
    animal_color = st.sidebar.text_area("What Color is your Dog?", max_chars=15)
if animal_color:
    response = pc.generate_pet_name(animal_type,animal_color)

    st.text(response)