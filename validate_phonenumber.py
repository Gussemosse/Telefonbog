def valider_telefonnummer(nummer, laengde=8, fjern_mellemrum=True):

    if fjern_mellemrum:
        nummer = "".join(nummer.split())

    if nummer == "":
        return False
    if not nummer.isdigit():
        return False
    if len(nummer) != laengde:
        return False

    return True