def clean_figshare_depression_columns(data, column_mapping):
    data.columns = data.columns.str.strip().str.replace(r"\s+", " ", regex=True)
    for col in data.columns:
        if "In a semester" in col:
            if "little interest" in col.lower():
                column_mapping[col] = "Little Interest"
            elif "feeling down" in col.lower():
                column_mapping[col] = "Feeling Down"
            elif "trouble falling" in col.lower():
                column_mapping[col] = "Trouble Sleeping"
            elif "feeling tired" in col.lower():
                column_mapping[col] = "Feeling Tired"
            elif "poor appetite" in col.lower():
                column_mapping[col] = "Appetite Issues"
            elif "feeling bad about yourself" in col.lower():
                column_mapping[col] = "Feeling Failure"
            elif "trouble concentrating" in col.lower():
                column_mapping[col] = "Trouble Concentrating"
            elif "moved or spoke too slowly" in col.lower():
                column_mapping[col] = "Restlessness"
            elif "thoughts that you would be better off dead" in col.lower():
                column_mapping[col] = "Suicidal Thoughts"

    clean_columns(data, column_mapping)


def clean_columns(data, column_mapping):
    data.rename(columns=column_mapping, inplace=True)
