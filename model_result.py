import streamlit as st
import joblib
import pandas as pd
def app ():
    @st.cache(allow_output_mutation=True)
    def load(scaler_path, model_path):
        sc = joblib.load(scaler_path)
        model = joblib.load(model_path)
        return sc , model

    def inference(row, scaler, model, feat_cols):
        df = pd.DataFrame([row], columns = feat_cols)
        X = scaler.transform(df)
        features = pd.DataFrame(X, columns = feat_cols)
        if (model.predict(features)==0):
            return "The patient will be re-admitted "
        else: return "The patient will not be re-admited "
        
    st.title('Readmission recommender App')
    st.write('Interactive web app with streamlit')


    st.write('Please fill details of the patient information in the left sidebar and click on the button below!')
    discharge_disposition_id = st.sidebar.number_input(
            "discharge_disposition_id",
            min_value=1,
            max_value=None,
            value=100,
            step=1,
            help="Fill discharge disposition id in number",
            )
    time_in_hospital = st.sidebar.number_input(
            "time_in_hospital",
            min_value=1,
            max_value=None,
            value=100,
            step=1,
            help="Fill number of time in hospital",
            )   


    num_medications = st.sidebar.number_input(
            "num_medications",
            min_value=1,
            max_value=None,
            value=100,
            step=1,
            help="Fill number of medication",
            )

    number_outpatient = st.sidebar.number_input(
            "number_outpatient",
            min_value=0,
            max_value=None,
            value=100,
            step=1,
            help="Fill number of outpatient	",
            )

    number_emergency = st.sidebar.number_input(
            "number_emergency",
            min_value=0,
            max_value=None,
            value=100,
            step=1,
            help="Fill number of patinets in emergency",
            )
    

    number_inpatient = st.sidebar.number_input(
            "number_inpatient",
            min_value=0,
            max_value=None,
            value=100,
            step=1,
            help="Fill number of inpatient",
            )
    

    number_diagnoses = st.sidebar.number_input(
            "number_diagnoses",
            min_value=0,
            max_value=None,
            value=100,
            step=1,
            help="Fill number of diagnoses",
            )
    
    change = st.sidebar.radio("Select change: ", ('Change', 'No'))
    

    if (change== 'Change'):
        change=1
    else:
        change=0
    diabetesMed= st.sidebar.radio("Select diabetes Medication: ", ('Yes', 'No'))
 

    if (diabetesMed== 'yes'):
        diabetesMed=1
    else:
        diabetesMed=0

    row = [discharge_disposition_id, time_in_hospital, num_medications, number_outpatient, number_emergency, number_inpatient, number_diagnoses, change, diabetesMed]

    if (st.button('Find Patient Status')):
        feat_cols = ['discharge_disposition_id', 'time_in_hospital', 'num_medications', 'number_outpatient', 'number_emergency', 'number_inpatient', 'number_diagnoses', 'change', 'diabetesMed']
        sc, model = load('models/scaler.pkl', 'models/model.pkl')
        result = inference(row, sc, model, feat_cols)
        st.write(result)
        
