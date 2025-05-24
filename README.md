# 🔮 Friction Forecast: Predicting and Understanding Employee Attrition at IBM / 🔮 Friction Forecast: Prevendo e Entendendo a Atrição de Funcionários na IBM

## 🎯 Introduction / 🎯 Introdução

**English:**
Talent loss is a critical challenge for any organization. The **Friction Forecast** project delves into IBM's Human Resources data with the aim of not only predicting employee attrition but also of identifying the main factors that lead to this decision. By understanding the root causes, we can equip IBM with insights to develop more effective retention strategies.

**Português:**
A perda de talentos é um desafio crítico para qualquer organização. O projeto **Friction Forecast** mergulha nos dados de Recursos Humanos da IBM com o objetivo de não apenas prever a atrição de funcionários, mas também de identificar os principais fatores que levam a essa decisão. Ao entender as causas raízes, podemos munir a IBM com insights para desenvolver estratégias de retenção mais eficazes.

---

## 🗺️ Data Exploration and Discoveries (EDA) / 🗺️ Exploração e Descobertas dos Dados (EDA)

**English:**
Our journey began with a detailed exploratory analysis of IBM's employee dataset. The goal was clear: to find hidden patterns and clues that could tell us a story about attrition.

### 📊 Key EDA Findings:

- **Attrition Imbalance:** We found that approximately 16.12% of employees in the dataset had left the company, while 83.88% remained. This imbalance is a crucial point to consider in predictive modeling.
- **Cleaning and Preparation:** We removed irrelevant columns (like `EmployeeCount`, `Over18`, `StandardHours`) and unique identifiers (`EmployeeNumber`) that would not add value to the model. Fortunately, the data proved to be of high quality, with no missing values or duplicates.
- **Attribute Categorization:** Variables were carefully separated into nominal, ordinal, and numerical to guide subsequent transformations and visualizations.
- **Distributions and Relationships:**
  - Through histograms and boxplots, we analyzed the distribution of numerical variables like `MonthlyIncome`, `DistanceFromHome`, and `TotalWorkingYears`, comparing the profiles of employees who left versus those who stayed.
  - A correlation heatmap allowed us to visualize the relationships between numerical variables, identifying potential multicollinearities and associated factors.

**Português:**
Nossa jornada começou com uma análise exploratória detalhada do conjunto de dados de funcionários da IBM. O objetivo era claro: encontrar padrões e pistas escondidas que pudessem nos contar uma história sobre a atrição.

### 📊 Principais Achados da EDA:

- **Desbalanceamento da Atrição:** Constatamos que aproximadamente 16,12% dos funcionários no dataset deixaram a empresa, enquanto 83,88% permaneceram. Esse desbalanceamento é um ponto crucial a ser considerado na modelagem preditiva.
- **Limpeza e Preparação:** Removemos colunas irrelevantes (como `EmployeeCount`, `Over18`, `StandardHours`) e identificadores únicos (`EmployeeNumber`) que não agregariam valor ao modelo. Felizmente, os dados se mostraram de alta qualidade, sem valores ausentes ou duplicatas.
- **Categorização de Atributos:** As variáveis foram cuidadosamente separadas em nominais, ordinais e numéricas para guiar as transformações e visualizações subsequentes.
- **Distribuições e Relações:**
  - Através de histogramas e boxplots, analisamos a distribuição de variáveis numéricas como `MonthlyIncome`, `DistanceFromHome` e `TotalWorkingYears`, comparando os perfis de funcionários que saíram versus os que ficaram.
  - Um mapa de calor de correlação nos permitiu visualizar as relações entre as variáveis numéricas, identificando potenciais multicollinearidades e fatores associados.

### 📈 Interactive Dashboard and Graphics (Illustrative Example) / 📈 Painel Interativo e Gráficos (Exemplo Ilustrativo)

_(This section describes what dashboards and graphics would ideally show. Please replace with your actual visuals or links.)_
_(Esta seção descreve o que os painéis e gráficos idealmente mostrariam. Por favor, substitua com seus visuais reais ou links.)_

**English:**
An interactive dashboard would complement our EDA, allowing for dynamic exploration of the data. We could visualize:

- **Attrition Rate by Department:** A bar chart showing which department has the highest turnover rate.
- **Monthly Income vs. Attrition:** Boxplots comparing salary distribution between the groups.
- **Overtime and Attrition:** A chart showing the proportion of employees who work overtime and leave the company.
- **Job Satisfaction:** Pie or bar charts illustrating the satisfaction levels of employees who stayed and those who left.

These visualizations would help solidify insights and effectively communicate findings to stakeholders.

**Português:**
Um painel interativo complementaria nossa EDA, permitindo uma exploração dinâmica dos dados. Poderíamos visualizar:

- **Taxa de Atrição por Departamento:** Um gráfico de barras mostrando qual departamento tem a maior taxa de evasão.
- **Renda Mensal vs. Atrição:** Boxplots comparando a distribuição salarial entre os grupos.
- **Horas Extras e Atrição:** Um gráfico mostrando a proporção de funcionários que fazem horas extras e saem da empresa.
- **Satisfação no Trabalho:** Gráficos de pizza ou barras ilustrando os níveis de satisfação dos funcionários que ficaram e dos que saíram.

Essas visualizações ajudariam a solidificar os insights e a comunicar as descobertas de forma eficaz para as partes interessadas.

---

## ⚙️ Building the Predictive Model / ⚙️ Construindo o Modelo Preditivo

**English:**
With insights from the EDA, we moved on to building a machine learning model capable of predicting attrition.

### 🛠️ Data Preparation for Modeling:

- **Target Variable Encoding:** The `Attrition` variable was transformed from categorical ("Yes"/"No") to numerical (1/0).
- **Feature Engineering and Preprocessing:** We applied specific transformations for each type of variable:
  - `OneHotEncoder` for nominal variables.
  - `OrdinalEncoder` for ordinal variables.
  - `MinMaxScaler`, `StandardScaler`, and `PowerTransformer` for different sets of numerical variables to optimize model performance.
- **Handling Imbalance:** We calculated `scale_pos_weight` (approximately 5.2) so that models would give due importance to the minority class (attrited employees), especially for algorithms like XGBoost and LightGBM.

### 🧠 Model Selection and Evaluation:

Several classification algorithms were tested, including:

- Dummy Classifier (baseline)
- Logistic Regression
- Decision Tree
- Gradient Boosting
- LGBM Classifier
- XGBoost

We used stratified cross-validation to ensure the robustness of the results. **Logistic Regression** showed the best initial performance in terms of `test_average_precision` (0.613) and `test_roc_auc` (0.824).

### 🚀 Optimization and Final Model:

We performed a grid search (`GridSearchCV`) to optimize the hyperparameters of Logistic Regression. The final model, with parameters `{'clf__C': 0.1, 'clf__l1_ratio': 0.5, 'clf__penalty': 'elasticnet'}`, achieved an **average_precision of approximately 0.635**.

### 🔑 Key Predictive Factors (Based on Logistic Regression Coefficients):

The coefficients of the final model revealed the most significant drivers of attrition:

- **Factors that INCREASE the likelihood of attrition:**
  - Working **Overtime** (`OverTime_Yes`)
  - **Frequent Business Travel** (`BusinessTravel_Travel_Frequently`)
  - Being **Single** (`MaritalStatus_Single`)
  - Number of **Previous Companies Worked**
- **Factors that DECREASE the likelihood of attrition:**
  - High **Job Involvement** (`Ordinal__JobInvolvement`)
  - Higher **Monthly Income** (`power_transform__MonthlyIncome`)
  - Higher **Environment Satisfaction** (`Ordinal__EnvironmentSatisfaction`)
  - Being in the **Research & Development** department

**Português:**
Com os insights da EDA, partimos para a construção de um modelo de aprendizado de máquina capaz de prever a atrição.

### 🛠️ Preparação dos Dados para Modelagem:

- **Codificação da Variável Alvo:** A variável `Attrition` foi transformada de categórica ("Yes"/"No") para numérica (1/0).
- **Engenharia de Atributos e Pré-processamento:** Aplicamos transformações específicas para cada tipo de variável:
  - `OneHotEncoder` para variáveis nominais.
  - `OrdinalEncoder` para variáveis ordinais.
  - `MinMaxScaler`, `StandardScaler` e `PowerTransformer` para diferentes conjuntos de variáveis numéricas, visando otimizar o desempenho dos modelos.
- **Tratamento de Desbalanceamento:** Calculamos o `scale_pos_weight` (aproximadamente 5.2) para que os modelos dessem a devida importância à classe minoritária (funcionários com atrição), especialmente para algoritmos como XGBoost e LightGBM.

### 🧠 Seleção e Avaliação de Modelos:

Diversos algoritmos de classificação foram testados, incluindo:

- Dummy Classifier (linha de base)
- Regressão Logística
- Árvore de Decisão
- Gradient Boosting
- LGBM Classifier
- XGBoost

Utilizamos validação cruzada estratificada para garantir a robustez dos resultados. A **Regressão Logística** apresentou o melhor desempenho inicial em termos de `test_average_precision` (0.613) e `test_roc_auc` (0.824).

### 🚀 Otimização e Modelo Final:

Realizamos uma busca em grade (`GridSearchCV`) para otimizar os hiperparâmetros da Regressão Logística. O modelo final, com os parâmetros `{'clf__C': 0.1, 'clf__l1_ratio': 0.5, 'clf__penalty': 'elasticnet'}`, alcançou uma **average_precision de aproximadamente 0.635**.

### 🔑 Principais Fatores Preditivos (Baseado nos Coeficientes da Regressão Logística):

Os coeficientes do modelo final nos revelaram os impulsionadores mais significativos da atrição:

- **Fatores que AUMENTAM a probabilidade de atrição:**
  - Trabalhar **Horas Extras** (`OverTime_Yes`)
  - **Viagens de Negócios Frequentes** (`BusinessTravel_Travel_Frequently`)
  - Ser **Solteiro** (`MaritalStatus_Single`)
  - **Número de Empresas Anteriores**
- **Fatores que DIMINUEM a probabilidade de atrição:**
  - Alto **Envolvimento no Trabalho** (`Ordinal__JobInvolvement`)
  - Maior **Renda Mensal** (`power_transform__MonthlyIncome`)
  - Maior **Satisfação com o Ambiente** (`Ordinal__EnvironmentSatisfaction`)
  - Estar no departamento de **Pesquisa & Desenvolvimento**

---

## 🖥️ Friction Forecast Web App: How to Use / 🖥️ Friction Forecast Web App: Como Usar

**English:**
To make the model's insights actionable, we developed the **Friction Forecast** web application. It allows HR managers to input an employee's information and receive a prediction about their likelihood of attrition.

### Instructions for Use:

1.  **Access the Application:** Open the Streamlit application (usually by running `streamlit run home.py` in your terminal, in the project directory).

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

1.  **Acesse o Aplicativo:** Abra o aplicativo Streamlit (normalmente executando `streamlit run home.py` no seu terminal, no diretório do projeto).

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
