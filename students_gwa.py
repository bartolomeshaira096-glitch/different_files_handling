def get_latin_honor(gwa):
    if gwa <= 1.20:
        return "Summa Cum Laude"
    elif gwa <= 1.45:
        return "Magna Cum Laude"
    elif gwa <= 1.75:
        return "Cum Laude"
    else:
        return "No Latin Honor"