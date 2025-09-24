import pandas as pd

def authors() -> pd.DataFrame:
    source = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    return pd.read_csv(source)


def languages() -> pd.DataFrame:
    source = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
    return pd.read_csv(source)


def metadata() -> pd.DataFrame:
    source = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    return pd.read_csv(source)