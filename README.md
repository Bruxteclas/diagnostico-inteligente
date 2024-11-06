# 🩺 Diagnóstico Inteligente de Doenças com Machine Learning

**Website**: [Diagnóstico Inteligente](https://diagnostico-inteligente.onrender.com/)

Este projeto utiliza inteligência artificial para auxiliar na previsão de diagnósticos médicos com base em sintomas informados pelo usuário. Desenvolvido com o poder do **AutoGluon** e uma interface interativa com **Streamlit**, o Diagnóstico Inteligente oferece uma solução acessível para ajudar na triagem de sintomas, fornecendo diagnósticos preliminares em tempo real.

![Captura de tela 2024-11-04 221727](https://github.com/user-attachments/assets/68a6e468-6996-4c2e-a782-dace61a72868)

# 🔍 Visão Geral


O Diagnóstico Inteligente é uma aplicação de aprendizado de máquina que, a partir dos sintomas selecionados, sugere diagnósticos prováveis. Essa ferramenta foi treinada usando o **AutoGluon** com dados disponíveis no Kaggle para prever uma variedade de doenças comuns.

- **Link para os Dados**: [Disease Prediction Dataset no Kaggle](https://www.kaggle.com/datasets/marslinoedward/disease-prediction-data)

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é demonstrar como um modelo de aprendizado de máquina pode ser implementado em um sistema web interativo na área da saúde. A ferramenta foi desenvolvida para fins de demonstração, ilustrando o potencial do uso de IA para identificar possíveis condições médicas com base nos sintomas fornecidos pelo usuário. 
🚨**Importante**: esta ferramenta não se destina a fornecer diagnósticos médicos nem a ser utilizada por profissionais de saúde, servindo apenas como um exemplo de aplicação da inteligência artificial na área médica.

---


### Lista Completa de Doenças e Sintomas

Abaixo, fornecemos uma lista de doenças e seus principais sintomas para ajudar na escolha correta e melhorar a precisão das previsões.

| **Doença**                        | **Sintomas**                                                                                                                                                                           |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Fungal infection**              | itching, skin_rash, nodal_skin_eruptions, dischromic_patches                                                                                                                           |
| **Allergy**                       | continuous_sneezing, shivering, chills, watering_from_eyes                                                                                                                             |
| **GERD**                          | stomach_pain, acidity, ulcers_on_tongue, vomiting, cough, chest_pain                                                                                                                  |
| **Chronic cholestasis**           | itching, vomiting, yellowish_skin, nausea, loss_of_appetite, abdominal_pain, yellowing_of_eyes                                                                                        |
| **Drug Reaction**                 | itching, skin_rash, stomach_pain, burning_micturition, spotting_urination                                                                                                             |
| **Peptic ulcer disease**          | vomiting, indigestion, loss_of_appetite, abdominal_pain, passage_of_gases, internal_itching                                                                                           |
| **AIDS**                          | muscle_wasting, patches_in_throat, high_fever, extra_marital_contacts                                                                                                                 |
| **Diabetes**                      | fatigue, weight_loss, restlessness, lethargy, irregular_sugar_level, blurred_and_distorted_vision, obesity, excessive_hunger, increased_appetite, polyuria                           |
| **Gastroenteritis**               | vomiting, sunken_eyes, dehydration, diarrhoea                                                                                                                                         |
| **Bronchial Asthma**              | fatigue, cough, high_fever, breathlessness, family_history, mucoid_sputum                                                                                                             |
| **Hypertension**                  | headache, chest_pain, dizziness, loss_of_balance, lack_of_concentration                                                                                                               |
| **Migraine**                      | acidity, indigestion, headache, blurred_and_distorted_vision, excessive_hunger, stiff_neck, depression, irritability, visual_disturbances                                           |
| **Cervical spondylosis**          | back_pain, weakness_in_limbs, neck_pain, dizziness, loss_of_balance                                                                                                                   |
| **Paralysis (brain hemorrhage)**  | vomiting, headache, weakness_of_one_body_side, altered_sensorium                                                                                                                      |
| **Jaundice**                      | itching, vomiting, fatigue, weight_loss, high_fever, yellowish_skin, dark_urine, abdominal_pain                                                                                       |
| **Malaria**                       | chills, vomiting, high_fever, sweating, headache, nausea, diarrhoea, muscle_pain                                                                                                      |
| **Chicken pox**                   | itching, skin_rash, fatigue, lethargy, high_fever, headache, loss_of_appetite, mild_fever, swelled_lymph_nodes, malaise, red_spots_over_body                                         |
| **Dengue**                        | skin_rash, chills, joint_pain, vomiting, fatigue, high_fever, headache, nausea, loss_of_appetite, pain_behind_the_eyes, back_pain, malaise, muscle_pain, red_spots_over_body         |
| **Typhoid**                       | chills, vomiting, fatigue, high_fever, headache, nausea, constipation, abdominal_pain, diarrhoea, toxic_look_(typhos), belly_pain                                                   |
| **Hepatitis A**                   | joint_pain, vomiting, yellowish_skin, dark_urine, nausea, loss_of_appetite, abdominal_pain, diarrhoea, mild_fever, yellowing_of_eyes, muscle_pain                                   |
| **Hepatitis B**                   | itching, fatigue, lethargy, yellowish_skin, dark_urine, loss_of_appetite, abdominal_pain, yellow_urine, yellowing_of_eyes, malaise, receiving_blood_transfusion, receiving_unsterile_injections |
| **Hepatitis C**                   | fatigue, yellowish_skin, nausea, loss_of_appetite, yellowing_of_eyes, family_history                                                                                                  |
| **Hepatitis D**                   | joint_pain, vomiting, fatigue, yellowish_skin, dark_urine, nausea, loss_of_appetite, abdominal_pain, yellowing_of_eyes                                                                |
| **Hepatitis E**                   | joint_pain, vomiting, fatigue, high_fever, yellowish_skin, dark_urine, nausea, loss_of_appetite, abdominal_pain, yellowing_of_eyes, acute_liver_failure, coma, stomach_bleeding      |
| **Alcoholic hepatitis**           | vomiting, yellowish_skin, abdominal_pain, swelling_of_stomach, distention_of_abdomen, history_of_alcohol_consumption, fluid_overload.1                                               |
| **Tuberculosis**                  | chills, vomiting, fatigue, weight_loss, cough, high_fever, breathlessness, sweating, loss_of_appetite, mild_fever, yellowing_of_eyes, swelled_lymph_nodes, malaise, phlegm, chest_pain, blood_in_sputum |
| **Common Cold**                   | continuous_sneezing, chills, fatigue, cough, high_fever, headache, swelled_lymph_nodes, malaise, phlegm, throat_irritation, redness_of_eyes, sinus_pressure, runny_nose, congestion, chest_pain, loss_of_smell, muscle_pain |
| **Pneumonia**                     | chills, fatigue, cough, high_fever, breathlessness, sweating, malaise, phlegm, chest_pain, fast_heart_rate, rusty_sputum                                                             |
| **Dimorphic hemorrhoids (piles)** | constipation, pain_during_bowel_movements, pain_in_anal_region, bloody_stool, irritation_in_anus                                                                                     |
| **Heart attack**                  | vomiting, breathlessness, sweating, chest_pain                                                                                                                                       |
| **Varicose veins**                | fatigue, cramps, bruising, obesity, swollen_legs, swollen_blood_vessels, prominent_veins_on_calf                                                                                     |
| **Hypothyroidism**                | fatigue, weight_gain, cold_hands_and_feets, mood_swings, lethargy, dizziness, puffy_face_and_eyes, enlarged_thyroid, brittle_nails, swollen_extremities, depression, irritability  |
| **Hyperthyroidism**               | fatigue, mood_swings, weight_loss, restlessness, sweating, diarrhoea, fast_heart_rate, excessive_hunger, muscle_weakness, irritability, abnormal_menstruation                      |
| **Hypoglycemia**                  | vomiting, fatigue, anxiety, sweating, headache, nausea, blurred_and_distorted_vision, excessive_hunger, drying_and_tingling_lips, slurred_speech, irritability, palpitations       |
| **Osteoarthritis**                | joint_pain, neck_pain, knee_pain, hip_joint_pain, swelling_joints, painful_walking                                                                                                   |
| **Arthritis**                     | muscle_weakness, stiff_neck, swelling_joints, movement_stiffness, painful_walking                                                                                                    |
| **(vertigo) Paroymsal Positional Vertigo** | vomiting, headache, nausea, spinning_movements, loss_of_balance, unsteadiness                                                              |
| **Acne**                          | skin_rash, pus_filled_pimples, blackheads, scurring                                                                                                                                  |
| **Urinary tract infection**       | burning_micturition, bladder_discomfort, foul_smell_of_urine, continuous_feel_of_urine                                                                                               |
| **Psoriasis**                     | skin_rash, joint_pain, skin_peeling, silver_like_dusting, small_dents_in_nails, inflammatory_nails                                                                                   |
| **Impetigo**                      | skin_rash, high_fever, blister, red_sore_around_nose, yellow_crust_ooze                                                                                                              |
| **Acne**                          | itching, skin_rash, red_spots_over_body, family_history, skin_peeling, red_sore_around_nose                                                                                          |

---

## 🚀 Funcionalidades Principais

✨ **Previsão de Diagnóstico**: Selecione sintomas e receba uma previsão de diagnóstico em tempo real.

🌐 **Interface Web Amigável**: Uma interface simples e responsiva criada com **Streamlit**.

📈 **Alta Precisão**: Treinado com **AutoGluon**, o modelo atinge mais de **97% de acurácia**.

🔒 **Acesso Remoto Seguro**: Hospedado no Render, você pode acessar de qualquer lugar.

## 🛠️ Tecnologias Utilizadas

- **AutoGluon**: Para o treinamento e previsão do modelo.
- **Streamlit**: Para a criação da interface web interativa.
- **Ngrok**: Exposição do servidor para testes.
- **Render**: Hospedagem e deploy do aplicativo.

## 📦 Instalação Local

Se desejar rodar o projeto localmente, siga os passos abaixo:

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seuusuario/diagnostico-inteligente.git
   cd diagnostico-inteligente
   ```

2. **Instale as Dependências**:
   Certifique-se de que o `Dockerfile` e o `requirements.txt` estejam configurados e execute:
   ```bash
   docker build -t diagnostico-inteligente .
   docker run -p 8501:8501 diagnostico-inteligente
   ```

3. **Acesse o Aplicativo**:
   O aplicativo estará disponível em `http://localhost:8501`.

---

## 🖱️ Como Usar

1. Acesse o site: [Diagnóstico Inteligente](https://diagnostico-inteligente.onrender.com/).
2. Selecione os sintomas que você apresenta na lista de sintomas.
3. Clique no botão "Prever".
4. Veja o diagnóstico sugerido baseado nos sintomas.

---

## 📊 Dados e Treinamento do Modelo

O modelo foi treinado utilizando o [dataset Disease Prediction no Kaggle](https://www.kaggle.com/datasets/marslinoedward/disease-prediction-data), que contém dados sobre sintomas e diagnósticos médicos.

### **Etapas de Treinamento**

1. **Pré-processamento**: Limpeza e transformação dos dados para uso no modelo.
2. **Treinamento**: Utilização do AutoGluon para treinar um modelo de classificação.
3. **Validação**: Avaliação do modelo com métricas de precisão e recall.

---

## 📊 Resultados e Desempenho do Modelo

### 🔍 Desempenho Geral
O modelo de IA foi avaliado em um conjunto de dados abrangente e atingiu excelentes resultados:

- **Acurácia**: 97.6%
- **Balanced Accuracy**: 98.8%
- **MCC (Matthews Correlation Coefficient)**: 97.6%

### 📋 Relatório de Classificação

Cada condição médica foi classificada com alta precisão, como mostra a tabela abaixo:

| Doença                            | Precisão | Recall | F1-Score | Total  |
|-----------------------------------|----------|--------|----------|--------|
| (vertigo) Paroymsal Positional Vertigo | 1.00     | 1.00   | 1.00     | 1      |
| AIDS                              | 1.00     | 1.00   | 1.00     | 1      |
| Acne                              | 1.00     | 1.00   | 1.00     | 1      |
| Pneumonia                         | 1.00     | 1.00   | 1.00     | 1      |
| Varicose veins                    | 1.00     | 1.00   | 1.00     | 1      |
| **E outras...**                   | ...      | ...    | ...      | ...    |

### 🖼️ Matriz de Confusão
Veja a matriz de confusão para entender melhor a precisão do modelo em diferentes diagnósticos:

![image](https://github.com/user-attachments/assets/36e30c5a-a179-4b35-a46b-41177fd32fd0)

### Matriz de Confusão

A matriz de confusão me permite visualizar onde o modelo está acertando ou errando nas previsões. Cada célula mostra o número de previsões corretas ou incorretas entre as classes reais e previstas.

---
## Limitações do Modelo

Nosso modelo apresenta boa precisão, mas algumas limitações precisam ser consideradas para garantir melhores previsões:

### Sensibilidade a Sintomas Omissos
   - **Descrição**: Certas doenças apresentam sintomas muito semelhantes, e a ausência de sintomas específicos pode levar a previsões incorretas. Esse problema é particularmente relevante para doenças como resfriado, gripe, hepatites e outras infecções respiratórias, que compartilham muitos sintomas comuns.
   - **Orientação para o Usuário**: Para melhorar a precisão, selecione todos os sintomas relevantes sempre que possível, mesmo que nem todos os sintomas estejam imediatamente presentes no quadro clínico do paciente.

---
## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* e *pull requests*.

---


### 🚨 Aviso Importante

Este projeto é apenas uma ferramenta de auxílio e **não substitui um diagnóstico médico profissional**. Consulte sempre um profissional de saúde para obter uma avaliação completa.

