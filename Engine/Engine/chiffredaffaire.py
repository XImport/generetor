import sys


def ChiffreAffaireNet(cabrute, catransport):
    CaNet = []
    for (brute, transpo) in zip(cabrute, catransport):
        ca_net = brute - transpo
        CaNet.append(ca_net)
    return CaNet


def chiffreDaffaireCount(
    qtetonne, priceentonne, clients, clientsdb, qteenmetre3, priceenmetre3
):
    CA = []
    for (client, qtet, priceton, qteenm3, prixenm3) in zip(
        clients, qtetonne, priceentonne, qteenmetre3, priceenmetre3
    ):
        if client in clientsdb["Name"].to_list():
            client_index = clientsdb["Name"].to_list().index(client)
            client_unite = clientsdb.iloc[client_index][1]
            if client_unite == "T":
                CA.append(qtet * priceton)
            if client_unite == "M3":
                CA.append(qteenm3 * prixenm3)

        else:
            print(
                f"This Client That You Trying To Find His Product Price is Probably Missing Or Miswriting  [{client} ]  "
            )
            sys.exit()

    return CA
