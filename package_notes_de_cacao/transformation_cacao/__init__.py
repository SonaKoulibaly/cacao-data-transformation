"""
Package transformation_cacao
----------------------------
Transformations post-scraping pour le dataset Cacao.

Expose:
- transform_cacao(df): pipeline haut niveau de transformation.
"""

from .pipeline import transform_cacao

__all__ = ["transform_cacao"]
