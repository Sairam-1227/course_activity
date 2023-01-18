import pickle
import streamlit as st 


pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)


def predict_note_authentication(Age,Experience,Income,Family,CCAvg,Education,Mortgage,SecuritiesAccount,CDAccount,Online,CreditCard):
    prediction=model.predict([[Age,Experience,Income,Family,CCAvg,Education,Mortgage,SecuritiesAccount,CDAccount,Online,CreditCard]])
    print(prediction)
    return prediction

def main():
    st.title("Personal Loan Prediction")
    Age = st.text_input("Age")
    Experience = st.text_input("Experience")
    Income = st.text_input("Income value")
    Family = st.text_input("Number of people")
    CCAvg = st.text_input("CC Avg value")
    Education = st.text_input("Education value")
    Mortgage = st.text_input("Mortgage value")
    SecuritiesAccount = st.text_input("Number of Accounts")
    CDAccount = st.text_input("CD account value")
    Online = st.text_input("online value")
    CreditCard = st.text_input("creditcard value")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Age,Experience,Income,Family,CCAvg,Education,Mortgage,SecuritiesAccount,CDAccount,Online,CreditCard)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()
    
    
    
