"""
Module features : sécurisation et filtres simples.
"""

import pandas as pd

def clip_rating(df: pd.DataFrame, min_val: float = 1.0, max_val: float = 5.0) -> pd.DataFrame:
    """
    Tronque les valeurs de Rating hors de [min_val, max_val].

    Parameters
    ----------
    df : pd.DataFrame
    min_val : float
    max_val : float

    Returns
    -------
    pd.DataFrame
        DataFrame avec Rating borné.
    """
    df = df.copy()
    if "Rating" in df.columns:
        df["Rating"] = df["Rating"].clip(lower=min_val, upper=max_val)
    return df


def drop_rows_with_key_nans(df: pd.DataFrame) -> pd.DataFrame:
    """
    Supprime les lignes ayant des NaN sur colonnes clés disponibles.

    Colonnes clés considérées (si présentes): Company, BeanOrigin, Rating, CocoaPercent

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        DataFrame filtré.
    """
    keys = [c for c in ("Company", "BeanOrigin", "Rating", "CocoaPercent") if c in df.columns]
    if not keys:
        return df
    return df.dropna(subset=keys)
