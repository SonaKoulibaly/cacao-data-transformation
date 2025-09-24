"""
Module typage : conversions de types et colonnes dérivées.
"""

import pandas as pd

def fix_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convertit les colonnes au bon type et crée CocoaFraction.

    Règles:
    - Rating -> float
    - CocoaPercent -> float (strip '%')
    - CocoaFraction = CocoaPercent / 100
    - Company, BeanOrigin -> category (si présentes)

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        DataFrame avec types corrigés et feature dérivée.
    """
    df = df.copy()

    if "Rating" in df.columns:
        df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

    if "CocoaPercent" in df.columns:
        df["CocoaPercent"] = (
            df["CocoaPercent"]
            .astype("string")
            .str.replace("%", "", regex=False)
            .str.strip()
        )
        df["CocoaPercent"] = pd.to_numeric(df["CocoaPercent"], errors="coerce")
        df["CocoaFraction"] = df["CocoaPercent"] / 100.0

    for col in ("Company", "BeanOrigin"):
        if col in df.columns:
            df[col] = df[col].astype("category")

    return df
