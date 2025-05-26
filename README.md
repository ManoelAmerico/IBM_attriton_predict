# 🔮 Friction Forecast: Predicting and Understanding Employee Attrition at IBM / 🔮 Friction Forecast: Prevendo e Entendendo a Atrição de Funcionários na IBM

## 🎯 Introduction / 🎯 Introdução

**English:**
Talent loss is a critical challenge for any organization. The **Friction Forecast** project delves into IBM's Human Resources data with the aim of not only predicting employee attrition but also of identifying the main factors that lead to this decision. By understanding the root causes, we can equip IBM with insights to develop more effective retention strategies.

**Português:**
A perda de talentos é um desafio crítico para qualquer organização. O projeto **Friction Forecast** mergulha nos dados de Recursos Humanos da IBM com o objetivo de não apenas prever a atrição de funcionários, mas também de identificar os principais fatores que levam a essa decisão. Ao entender as causas raízes, podemos munir a IBM com insights para desenvolver estratégias de retenção mais eficazes.

## 📁 Repository Structure / 📁 Estrutura do Repositório

**English:**
The project is organized as follows:
```
.
├── notebooks/                  # Contains Jupyter notebooks for analysis and modeling
│   ├── 1_eda.ipynb             # Notebook for Exploratory Data Analysis (EDA)
│   ├── 2_model.ipynb           # Notebook for model development and training
│   └── src/                    # Source code used by the notebooks
│       ├── config.py           # Configuration files (e.g., data paths)
│       ├── graphics.py         # Functions for generating plots
│       ├── models.py           # Model training and evaluation helper functions
│       └── utils.py            # Utility functions
├── data/                       # Directory for datasets
│   ├── raw/                    # Raw data (e.g., ORIGINAL_DATA location defined in config.py)
│   └── processed/              # Processed data (e.g., PROCESSED_DATA location defined in config.py)
├── home.py                     # Main Streamlit application file
├── models/                     # Saved trained models (e.g., FINAL_MODEL location defined in config.py)
├── README.md                   # This file, providing an overview of the project
└── ...                         # Other project files (e.g., .gitignore, requirements.txt)
```

**Português:**
O projeto está organizado da seguinte forma:
```
.
├── notebooks/                  # Contém os notebooks Jupyter para análise e modelagem
│   ├── 1_eda.ipynb             # Notebook para Análise Exploratória de Dados (EDA)
│   ├── 2_model.ipynb           # Notebook para desenvolvimento e treinamento do modelo
│   └── src/                    # Código fonte utilizado pelos notebooks
│       ├── config.py           # Arquivos de configuração (ex: caminhos dos dados)
│       ├── graphics.py         # Funções para geração de gráficos
│       ├── models.py           # Funções auxiliares para treinamento e avaliação de modelos
│       └── utils.py            # Funções utilitárias
├── data/                       # Diretório para os conjuntos de dados
│   ├── raw/                    # Dados brutos (ex: localização de ORIGINAL_DATA definida em config.py)
│   └── processed/              # Dados processados (ex: localização de PROCESSED_DATA definida em config.py)
├── home.py                     # Arquivo principal da aplicação Streamlit
├── models/                     # Modelos treinados salvos (ex: localização de FINAL_MODEL definida em config.py)
├── README.md                   # Este arquivo, fornecendo uma visão geral do projeto
└── ...                         # Outros arquivos do projeto (ex: .gitignore, requirements.txt)
```
---

## 🗺️ Data Exploration and Discoveries (EDA) / 🗺️ Exploração e Descobertas dos Dados (EDA)

**English:**
Our journey began with a detailed exploratory analysis of IBM's employee dataset. The goal was clear: to find hidden patterns and clues that could tell us a story about attrition.

### 📊 Key EDA Findings:

- **Attrition Imbalance:** We observed that approximately 16.12% of employees in the dataset had left the company, while 83.88% remained. This imbalance is a crucial point to consider in predictive modeling.
- **Cleaning and Preparation:** We streamlined the dataset by removing columns that offered no predictive value, such as `EmployeeCount`, `Over18`, and `StandardHours` (which had identical values for all employees), and the unique identifier `EmployeeNumber`. Importantly, our data was high quality, with no missing values or duplicate records found.
- **Attribute Categorization:** Variables were carefully classified into nominal (e.g., `Department`), ordinal (e.g., `Education`), and numerical (e.g., `MonthlyIncome`) types to guide appropriate analysis and transformation.
- **Visual Insights from Data Distributions and Relationships:**

  - **Understanding Numerical Features (Histograms & Boxplots):** Our initial exploration involved generating histograms for all 14 numerical features (as seen in cells 19 and 20 of `1_eda.ipynb`). These plots revealed the underlying distributions; for example, `MonthlyIncome` was right-skewed, indicating a larger concentration of employees in lower to mid-income brackets. `HourlyRate`, in contrast, showed a more uniform distribution. Boxplots alongside these provided a concise summary of each feature's spread, central tendency, and potential outliers.

    ![Image of Histograms for Numerical Features](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/histogram_numerical.png)
    
    ![Image of Boxplots for Numerical Features](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/boxplot_numerical.png)

  - **Attrition's Tale in Numbers (Comparative Boxplots):** To draw early connections to attrition, we visualized numerical features against the attrition status (cell 21 of `1_eda.ipynb`). These comparative boxplots offered initial clues. For instance, employees who left the company tended to have, on average, lower `MonthlyIncome`. The `DistanceFromHome` also showed a wider interquartile range for those who attrited, suggesting greater variability in commute for this group.

    ![Image of Comparative Boxplots (Numerical Features vs Attrition)](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/boxplot_numerical_attrition.png)

  - **Interconnectedness of Features (Correlation Heatmap):** A Pearson correlation heatmap (cell 22 of `1_eda.ipynb`) vividly displayed the relationships between numerical variables. Strong positive correlations were evident, such as between `TotalWorkingYears` and `MonthlyIncome`, and between `YearsAtCompany` and `YearsWithCurrManager`. This also helped us to be mindful of potential multicollinearity when selecting models.

    ![Image of Correlation Heatmap](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/heatmap_correlation.png)

**Português:**
Nossa jornada começou com uma análise exploratória detalhada do conjunto de dados de funcionários da IBM. O objetivo era claro: encontrar padrões e pistas escondidas que pudessem nos contar uma história sobre a atrição.

### 📊 Principais Achados da EDA:

- **Desbalanceamento da Atrição:** Constatamos que aproximadamente 16,12% dos funcionários no dataset deixaram a empresa, enquanto 83,88% permaneceram. Esse desbalanceamento é um ponto crucial a ser considerado na modelagem preditiva.
- **Limpeza e Preparação:** Otimizamos o conjunto de dados removendo colunas que não ofereciam valor preditivo, como `EmployeeCount`, `Over18` e `StandardHours` (que possuíam valores idênticos para todos os funcionários), e o identificador único `EmployeeNumber`. Importante destacar que nossos dados se mostraram de alta qualidade, sem valores ausentes ou registros duplicados.
- **Categorização de Atributos:** As variáveis foram cuidadosamente classificadas em nominais (ex: `Department`), ordinais (ex: `Education`) e numéricas (ex: `MonthlyIncome`) para guiar análises e transformações apropriadas.
- **Insights Visuais das Distribuições e Relações dos Dados:**

  - **Entendendo as Variáveis Numéricas (Histogramas e Boxplots):** Nossa exploração inicial envolveu a geração de histogramas para todas as 14 variáveis numéricas (conforme visto nas células 19 e 20 do `1_eda.ipynb`). Esses gráficos revelaram as distribuições subjacentes; por exemplo, `MonthlyIncome` apresentou assimetria à direita, indicando uma maior concentração de funcionários nas faixas de renda mais baixas e médias. `HourlyRate`, em contraste, mostrou uma distribuição mais uniforme. Boxplots complementares forneceram um resumo conciso da dispersão, tendência central e potenciais outliers de cada variável.

    ![Imagem de Histogramas para Variáveis Numéricas](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/histogram_numerical.png)
    
    ![Imagem de Boxplots para Variáveis Numéricas](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/boxplot_numerical.png)

  - **A História da Atrição em Números (Boxplots Comparativos):** Para traçar conexões iniciais com a atrição, visualizamos as variáveis numéricas em relação ao status de atrição (célula 21 do `1_eda.ipynb`). Esses boxplots comparativos ofereceram pistas iniciais. Por exemplo, funcionários que deixaram a empresa tendiam a ter, em média, menor `MonthlyIncome`. A `DistanceFromHome` também mostrou uma maior amplitude interquartil para aqueles que saíram, sugerindo maior variabilidade no deslocamento para este grupo.

    ![Imagem de Boxplots Comparativos (Variáveis Numéricas vs Atrição)](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/boxplot_numerical_attrition.png)

  - **Interconectividade das Variáveis (Mapa de Calor de Correlação):** Um mapa de calor da correlação de Pearson (célula 22 do `1_eda.ipynb`) exibiu vividamente as relações entre as variáveis numéricas. Fortes correlações positivas foram evidentes, como entre `TotalWorkingYears` e `MonthlyIncome`, e entre `YearsAtCompany` e `YearsWithCurrManager`. Isso também nos ajudou a ter cautela com potencial multicolinearidade ao selecionar modelos.

    ![Imagem de Mapa de Calor de Correlação](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/heatmap_correlation.png)

---

## ⚙️ Building the Predictive Model / ⚙️ Construindo o Modelo Preditivo

**English:**
With insights from the EDA, we moved on to building a machine learning model capable of predicting attrition.

### 🛠️ Data Preparation for Modeling:

- **Target Variable Encoding:** The `Attrition` variable was transformed from categorical ("Yes"/"No") to numerical (1/0) using `LabelEncoder`.
- **Feature Engineering and Preprocessing:** We applied specific transformations for each type of variable using `ColumnTransformer`:
  - `OneHotEncoder` for nominal variables (e.g., `Department`, `Gender`).
  - `OrdinalEncoder` for ordinal variables (e.g., `Education`, `JobSatisfaction`).
  - `MinMaxScaler` for numerical features like `DailyRate`, `StandardScaler` for `Age`, and `PowerTransformer` for others like `MonthlyIncome` and `DistanceFromHome` to optimize model performance by normalizing their distributions.
- **Handling Imbalance:** We calculated `scale_pos_weight` (approximately 5.2) so that models would give due importance to the minority class (attrited employees), especially for algorithms like XGBoost and LightGBM.

### 🧠 Model Selection and Evaluation:

Several classification algorithms were tested using stratified 5-fold cross-validation. The performance of these models was compiled and visualized in a **Model Comparison Box Plot** (generated in cell 15 of `2_model.ipynb`). This plot clearly showed how each model performed across various metrics (Average Precision, ROC AUC, F1-score, Recall, Precision, Accuracy, and Balanced Accuracy). **Logistic Regression** emerged as a strong candidate, particularly due to its robust `test_average_precision` (0.613) and `test_roc_auc` (0.824), which are vital metrics for imbalanced datasets.

![Image of Model Comparison Box Plot](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/boxplot_model.png)

### 🚀 Optimization and Final Model:

We performed a grid search (`GridSearchCV`) to optimize the hyperparameters of Logistic Regression, focusing on `average_precision` as the refit metric. The final model, with parameters `{'clf__C': 0.1, 'clf__l1_ratio': 0.5, 'clf__penalty': 'elasticnet'}`, achieved an **average_precision of approximately 0.635**.

### 🔑 Key Predictive Factors (Based on Logistic Regression Coefficients):

To understand what drives attrition according to our best model, we examined its coefficients. A **Coefficient Importance Plot** (generated in cell 28 of `2_model.ipynb`) visually highlighted the most influential features. This plot revealed:

![Image of Coefficient Importance Plot](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/coeffiente_importance.png)

- **Factors that INCREASE the likelihood of attrition:**
  - Working **Overtime** (`one_hot__OverTime_Yes`) stood out as the strongest positive predictor.
  - **Frequent Business Travel** (`one_hot__BusinessTravel_Travel_Frequently`).
  - Being **Single** (`one_hot__MaritalStatus_Single`).
  - Higher number of **Previous Companies Worked** (`power_transform__NumCompaniesWorked`).
- **Factors that DECREASE the likelihood of attrition:**
  - High **Job Involvement** (`Ordinal__JobInvolvement`) was the most significant factor in retaining employees.
  - Higher **Monthly Income** (`power_transform__MonthlyIncome`).
  - Greater **Environment Satisfaction** (`Ordinal__EnvironmentSatisfaction`).
  - Being in the **Research & Development** department (`one_hot__Department_Research & Development`).
  - Higher **Job Satisfaction** (`Ordinal__JobSatisfaction`).

**Português:**
Com os insights da EDA, partimos para a construção de um modelo de aprendizado de máquina capaz de prever a atrição.

### 🛠️ Preparação dos Dados para Modelagem:

- **Codificação da Variável Alvo:** A variável `Attrition` foi transformada de categórica ("Yes"/"No") para numérica (1/0) usando `LabelEncoder`.
- **Engenharia de Atributos e Pré-processamento:** Aplicamos transformações específicas para cada tipo de variável usando `ColumnTransformer`:
  - `OneHotEncoder` para variáveis nominais (ex: `Department`, `Gender`).
  - `OrdinalEncoder` para variáveis ordinais (ex: `Education`, `JobSatisfaction`).
  - `MinMaxScaler` para variáveis numéricas como `DailyRate`, `StandardScaler` para `Age`, e `PowerTransformer` para outras como `MonthlyIncome` e `DistanceFromHome`, visando otimizar o desempenho dos modelos normalizando suas distribuições.
- **Tratamento de Desbalanceamento:** Calculamos o `scale_pos_weight` (aproximadamente 5.2) para que os modelos dessem a devida importância à classe minoritária (funcionários com atrição), especialmente para algoritmos como XGBoost e LightGBM.

### 🧠 Seleção e Avaliação de Modelos:

Diversos algoritmos de classificação foram testados usando validação cruzada estratificada de 5 folds. O desempenho desses modelos foi compilado e visualizado em um **Boxplot de Comparação de Modelos** (gerado na célula 15 do `2_model.ipynb`). Este gráfico mostrou claramente o desempenho de cada modelo em várias métricas (Average Precision, ROC AUC, F1-score, Recall, Precision, Accuracy e Balanced Accuracy). A **Regressão Logística** emergiu como um forte candidato, particularmente devido à sua robusta `test_average_precision` (0.613) e `test_roc_auc` (0.824), que são métricas vitais para conjuntos de dados desbalanceados.

![Imagem de Boxplot de Comparação de Modelos](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/boxplot_model.png)

### 🚀 Otimização e Modelo Final:

Realizamos uma busca em grade (`GridSearchCV`) para otimizar os hiperparâmetros da Regressão Logística, focando em `average_precision` como métrica de reajuste. O modelo final, com os parâmetros `{'clf__C': 0.1, 'clf__l1_ratio': 0.5, 'clf__penalty': 'elasticnet'}`, alcançou uma **average_precision de aproximadamente 0.635**.

### 🔑 Principais Fatores Preditivos (Baseado nos Coeficientes da Regressão Logística):

Para entender o que impulsiona a atrição de acordo com nosso melhor modelo, examinamos seus coeficientes. Um **Gráfico de Importância dos Coeficientes** (gerado na célula 28 do `2_model.ipynb`) destacou visualmente as variáveis mais influentes. Este gráfico revelou:

![Imagem de Gráfico de Importância dos Coeficientes](https://github.com/ManoelAmerico/IBM_attriton_predict/blob/main/images/coeffiente_importance.png)

- **Fatores que AUMENTAM a probabilidade de atrição:**
  - Trabalhar **Horas Extras** (`one_hot__OverTime_Yes`) destacou-se como o preditor positivo mais forte.
  - **Viagens de Negócios Frequentes** (`one_hot__BusinessTravel_Travel_Frequently`).
  - Ser **Solteiro** (`one_hot__MaritalStatus_Single`).
  - Maior número de **Empresas Anteriores Trabalhadas** (`power_transform__NumCompaniesWorked`).
- **Fatores que DIMINUEM a probabilidade de atrição:**
  - Alto **Envolvimento no Trabalho** (`Ordinal__JobInvolvement`) foi o fator mais significativo na retenção de funcionários.
  - Maior **Renda Mensal** (`power_transform__MonthlyIncome`).
  - Maior **Satisfação com o Ambiente** (`Ordinal__EnvironmentSatisfaction`).
  - Estar no departamento de **Pesquisa & Desenvolvimento** (`one_hot__Department_Research & Development`).
  - Maior **Satisfação no Trabalho** (`Ordinal__JobSatisfaction`).

---

## 🖥️ Friction Forecast Web App: How to Use / 🖥️ Friction Forecast Web App: Como Usar

**English:**
To make the model's insights actionable, we developed the **Friction Forecast** web application. It allows HR managers to input an employee's information and receive a prediction about their likelihood of attrition.

### Instructions for Use:

1.  **Access the Application:** [Web IBM Attrition Predict](https://ibm-attriton-predict.onrender.com)

2.  **Fill in Employee Information:**
    The application will present a series of sections to collect employee data. Fill in each field with the corresponding information:

    - **Personal Information:**

      - `Gender`: Select the gender.
      - `Educational Level`: Choose the educational level (e.g., "Bachelor", "Master" - the app will display user-friendly text like "Below College", "College", etc.).
      - `Training area` (EducationField): Select the field of education.
      - `Distance from home`: Use the slider to indicate the distance from home to work.

    - **Routine at Company:**

      - `Department`: Select the department.
      - `Business Travel`: Indicate the frequency of business travel.
      - `Position` (JobRole): Choose the job role (the list will be filtered based on the selected department).
      - `Overtime`: Mark if the employee works overtime.
      - `Monthly Income`: Use the slider to enter the monthly income.

    - **Professional Experience:**

      - `Companies worked` (NumCompaniesWorked): Number of previously worked companies.
      - `Years worked` (TotalWorkingYears): Total years worked.
      - `Years at Company`: Years at IBM.
      - `Years in Current Position` (YearsInCurrentRole): Years in the current role.
      - `Years with the Same Manager` (YearsWithCurrManager): Years with the same manager.
      - `Years Since Last Promotion`: Years since the last promotion.

    - **Incentives and Metrics:**
      - `Job Satisfaction`: Level of job satisfaction (e.g., "Low", "Medium", "High", "Very High").
      - `Satisfaction with Colleagues` (RelationshipSatisfaction): Level of satisfaction with colleagues.
      - `Work Engagement` (JobInvolvement): Level of work engagement.
      - `Satisfaction with Environment` (EnvironmentSatisfaction): Level of satisfaction with the environment.
      - `Work-Life Balance`: Level of work-life balance (e.g., "Bad", "Good", "Better", "Best").
      - `Stock Option` (StockOptionLevel): Indicate if they have stock options.
      - `Salary increase (%)` (PercentSalaryHike): Percentage of the last salary increase.
      - `Trainings in the Last Year` (TrainingTimesLastYear): Number of trainings in the last year.

3.  **Get the Prediction:**
    After filling in all relevant fields, the application will use the trained Logistic Regression model to calculate the employee's probability of attrition.

    - The result will be displayed, indicating whether the employee has a **low** or **high** probability of leaving the company.
    - The exact probability will also be shown.

4.  **Make Informed Decisions:**
    Based on the prediction, managers can identify at-risk employees and proactively implement personalized retention strategies.

**Português:**
Para tornar os insights do modelo acionáveis, desenvolvemos o aplicativo web **Friction Forecast**. Ele permite que os gestores de RH insiram informações de um funcionário e recebam uma previsão sobre sua probabilidade de atrição.

### Instruções de Uso:

1.  **Acesse o Aplicativo:** [Web Predição de atritor IBM](https://ibm-attriton-predict.onrender.com)

2.  **Preencha as Informações do Funcionário:**
    O aplicativo apresentará uma série de seções para coletar dados do funcionário. Preencha cada campo com a informação correspondente:

    - **Informações Pessoais:**

      - `Gender` (Gênero): Selecione o gênero.
      - `Educational Level` (Nível Educacional): Escolha o nível educacional (o app exibirá textos amigáveis como "Abaixo da Graduação", "Graduação", etc.).
      - `Training area` (Área de Formação - EducationField): Selecione a área de formação.
      - `Distance from home` (Distância de Casa): Use o controle deslizante para indicar a distância da casa ao trabalho.

    - **Rotina na Empresa:**

      - `Department` (Departamento): Selecione o departamento.
      - `Business Travel` (Viagens a Negócio): Indique a frequência de viagens a negócio.
      - `Position` (Cargo - JobRole): Escolha o cargo (a lista será filtrada com base no departamento selecionado).
      - `Overtime` (Horas Extras): Marque se o funcionário faz horas extras.
      - `Monthly Income` (Renda Mensal): Use o controle deslizante para informar a renda mensal.

    - **Experiência Profissional:**

      - `Companies worked` (Empresas Trabalhadas - NumCompaniesWorked): Número de empresas onde trabalhou anteriormente.
      - `Years worked` (Anos Trabalhados - TotalWorkingYears): Total de anos trabalhados.
      - `Years at Company` (Anos na Empresa): Anos na IBM.
      - `Years in Current Position` (Anos no Cargo Atual - YearsInCurrentRole): Anos no cargo atual.
      - `Years with the Same Manager` (Anos com o Mesmo Gestor - YearsWithCurrManager): Anos com o mesmo gestor.
      - `Years Since Last Promotion` (Anos Desde a Última Promoção): Anos desde a última promoção.

    - **Incentivos e Métricas:**
      - `Job Satisfaction` (Satisfação no Trabalho): Nível de satisfação com o trabalho (ex: "Baixa", "Média", "Alta", "Muito Alta").
      - `Satisfaction with Colleagues` (Satisfação com Colegas - RelationshipSatisfaction): Nível de satisfação com os colegas.
      - `Work Engagement` (Engajamento no Trabalho - JobInvolvement): Nível de engajamento no trabalho.
      - `Satisfaction with Environment` (Satisfação com o Ambiente - EnvironmentSatisfaction): Nível de satisfação com o ambiente.
      - `Work-Life Balance` (Equilíbrio Vida-Trabalho): Nível de equilíbrio entre vida pessoal e trabalho (ex: "Ruim", "Bom", "Melhor", "Ótimo").
      - `Stock Option` (Opção de Ações - StockOptionLevel): Indique se possui opções de ações.
      - `Salary increase (%)` (Aumento Salarial (%) - PercentSalaryHike): Percentual do último aumento salarial.
      - `Trainings in the Last Year` (Treinamentos no Último Ano - TrainingTimesLastYear): Número de treinamentos no último ano.

3.  **Obtenha a Previsão:**
    Após preencher todos os campos relevantes, o aplicativo utilizará o modelo de Regressão Logística treinado para calcular a probabilidade de atrição do funcionário.

    - O resultado será exibido, indicando se o funcionário tem **baixa** ou **alta** probabilidade de deixar a empresa.
    - A probabilidade exata também será mostrada.

4.  **Tome Decisões Informadas:**
    Com base na previsão, os gestores podem identificar funcionários em risco e proativamente implementar estratégias de retenção personalizadas.

---

## 🚀 Conclusion / 🚀 Conclusão

**English:**
The Friction Forecast project successfully demonstrated the ability to use HR data to predict employee attrition with a reasonable degree of accuracy, using a Logistic Regression model. More importantly, we identified key factors influencing this decision, providing IBM with a solid foundation for strategic actions.

**Português:**
O projeto Friction Forecast demonstrou com sucesso a capacidade de usar dados de RH para prever a atrição de funcionários com um grau razoável de precisão, utilizando um modelo de Regressão Logística. Mais importante, identificamos os fatores-chave que influenciam essa decisão, fornecendo à IBM uma base sólida para ações estratégicas.
