import streamlit as st


st.title("Basic Calculator")


num1 = st.number_input("Enter the first number:", format="%f")
num2 = st.number_input("Enter the second number:", format="%f")


operation = st.selectbox("Choose an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

if st.button("Calculate"):
    try:

        if operation == "Addition":
            result = num1 +num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
    
        st.success(f"The result of {operation} is: {result}")
    except ZeroDivisionError as e:
        st.error(e)
