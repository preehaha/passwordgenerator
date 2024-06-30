import random
import streamlit as st

# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

st.title("PyPassword Generator")

# User inputs
nr_letters = st.number_input("How many letters would you like in your password?", min_value=0, step=1)
nr_symbols = st.number_input("How many symbols would you like?", min_value=0, step=1)
nr_numbers = st.number_input("How many numbers would you like?", min_value=0, step=1)

level = st.radio("Choose difficulty level:", ("Easy", "Hard"))

if st.button("Generate Password"):
    if level == "Easy":
        password = ""

        for char in range(1, nr_letters + 1):
            password += random.choice(letters)

        for char in range(1, nr_symbols + 1):
            password += random.choice(symbols)

        for char in range(1, nr_numbers + 1):
            password += random.choice(numbers)

        st.write(f"Your password is: {password}")

    else:  # Hard Level
        password_list = []

        for char in range(1, nr_letters + 1):
            password_list.append(random.choice(letters))

        for char in range(1, nr_symbols + 1):
            password_list.append(random.choice(symbols))

        for char in range(1, nr_numbers + 1):
            password_list.append(random.choice(numbers))

        random.shuffle(password_list)

        password = ""
        for char in password_list:
            password += char

        st.write(f"Your password is: {password}")
