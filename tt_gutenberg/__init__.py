'''
import pandas as pd

def load_authors() -> pd.DataFrame:
    """
    Loads authors data. This data must include at least 'gutenberg_author_id' and 'alias'
    """
    source = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    return pd.read_csv(source)

def load_languages() -> pd.DataFrame:
    """
    Loads languages data. This data must include at least 'gutenberg_author_id' and 'language'.
    """
    source = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
    return pd.read_csv(source)

def load_metadata() -> pd.DataFrame:
    """
    Loads metadata data. This data must include at least 'gutenberg_author_id' and 'gutenberg_id'.
    """
    source = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    return pd.read_csv(source)
'''