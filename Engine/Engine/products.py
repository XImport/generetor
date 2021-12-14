def PdtTypes(products, products_db):
    pdtss = []
    for productt in products["Produit"].to_list():
        if productt in products_db["PRODUCTS"].to_list():
            product_index = products_db["PRODUCTS"].to_list().index(productt)

            pdtss.append(products_db.iloc[product_index][0])
        else:
            pass
    return pdtss


def TypesFilter(products, db_types_graves, db_types_nobles, db_types_steril):
    typess = []
    for product in products["Produit"].to_list():
        if product in db_types_graves.to_list():
            typess.append("Graves")

        elif product in db_types_nobles.to_list():
            typess.append("Nobles")
        elif product in db_types_steril.to_list():
            typess.append("Stérile")
        else:
            pass

    return typess
