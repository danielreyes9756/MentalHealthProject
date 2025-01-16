import matplotlib.pyplot as plt


def print_basic_insights(df, df_name, is_cleaned=False):
    state = "after" if is_cleaned else "before"
    print(f"First rows of {df_name} {state} cleaning:")
    print(df.head())

    print(f"\nGeneral information about {df_name} {state} cleaning:")
    df.info()

    print(f"\nMissing values in {df_name} {state} cleaning:")
    print(df.isnull().sum())


def plot_boxplot(df, title_prefix="Boxplot of"):
    # Select numerical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

    for col in numerical_cols:
        plt.figure(figsize=(8, 6))
        plt.boxplot(df[col].dropna(), vert=True, patch_artist=True)
        plt.title(f"{title_prefix} {col}")
        plt.ylabel(col)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
