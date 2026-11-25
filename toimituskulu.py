def toimituskulu(summa):
    """Palauta tilauksen toimituskulu euroina."""
    if summa >= 50:
        return 0.0
    return 4.90
