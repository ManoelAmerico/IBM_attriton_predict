import pandas as pd
import streamlit as st

from joblib import load

from notebooks.src.config import PROCESSED_DATA, FINAL_MODEL


@st.cache_data
def load_data():
    return pd.read_parquet(PROCESSED_DATA)


@st.cache_resource
def load_model():
    return load(FINAL_MODEL)


df = load_data()
model = load_model()

educational_levels_text = {
    1: "Below College",
    2: "College",
    3: "Bachelor",
    4: "Master",
    5: "PhD",
}

satisfaction_levels_text = {
    1: "Low",
    2: "Medium",
    3: "High",
    4: "Very High",
}

work_life_text_levels = {
    1: "Bad",
    2: "Good",
    3: "Better",
    4: "Best",
}

genres = sorted(df["Gender"].unique())
educational_levels = sorted(df["Education"].unique())
area_formation = sorted(df["EducationField"].unique())
departments = sorted(df["Department"].unique())
travel_business = sorted(df["BusinessTravel"].unique())
overtime = sorted(df["OverTime"].unique())
job_satisfaction = sorted(df["JobSatisfaction"].unique())
colleagues_satisfaction = sorted(df["RelationshipSatisfaction"].unique())
satisfaction_environment = sorted(df["EnvironmentSatisfaction"].unique())
life_work = sorted(df["WorkLifeBalance"].unique())
option_actions = sorted(df["StockOptionLevel"].unique())
work_involvement = sorted(df["JobInvolvement"].unique())

columns_slider = [
    "DistanceFromHome",
    "MonthlyIncome",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager",
]

columns_slider_min_max = {
    column: {"min_value": df[column].min(), "max_value": df[column].max()}
    for column in columns_slider
}

ignored_columns = (
    "Age",
    "DailyRate",
    "JobLevel",
    "HourlyRate",
    "MonthlyRate",
    "PerformanceRating",
)

medians_columns_ignored = {
    column: df[column].median() for column in ignored_columns
}

st.title("Friction Forecast")

with st.container(border=True):
    st.write("### Personal information")

    widget_gender = st.radio("Gender", genres)

    widget_educational_level = st.selectbox(
        "Educational Level",
        educational_levels,
        format_func=lambda number: educational_levels_text[number]
    )

    widget_area_formation = st.selectbox("Training area", area_formation)

    widget_distance_home = st.slider(
        "Distance from home", **columns_slider_min_max["DistanceFromHome"]
    )

with st.container(border=True):
    st.write("### Routine at company")

    column_left, column_right = st.columns(2)

    with column_left:
        widget_department = st.selectbox("Department", departments)
        widget_travel_business = st.selectbox("Business Travel", travel_business)

    with column_right:
        widget_position = st.selectbox(
            "Position",
            sorted(df[df["Department"] == widget_department]["JobRole"].unique())
        )
    
        widget_overtime = st.radio("Overtime", overtime)

    widget_monthly_income = st.slider(
        "Monthly Income", **columns_slider_min_max["MonthlyIncome"]
    )

with st.container(border=True):
    st.write("### Professional experience")

    column_left, column_right = st.columns(2)

    with column_left:
        widget_companies_worked = st.slider(
            "Companies worked", **columns_slider_min_max["NumCompaniesWorked"]
        )
        widget_years_worked = st.slider(
            "Years worked", **columns_slider_min_max["TotalWorkingYears"]
        )
        widget_company_years = st.slider(
            "Years at Company", **columns_slider_min_max["YearsAtCompany"]
        )

    with column_right:
        widget_years_current_position = st.slider(
            "Years in Current Position", **columns_slider_min_max["YearsInCurrentRole"]
        )
        widget_years_same_manager = st.slider(
            "Years with the Same Manager", **columns_slider_min_max["YearsWithCurrManager"]
        )
        widget_years_last_promotion = st.slider(
            "Years Since Last Promotion", **columns_slider_min_max["YearsSinceLastPromotion"]
        )
        
with st.container(border=True):
    st.write("### Incentives and metrics")
    
    column_left, column_right = st.columns(2)

    with column_left:
        widget_job_satisfaction = st.selectbox(
            "Job Satisfaction",
            job_satisfaction,
            format_func=lambda number: satisfaction_levels_text[number],
        )

        widget_colleagues_satisfaction = st.selectbox(
            "Satisfaction with Colleagues",
            colleagues_satisfaction,
            format_func=lambda number: satisfaction_levels_text[number],
        )

        widget_work_involvement = st.selectbox(
            "Work Engagement", work_involvement
        )
        
    with column_right:
        widget_satisfaction_environment = st.selectbox(
            "Satisfaction with Environment",
            satisfaction_environment,
            format_func=lambda number: satisfaction_levels_text[number],
        )
        
        widget_work_life_balance = st.selectbox(
            "Work-Life Balance",
            life_work,
            format_func=lambda number: satisfaction_levels_text[number],
        )

        widget_option_actions = st.radio("Stock Option", option_actions)

    widget_salary_increase = st.slider(
        "Salary increase (%)",
        **columns_slider_min_max["PercentSalaryHike"]
    )
    
    widget_trainings_last_year = st.slider(
        "Trainings in the Last Year",
        **columns_slider_min_max["TrainingTimesLastYear"]
    )

input_model = {
    "Age": medians_columns_ignored["Age"],
    "BusinessTravel": widget_travel_business,
    "DailyRate": medians_columns_ignored["DailyRate"],
    "Department": widget_department,
    "DistanceFromHome": widget_distance_home,
    "Education": widget_educational_level,
    "EducationField": widget_area_formation,
    "EnvironmentSatisfaction": widget_satisfaction_environment,
    "Gender": widget_gender,
    "HourlyRate": medians_columns_ignored["HourlyRate"],
    "JobInvolvement": widget_work_involvement,
    "JobLevel": medians_columns_ignored["JobLevel"],
    "JobRole": widget_position,
    "JobSatisfaction": widget_satisfaction_environment,
    "MaritalStatus": "Single",
    "MonthlyIncome": widget_monthly_income,
    "MonthlyRate": medians_columns_ignored["MonthlyRate"],
    "NumCompaniesWorked": widget_companies_worked,
    "PerformanceRating": medians_columns_ignored["PerformanceRating"],
    "OverTime": widget_overtime,
    "PercentSalaryHike": widget_salary_increase,
    "RelationshipSatisfaction": widget_colleagues_satisfaction,
    "StockOptionLevel": widget_option_actions,
    "TotalWorkingYears": widget_years_worked,
    "TrainingTimesLastYear": widget_trainings_last_year,
    "WorkLifeBalance": widget_work_life_balance,
    "YearsAtCompany": widget_company_years,
    "YearsInCurrentRole": widget_years_current_position,
    "YearsSinceLastPromotion": widget_years_last_promotion,
    "YearsWithCurrManager": widget_years_same_manager,
}

df_input_model = pd.DataFrame([input_model])

forecast_button = st.button("Predict Friction")

if forecast_button:
    forecast = model.predict(df_input_model)[0]
    friction_probability = model.predict_proba(df_input_model)[0][1]

    color = ":red" if forecast == 1 else ":green"

    text_probability = (
        f"#### Friction Probability: {color}[{friction_probability:.1%}]"
    )
    friction_text = f"#### Friction: {color}[{'Yes' if forecast == 1 else 'No'}]"

    st.markdown(friction_text)
    st.markdown(text_probability)
