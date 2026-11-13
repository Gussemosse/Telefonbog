def valider_telefonnummer(nummer, laengde=8, fjern_mellemrum=True):
    # Konverter altid til string (hvis der f.eks. sendes et heltal)
    nummer = str(nummer)

    if fjern_mellemrum:
        nummer = "".join(nummer.split())

    if not nummer:
        return False
    if not nummer.isdigit():
        return False
    if len(nummer) != laengde:
        return False

    return True