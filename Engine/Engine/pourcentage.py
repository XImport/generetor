def PourcentageFacturation(clients, canet, tablefac):
    CaFacture = []
    for (client, can) in zip(clients, canet):
        if client in tablefac["Name"].to_list():
            index = tablefac["Name"].to_list().index(client)
            CaFacture.append(can * tablefac.iloc[index][1])
    return CaFacture


def PourcentageNonFacturation(caNet, caFact):
    CaNonFacture = []
    for (net, fac) in zip(caNet, caFact):
        CaNonFacture.append(net - fac)
    return CaNonFacture
