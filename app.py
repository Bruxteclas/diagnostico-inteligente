import streamlit as st

# Configurando o layout da página
st.set_page_config(page_title="Previsão de Doenças com AutoGluon", page_icon="🩺", layout="wide")

import pandas as pd
import joblib
from PIL import Image
import base64

# Função para adicionar imagem de fundo
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Adicionando imagem de fundo
add_bg_from_local('cena-de-saude-2_173691-553.avif')

# Carregando o modelo e o LabelEncoder
predictor = joblib.load('predictor_independente.pkl')
label_encoder = joblib.load('label_encoder.joblib') 

# Cabeçalho do aplicativo com título e subtítulo
st.title("🩺 Previsão de Doenças com AutoGluon")
st.markdown("**Descubra possíveis diagnósticos com base nos sintomas apresentados de forma rápida e precisa.**")
st.markdown("---")

# Seção de instruções 
st.markdown(
    "<div style='background-color: #f9f9f9; padding: 15px; border-radius: 10px;'>"
    "<h4 style='text-align: center; color: #333;'>Preencha os sintomas apresentados pelo paciente e clique em Prever.</h4>"
    "</div>",
    unsafe_allow_html=True
)

# Lista de sintomas
sintomas = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills',
    'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting',
    'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety',
    'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy',
    'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes',
    'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin',
    'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation',
    'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
    'acute_liver_failure', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise',
    'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'chest_pain', 'weakness_in_limbs',
    'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
    'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
    'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
    'swollen_extremities', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
    'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
    'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance',
    'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort',
    'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
    'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium',
    'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches',
    'watering_from_eyes', 'increased_appetite', 'family_history', 'mucoid_sputum', 'rusty_sputum',
    'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'coma',
    'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum',
    'prominent_veins_on_calf', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
    'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
    'red_sore_around_nose', 'yellow_crust_ooze'
]

# Seleção de sintomas
sintomas_selecionados = st.multiselect("Escolha os sintomas apresentados:", options=sintomas)

# Inicializando a variável previsao_significado como None
previsao_significado = None

# Botão de previsão
if st.button("Prever", help="Clique para realizar a previsão baseada nos sintomas selecionados"):
    dados_usuario = pd.DataFrame([{sintoma: 1 if sintoma in sintomas_selecionados else 0 for sintoma in sintomas}])

# fazendo previsão
    previsao = predictor.predict(dados_usuario)[0]
    previsao_significado = label_encoder.inverse_transform([previsao])[0]

# Exibindo o resultado 
if previsao_significado is not None:
    st.markdown(
        f"""
        <div style="background-color: #dff9fb; padding: 20px; border-radius: 10px; text-align: center; margin-top: 20px;">
            <h2 style="color: #130f40; font-weight: bold;">Previsão: {previsao_significado}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.balloons()

# Rodapé
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #555;'>"
    "Desenvolvido com 💖 por Paulo Eduardo, Cientista de Dados e Engenheiro de Machine Learning</div>",
    unsafe_allow_html=True
)
