# authors.py

from typing import List
import pandas as pd
from newplot.py import load_authors, load_languages, load_metadata

def list_authors(by_languages: bool = True, alias: bool = True) -> List[str]:
    """
    Lists Project Gutenberg author aliases in order of translation count.
    
    Returns:
        list: A list of author aliases, ordered by translation count.
    """
    # Load data
    authors = load_authors()
    languages = load_languages()
    metadata = load_metadata()

    if by_languages and alias:
        # Merge metadata and language data
        merged_data = metadata.merge(languages, on='gutenberg_id', how='left')
        
        # Clean data
        merged_data = merged_data.drop_duplicates().sort_values(by='gutenberg_id').reset_index(drop=True).dropna()
        merged_data['gutenberg_id'] = merged_data['gutenberg_id'].astype(int)

        # Merge with authors data
        merged_data_2 = merged_data.merge(authors, on='gutenberg_author_id', how='left')
        
        # Calculate total translations per alias
        alias_translation_count = merged_data_2.groupby('alias')['language'].nunique().reset_index()
        alias_translation_count.rename(columns={'language': 'translation_count'}, inplace=True)
        
        # Sort by the number of translations
        alias_translation_count_sorted = alias_translation_count.sort_values(by='translation_count', ascending=False)
        
        # Clean and return the author aliases
        author_aliases = [str(alias) for alias in alias_translation_count_sorted['alias'] if pd.notna(alias) and str(alias).strip()]
        return author_aliases
    else:
        return []
