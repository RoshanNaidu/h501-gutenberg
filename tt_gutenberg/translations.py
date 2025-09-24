import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .newplot import authors, metadata


    """
    Here it would visualize the average number of translations per author, grouped by a specific attribute, such as birth century.
    The function calculates the unique language count for each author, merges the data with author information, 
    and then creates a bar plot for visualization.
    """

def plot_author_translations(group_by='birth_century'):

    # Retrieve the authors and metadata dataframes
    authors_data = authors()
    metadata_data = metadata()

    # Data Preparation
    
    # Determine the number of distinct languages (translations) per author
    author_translation_count = metadata_data.groupby('gutenberg_author_id')['language'].nunique().reset_index()
    author_translation_count.rename(columns={'language': 'translation_count'}, inplace=True)
    
    # Merge the translation count data with the author's information
    merged_data = pd.merge(authors_data, author_translation_count, on='gutenberg_author_id')

    # Drop rows with missing birthdate and compute the birth century
    merged_data = merged_data.dropna(subset=['birthdate'])
    merged_data['birth_century'] = (merged_data['birthdate'] // 100) * 100

    # Visualization Part
    
    # Set the style for the plot
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(14, 8))
    
    # Create a barplot of the average translation counts, grouped by the selected category
    plot_ax = sns.barplot(
        data=merged_data, 
        x=group_by, 
        y='translation_count', 
        palette='viridis', 
        ci='sd'
    )

    # Customize the plot's appearance with labels and title
    plot_ax.set_title(
        f'Average Translations by Author\'s {group_by.replace("_", " ").title()}',
        fontsize=16,
        fontweight='bold'
    )
    plot_ax.set_xlabel(group_by.replace("_", " ").title(), fontsize=12)
    plot_ax.set_ylabel('Average Translation Count', fontsize=12)
    
    # Adjust x-axis labels for clarity
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
