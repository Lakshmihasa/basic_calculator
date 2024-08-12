import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Cannot divide by zero'
    return x / y

def power(x, y):
    return x ** y

def main():
    st.title('Simple Calculator')

    operations = {
        'Add': add,
        'Subtract': subtract,
        'Multiply': multiply,
        'Divide': divide,
        'Power': power
    }

    st.write('### Select Operation')
    operation = st.selectbox('', list(operations.keys()))

    num1 = st.number_input('Enter first number', value=0.0, step=0.1)
    num2 = st.number_input('Enter second number', value=0.0, step=0.1)

    if st.button('Calculate'):
        result = operations[operation](num1, num2)
        st.write(f'Result: **{result}**')

if __name__ == '__main__':
    main()
