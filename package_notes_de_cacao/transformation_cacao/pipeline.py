"""
Pipeline global orchestrant les étapes de transformation cacao.
"""

import pandas as pd
from .nettoyage import strip_strings, drop_duplicates, standardize_columns
from .typage import fix_types
from .features import clip_rating, drop_rows_with_key_nans

def transform_cacao(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applique le pipeline de transformation.

    Étapes:
    1) Nettoyage texte (trim/espaces)
    2) Standardisation des noms de colonnes
    3) Conversion de types + CocoaFraction
    4) Clip de Rating dans [1, 5]
    5) Suppression des lignes NaN sur colonnes clés
    6) Suppression des doublons

    Parameters
    ----------
    df : pd.DataFrame
        Données brutes post-scraping (déjà extraites).

    Returns
    -------
    pd.DataFrame
        Données propres et typées, prêtes pour analyse.
    """
    df = strip_strings(df)
    df = standardize_columns(df)
    df = fix_types(df)
    df = clip_rating(df)
    df = drop_rows_with_key_nans(df)
    df = drop_duplicates(df)
    return df
