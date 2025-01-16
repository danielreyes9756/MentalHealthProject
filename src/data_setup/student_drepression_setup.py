from src.data_analysis.common_data_analysis import print_basic_insights
from src.data_loading.load_data import load_csv
from src.data_processing.impute_values import impute_data
from src.data_processing.normalize_columns import clean_columns
from src.encoding.encoder import encode_columns


def setup_student_depression():
    # Load data
    df = load_csv("../data/Student Depression Dataset.csv")

    print_basic_insights(df, 'Student Depression Dataset')

    # Normalize column names
    column_mapping = {
        "Have you ever had suicidal thoughts ?": "Suicidal Thoughts"
    }
    clean_columns(df, column_mapping)

    # Impute values by using mean
    impute_data(df, ["Financial Stress"], "mean")

    columns = ['Suicidal Thoughts', 'Family History of Mental Illness', 'Dietary Habits']
    encode_columns(df, columns)

    print_basic_insights(df, 'Student Depression Dataset', True)

    return df
