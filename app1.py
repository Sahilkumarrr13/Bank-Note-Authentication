import pandas as pd
import pickle
import streamlit as st

with open('rfc.pkl', 'rb') as file:
    rfc = pickle.load(file)

def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction=rfc.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)

    return "The predicted value is " + str(prediction)

def main():
  st.title("Bank Note Authenticator")
  html_temp="""
  <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
  </div>
  """
  st.markdown(html_temp, unsafe_allow_html=True)
  variance = st.text_input('Variance')
  skewnees = st.text_input('skewnees')
  curtosis = st.text_input('curtosis')
  entropy = st.text_input('entropy')
  result = ""
  if st.button('Predict'):
    result = predict_note_authentication(variance, skewnees, curtosis, entropy)
  st.success('The Output is {}'.format(result))
  if st.button('About'):
    st.text("Built with Streamlit and ❤️")

if __name__ == '__main__':
    main()