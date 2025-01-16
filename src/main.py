import dash
from dash import html

from data_analysis.figshare_depression_analysis import analyze_depression_distribution_by_age_and_gender, \
    analyze_relation_between_depression_feeling_tired_age_and_gender,\
    analyze_depression_impact_by_trouble_sleep,\
    analyze_depression_distribution_by_cgpa_range_and_gender

from data_analysis.student_depression_analysis import analyze_depression_by_financial_stress_and_sleep_duration,\
    analyze_depression_by_age_dietary_and_distribution
from data_analysis.mental_health_analysis import analyze_panic_attack_cases_by_anxiety_and_gender,\
    analyze_relation_between_anxiety_academic_year_and_cgpa

from data_setup.depression_figshare_setup import setup_figshare_depression
from data_setup.student_drepression_setup import setup_student_depression
from data_setup.mental_health_setup import setup_mental_health

app = dash.Dash(__name__)


def render_graphs():
    graphs = []

    # Figshare Depression Analysis
    print('-' * 40 + 'Depression Figshare' + 40 * '-')
    df_figshare_depression = setup_figshare_depression()
    graphs.append(analyze_depression_distribution_by_age_and_gender(df_figshare_depression))
    graphs.append(analyze_depression_impact_by_trouble_sleep(df_figshare_depression))
    graphs.append(analyze_depression_distribution_by_cgpa_range_and_gender(df_figshare_depression))
    graphs.append(analyze_relation_between_depression_feeling_tired_age_and_gender(df_figshare_depression))
    print('-' * 100 + '\n')

    # Mental Health Analysis
    print('-' * 40 + 'Student Depression' + 40 * '-')
    df_mental_health = setup_mental_health()
    graphs.append(analyze_panic_attack_cases_by_anxiety_and_gender(df_mental_health))
    graphs.append(analyze_relation_between_anxiety_academic_year_and_cgpa(df_mental_health))
    print('-' * 100 + '\n')

    # Student Depression Analysis
    print('-' * 40 + 'Mental Health' + 40 * '-')
    df_student_depression = setup_student_depression()
    graphs.append(analyze_depression_by_age_dietary_and_distribution(df_student_depression))
    graphs.append(analyze_depression_by_financial_stress_and_sleep_duration(df_student_depression))
    print('-' * 100 + '\n')
    return graphs


app.layout = html.Div(children=[
    html.H1("Mental Health Analysis Dashboard"),
    *render_graphs()
])


if __name__ == "__main__":
    app.run_server(debug=True)
