from src.data_analysis.common_data_analysis import print_basic_insights
from src.data_loading.load_data import load_csv
from src.data_processing.normalize_columns import clean_columns
from src.encoding.encoder import encode_columns


def setup_mental_health():
    # Load data
    df = load_csv("../data/Student Mental health.csv")

    print_basic_insights(df, 'Mental Health Dataset')

    # Normalize column names
    column_mapping = {
        "What is your course?": "Suicidal Thoughts",
        "Choose your gender": "Gender",
        "Your current year of Study": "Academic Year",
        "What is your CGPA?": "CGPA",
        "Do you have Depression?": "Depression Label",
        "Do you have Anxiety?": "Anxiety Label",
        "Do you have Panic attack?": "Panic Attack Label",
        "Did you seek any specialist for a treatment?": "Treatment Label"
    }
    clean_columns(df, column_mapping)

    # Drop rows with na - justification: it's just one row in this case
    df = df.dropna(subset=["Age"])

    # Encode data in this case {yes, no} fields
    columns = ['Marital status', 'Depression Label', 'Anxiety Label', 'Panic Attack Label', 'Treatment Label']
    encode_columns(df, columns)

    print_basic_insights(df, 'Mental Health Dataset', True)

    return df
