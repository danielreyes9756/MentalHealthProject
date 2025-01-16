from sklearn.preprocessing import LabelEncoder


def encode_columns(df, columns):
    """
    Codificar la columna 'Depression Label' en valores numéricos.
    """
    encoder = LabelEncoder()
    for col in columns:
        df[col] = encoder.fit_transform(df[col])
