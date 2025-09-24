from typing import List
import pandas as pd
from newplot.py import authors, languages, metadata

    """
    It basically gets a list of Project Gutenberg author aliases sorted by the number of translations
    and returns a list of author aliases ordered by their translation count.
    """

def list_authors(by_languages: bool = True, alias: bool = True) -> List[str]:

    # Load the required datasets
    authors_data = authors()
    languages_data = languages()
    metadata_data = metadata()

    if by_languages and alias:
        # Combine the metadata and languages data
        combined_data = metadata_data.merge(languages_data, on='gutenberg_id', how='left')
        
        # Clean the data: remove duplicates, sort and reset the index, drop missing values
        combined_data = combined_data.drop_duplicates().sort_values(by='gutenberg_id').reset_index(drop=True).dropna()
        combined_data['gutenberg_id'] = combined_data['gutenberg_id'].astype(int)

        # Merge the cleaned data with authors data
        complete_data = combined_data.merge(authors_data, on='gutenberg_author_id', how='left')
        
        # Calculate the number of unique translations for each alias
        alias_translation_counts = complete_data.groupby('alias')['language'].nunique().reset_index()
        alias_translation_counts.rename(columns={'language': 'translation_count'}, inplace=True)
        
        # Sort aliases by translation count in descending order
        sorted_aliases = alias_translation_counts.sort_values(by='translation_count', ascending=False)
        
        # Clean up the aliases list, removing any invalid or empty aliases
        valid_aliases = [str(alias).strip() for alias in sorted_aliases['alias'] if pd.notna(alias) and str(alias).strip()]
        
        return valid_aliases
    else:
        return []
