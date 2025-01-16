import plotly.express as px
from dash import dcc


def analyze_depression_by_age_dietary_and_distribution(df):
    title = "Depression Distribution by Age, Dietary Habits, and Gender"
    fig = px.violin(
        df,
        y="Age",
        x="Depression",
        color="Dietary Habits",
        box=True,
        title=title,
        category_orders={
            "Dietary Habits": [
                0,
                1,
                2,
                3
            ]
        },
        width=1600,
        height=900
    )
    fig.write_html(f"../views/{title}.html")
    return dcc.Graph(figure=fig)


def analyze_depression_by_financial_stress_and_sleep_duration(df):
    title = "Depression Analysis by Financial Stress and Sleep Duration"
    grouped_df = df.groupby(['Financial Stress', 'Depression', 'Sleep Duration']).size().reset_index(name='Count')
    fig = px.scatter_3d(
        grouped_df,
        x="Financial Stress",
        y="Sleep Duration",
        z="Count",
        color="Depression",
        size="Count",
        size_max=30,
        title=title,
        width=1600,
        height=900,
        category_orders={
            "Sleep Duration": [
                "Less than 5 hours",
                "5-6 hours",
                "7-8 hours",
                "More than 8 hours",
                "Others"
            ]
        }
    )
    fig.write_html(f"../views/{title}.html")
    return dcc.Graph(figure=fig)


