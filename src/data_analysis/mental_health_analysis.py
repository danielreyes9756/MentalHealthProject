import plotly.express as px
from dash import dcc


def analyze_panic_attack_cases_by_anxiety_and_gender(df):
    df['Panic Attack Label'] = df['Panic Attack Label'].map({0: 'No', 1: 'Yes'})
    df['Anxiety Label'] = df['Anxiety Label'].map({0: 'No', 1: 'Yes'})
    fig = px.histogram(
        df,
        x="Panic Attack Label",
        color_discrete_sequence=px.colors.sequential.Agsunset_r,
        color="Gender",
        barmode="group",
        facet_col="Anxiety Label",
        labels={
            "Panic Attack Label": "Panic Attack Presence",
            "Anxiety Label": "Anxiety",
            "Gender": "Gender",
        },
        width=1600,
        height=900,
        title="Amount of Panic Attack Cases by Anxiety Level and Gender",
        text_auto="avg"
    )
    return dcc.Graph(figure=fig)


def analyze_relation_between_anxiety_academic_year_and_cgpa(df):
    fig = px.sunburst(
        df,
        path=["Anxiety Label", "Academic Year", "CGPA"],
        color="Academic Year",
        color_discrete_sequence=px.colors.sequential.Agsunset_r,
        width=1600,
        height=900,
        title="Relationship Between Anxiety Level CGPA and the Academic Year")
    return dcc.Graph(figure=fig)
