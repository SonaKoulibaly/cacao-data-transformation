"""
Module nettoyage : utilitaires de nettoyage pour le dataset cacao.
"""

from typing import List
import pandas as pd

def strip_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoie les colonnes textuelles : trim + réduction des espaces multiples.

    Parameters
    ----------
    df : pd.DataFrame
        Données extraites en DataFrame.

    Returns
    -------
    pd.DataFrame
        Copie du DataFrame avec colonnes texte nettoyées.
    """
    df = df.copy()
    txt_cols: List[str] = df.select_dtypes(include=["object", "string"]).columns.tolist()
    for col in txt_cols:
        df[col] = (
            df[col]
            .astype("string")
            .str.replace(r"\s+", " ", regex=True)
            .str.strip()
        )
    return df


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Supprime les doublons exacts.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        DataFrame sans doublons.
    """
    return df.drop_duplicates()


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardise les noms de colonnes propres à ce dataset.

    Règles:
    - 'Origine spécifique du harirot' -> 'BeanOrigin'
    - 'CocoaPercentage'              -> 'CocoaPercent'

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        DataFrame avec colonnes renommées.
    """
    df = df.copy()
    mapping = {
        "Company": "Company",
        "Origine spécifique du harirot": "BeanOrigin",
        "Rating": "Rating",
        "CocoaPercentage": "CocoaPercent",
    }
    df.columns = [mapping.get(c, c) for c in df.columns]
    return df
