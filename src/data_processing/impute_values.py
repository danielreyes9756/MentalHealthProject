from sklearn.impute import SimpleImputer


def impute_data(df, columns, strategy):
    imputer = SimpleImputer(strategy=strategy)
    df[columns] = imputer.fit_transform(df[columns])
