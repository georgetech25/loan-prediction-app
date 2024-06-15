import streamlit as st





st.title('Loan Application Prediction')

input= st.number_input('How Old Are You? ')
student = st.text_input('Are you a student ?    Yes/No')

btn =  st.button('Predict')
    
if btn:
    st.write('Welcome to our services')
    if input and student == '':
     st.write('Enter the above cells')
    elif input < 18 and student == 'yes':
     st.write('you are not eligible for this loan')
    elif input >= 18 and student == 'no':
     st.write('You are eligible to apply')
    elif input < 18 and student =='no':
        st.write('You must be 18 years to apply')
    elif input >=18 and student =='yes':
        st.write('You must be greateer than 17 and must not be a student to qualify for the loan')
        st.write('Re-apply later')
    else:
        st.write('complete the cells above')
