import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .newplot import load_authors, load_metadata

def plot_translations(over='birth_century'):
    """
    Creates a Seaborn barplot showing the average translation count for authors
    grouped by a specified category (e.g., birth century).
    """
    # Load the data
    authors_df = load_authors()
    metadata_df = load_metadata()

    # --- Data Processing ---
    
    # Calculate the number of unique languages (translations) for each author
    translation_counts = metadata_df.groupby('gutenberg_author_id')['language'].nunique().reset_index()
    translation_counts.rename(columns={'language': 'translation_count'}, inplace=True)
    
    # Merge the translation counts with the authors' data
    df = pd.merge(authors_df, translation_counts, on='gutenberg_author_id')

    # Calculate the birth century:
    # We drop authors with no birthdate and then calculate the century
    df.dropna(subset=['birthdate'], inplace=True)
    df['birth_century'] = (df['birthdate'] // 100 * 100).astype(int)

    # --- Plotting ---
    
    # Create the barplot using Seaborn
    # Group by birth century and calculate average translation count
    plt.style.use('seaborn-whitegrid')
    plt.figure(figsize=(14, 8))
    ax = sns.barplot(data=df, x='birth_century', y='translation_count', palette='viridis', ci='sd')
    
    # Set plot titles and labels
    ax.set_title(
        'Average Number of Translations by Author\'s Birth Century',
        fontsize=16,
        fontweight='bold'
    )
    ax.set_xlabel('Birth Century', fontsize=12)
    ax.set_ylabel('Average Translation Count', fontsize=12)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()