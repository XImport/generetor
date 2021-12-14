import sys

# import string


def Transport(chantiers, db_transport):
    prix_transport = []
    for chantier in enumerate(chantiers["Destination"].to_list()):
        if chantier[1] != "DEPART":
            trans_obj = chantiers.iloc[chantier[0]]
            if trans_obj["Client"] in db_transport["SOCIETE"].to_list():
                index = db_transport["SOCIETE"].to_list().index(trans_obj["Client"])
                # if db_transport.iloc[index]["CHANTIER"] == trans_obj["Destination"]:
                if compare(
                    db_transport.iloc[index]["CHANTIER"], trans_obj["Destination"]
                ):
                    prix_transport.append(db_transport.iloc[index]["PRIX TRANSPORT"])
                else:
                    for i in range(len(db_transport["SOCIETE"].to_list())):
                        ++i
                        # if db_transport.iloc[i]["CHANTIER"] == trans_obj["Destination"]:
                        if compare(
                            db_transport.iloc[i]["CHANTIER"], trans_obj["Destination"]
                        ):
                            prix_transport.append(
                                db_transport.iloc[i]["PRIX TRANSPORT"]
                            )
            else:
                print("There is Something Worng in Tranport Section !!")
                sys.exit()
        if chantier[1] == "DEPART":
            prix_transport.append(0)
    return prix_transport


def compare(a, b):
    return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]


def ChiffreAffaireTransport(qtetonne, clients, clientsdb, qteenmetre3, pricetransport):
    CA = []
    for (client, qtet, qteenm3, pricetrans) in zip(
        clients, qtetonne, qteenmetre3, pricetransport
    ):
        if client in clientsdb["Name"].to_list():
            client_index = clientsdb["Name"].to_list().index(client)
            client_unite = clientsdb.iloc[client_index][1]
            if client_unite == "T":
                CA.append(qtet * pricetrans)
            if client_unite == "M3":
                CA.append(qteenm3 * pricetrans)
    return CA


def CoutTransport(
    chantiers,
    db_transport,
    qtetonne,
    clients,
    clientsdb,
    qteenmetre3,
    pricetransport,
):
    prix_transport = []
    for (chantier, client, qtet, qteenm3, pricetrans) in zip(
        enumerate(chantiers["Destination"].to_list()),
        clients,
        qtetonne,
        qteenmetre3,
        pricetransport,
    ):
        if chantier[1] != "DEPART":
            trans_obj = chantiers.iloc[chantier[0]]
            if trans_obj["Client"] in db_transport["SOCIETE"].to_list():
                index = db_transport["SOCIETE"].to_list().index(trans_obj["Client"])
                # if db_transport.iloc[index]["CHANTIER"] == trans_obj["Destination"]:
                if compare(
                    db_transport.iloc[index]["CHANTIER"], trans_obj["Destination"]
                ):

                    if client in clientsdb["Name"].to_list():
                        client_index = clientsdb["Name"].to_list().index(client)
                        client_unite = clientsdb.iloc[client_index][1]
                        if client_unite == "T":
                            prix_transport.append(
                                qtet * db_transport.iloc[index]["COUT TRANSPORT"]
                            )
                        if client_unite == "M3":
                            prix_transport.append(
                                qteenm3 * db_transport.iloc[index]["COUT TRANSPORT"]
                            )
                else:

                    if client in clientsdb["Name"].to_list():
                        client_index = clientsdb["Name"].to_list().index(client)
                        client_unite = clientsdb.iloc[client_index][1]
                        if client_unite == "T":

                            for i in range(len(db_transport["SOCIETE"].to_list())):
                                ++i
                                # if (
                                #     db_transport.iloc[i]["CHANTIER"]
                                #     == trans_obj["Destination"]
                                # ):
                                if compare(
                                    db_transport.iloc[i]["CHANTIER"],
                                    trans_obj["Destination"],
                                ):
                                    prix_transport.append(
                                        qtet * db_transport.iloc[i]["COUT TRANSPORT"]
                                    )

                        if client_unite == "M3":

                            for i in range(len(db_transport["SOCIETE"].to_list())):
                                ++i
                                # if (
                                #     db_transport.iloc[i]["CHANTIER"]
                                #     == trans_obj["Destination"]
                                # ):
                                if compare(
                                    db_transport.iloc[i]["CHANTIER"],
                                    trans_obj["Destination"],
                                ):
                                    prix_transport.append(
                                        qteenm3 * db_transport.iloc[i]["COUT TRANSPORT"]
                                    )

            else:
                print("Please Add " + trans_obj["Client"] + "to the db file")
                sys.exit()
        else:
            prix_transport.append(" ")
    return prix_transport


def MargeTransport(catransport, couttransport):
    Marge = []
    for (CaT, CoutTrans) in zip(catransport, couttransport):
        try:
            Marge.append(float(CaT) - float(CoutTrans))
        except ValueError:
            Marge.append(0)
    any(n < 0 for n in Marge)
    if True:
        print("report generated successfully")
    return Marge
