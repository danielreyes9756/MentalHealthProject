from src.data_analysis.common_data_analysis import print_basic_insights
from src.data_loading.load_data import load_csv
from src.data_processing.normalize_columns import clean_figshare_depression_columns
from src.encoding.encoder import encode_columns


def setup_figshare_depression():
    # Load data
    df = load_csv("../data/Depression.csv")

    print_basic_insights(df, 'Depression Figshare Dataset')

    # Normalize column names
    column_mapping = {
        "1. Age": "Age",
        "2. Gender": "Gender",
        "3. University": "University",
        "4. Department": "Department",
        "5. Academic Year": "Academic Year",
        "6. Current CGPA": "CGPA",
        "7. Did you receive a waiver or scholarship at your university?": "Scholarship Waiver",
    }
    clean_figshare_depression_columns(df, column_mapping)

    # Encode data
    columns = ['Depression Label', 'Scholarship Waiver']
    encode_columns(df, columns)

    print_basic_insights(df, 'Depression Figshare Dataset', True)

    return df
