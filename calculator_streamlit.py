import streamlit as st
from binary_calculator import BaseTwoBinary

st.title('Binary:Decimal - Base 2')

option = st.selectbox(
    "What type of value would you like to convert?",
    ("Binary", "Decimal")
    )

y = st.text_input(
    "Enter the value you want to convert",
)

result = "Please enter a valid value."

if y:  # Check if input is not empty
    try:
        if option == 'Decimal':
            y = int(y)  # Ensure input is an integer
            result = BaseTwoBinary.full_binary_calculator('dec', y)
        elif option == 'Binary':
            y = str(y)  # Ensure input is treated as a string
            result = BaseTwoBinary.full_binary_calculator('bin', y)
    except ValueError:
        result = "Please enter a valid input."   

# Write the results out
st.write(result)