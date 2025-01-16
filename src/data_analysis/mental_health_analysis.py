import plotly.express as px
from dash import dcc


def analyze_panic_attack_cases_by_anxiety_and_gender(df):
    title = "Amount of Panic Attack Cases by Anxiety Level and Gender"
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
        title=title,
        text_auto="avg"
    )
    fig.write_html(f"../views/{title}.html")
    return dcc.Graph(figure=fig)


def analyze_relation_between_anxiety_academic_year_and_cgpa(df):
    title = "Relationship Between Anxiety Level CGPA and the Academic Year"
    fig = px.sunburst(
        df,
        path=["Anxiety Label", "Academic Year", "CGPA"],
        color="Academic Year",
        color_discrete_sequence=px.colors.sequential.Agsunset_r,
        width=1600,
        height=900,
        title=title)
    fig.write_html(f"../views/{title}.html")
    return dcc.Graph(figure=fig)
