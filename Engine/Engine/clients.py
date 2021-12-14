def ClientwithM3(clients, clientsdb, products):
    # if this algorithm sucks it means you should add your new clients to the database
    clients_with_m3 = []
    for (client, product) in zip(clients, products):
        if client in clientsdb["Name"].to_list():
            client_index = clientsdb["Name"].to_list().index(client)
            client_unite = clientsdb.iloc[client_index][1]

            # print(client,":::", ":::",product, ":::",clientsdb.iloc[client_index][2:][product])
            if client_unite == "M3":
                clients_with_m3.append(clientsdb.iloc[client_index][2:][product])
            elif client_unite == "T":
                clients_with_m3.append(" ")
    # print(clientsdb.iloc[1][2:])

    return clients_with_m3


def Clientwithtonne(clients, clientsdb, products):
    # if this algorithm sucks it means you should add your new clients to the database
    clients_with_tonne = []

    for (client, product) in zip(clients, products):
        if client in clientsdb["Name"].to_list():
            client_index = clientsdb["Name"].to_list().index(client)
            client_unite = clientsdb.iloc[client_index][1]

            if client_unite == "T":

                clients_with_tonne.append(clientsdb.iloc[client_index][2:][product])
            elif client_unite == "M3":
                clients_with_tonne.append(" ")

    return clients_with_tonne


def Clients(bc, clients):
    globalClients = []
    for bc, client in zip(bc.to_list(), clients.to_list()):
        # if str(client).split()[1] == "MARCO":
        #     client = "CLIENTS AU COMPTANT"
        #     print(client)
        if bc == "EN ESPECE" or bc == "en espece":
            client = "CLIENTS AU COMPTANT"
            globalClients.append(client)

        elif str(client).split()[0] == "STE":
            clients2 = client.split()[1::]
            # print(str(client).split()[1])
            globalClients.append(listToString(clients2))

        else:
            globalClients.append(client)

    return globalClients


def listToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return str1.join(s)
