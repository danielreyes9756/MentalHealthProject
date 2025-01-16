import plotly.express as px
from dash import dcc


def analyze_depression_distribution_by_age_and_gender(df):
    fig = px.box(
        df,
        x="Age",
        y="Depression Value",
        labels={'Age': 'Range Age'},
        color="Gender",
        color_discrete_sequence=px.colors.sequential.Viridis,
        title="Depression Distribution by Age Range and Gender",
        width=1600,
        height=900,
        category_orders={
            "Age": [
                "Below 18",
                "18-22",
                "23-26",
                "27-30",
                "Above 30"
            ]
        }
    )

    return dcc.Graph(figure=fig)


def analyze_depression_impact_by_trouble_sleep(df):
    response_map = {
        0: "Not at all",
        1: "Several days",
        2: "More than half the days",
        3: "Nearly every day"
    }
    df['Trouble Sleeping'] = df['Trouble Sleeping'].map(response_map)
    fig = px.violin(
        df,
        x='Trouble Sleeping',
        y='Depression Value',
        title="Impact of Trouble Sleeping on Depression",
        color='Trouble Sleeping',
        color_discrete_sequence=px.colors.sequential.Viridis,
        width=1600,
        height=900,
        category_orders={
            "Trouble Sleeping": [
                "Not at all",
                "Several days",
                "More than half the days",
                "Nearly every day"
            ]
        }
    )
    return dcc.Graph(figure=fig)


def analyze_depression_distribution_by_cgpa_range_and_gender(df):
    fig = px.box(
        df,
        x="Gender",
        y="Depression Value",
        color="CGPA",
        labels={"CGPA": "CGPA Range"},
        color_discrete_sequence=px.colors.sequential.Viridis,
        width=1600,
        height=900,
        title="Depression Distribution by CGPA Range and Gender",
        category_orders={
            "CGPA": [
                "Other",
                "Below 2.50",
                "2.50 - 2.99",
                "3.00 - 3.39",
                "3.40 - 3.79",
                "3.80 - 4.00",
            ]
        }
    )
    return dcc.Graph(figure=fig)


def analyze_relation_between_depression_feeling_tired_age_and_gender(df):
    response_map = {
        0: "Not at all",
        1: "Several days",
        2: "More than half the days",
        3: "Nearly every day"
    }

    df['Feeling Tired'] = df['Feeling Tired'].map(response_map)

    fig = px.sunburst(
        df,
        path=["Feeling Tired", "Age", "Gender"],
        color="Depression Value",
        width=1600,
        height=900,
        title="Relation between Depression, Feeling Tired, Age and Gender")
    return dcc.Graph(figure=fig)
