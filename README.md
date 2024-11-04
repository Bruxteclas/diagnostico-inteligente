# 🩺 Diagnóstico Inteligente de Doenças com Machine Learning

**Website**: [Diagnóstico Inteligente](https://diagnostico-inteligente.onrender.com/)

Este projeto utiliza inteligência artificial para auxiliar na previsão de diagnósticos médicos com base em sintomas informados pelo usuário. Desenvolvido com o poder do **AutoGluon** e uma interface interativa com **Streamlit**, o Diagnóstico Inteligente oferece uma solução acessível para ajudar na triagem de sintomas, fornecendo diagnósticos preliminares em tempo real.

## 🔍 Visão Geral

O Diagnóstico Inteligente é uma aplicação de aprendizado de máquina que, a partir dos sintomas selecionados, sugere diagnósticos prováveis. Essa ferramenta foi treinada usando o **AutoGluon** com dados disponíveis no Kaggle para prever uma variedade de doenças comuns.

- **Link para os Dados**: [Disease Prediction Dataset no Kaggle](https://www.kaggle.com/datasets/marslinoedward/disease-prediction-data)

## 🎯 Objetivo

A ferramenta visa facilitar a triagem inicial, permitindo que pacientes e profissionais da saúde identifiquem rapidamente possíveis condições médicas, possibilitando intervenções mais rápidas e informadas.

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

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* e *pull requests*.

---


### 🚨 Aviso Importante

Este projeto é apenas uma ferramenta de auxílio e **não substitui um diagnóstico médico profissional**. Consulte sempre um profissional de saúde para obter uma avaliação completa.

