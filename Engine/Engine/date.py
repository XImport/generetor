import datetime
def DateHandler(doc):
    dates = []
    for date in doc["Date d'entrée"].to_list():
        try:
            date = (
                datetime.datetime.strptime(str(date), "%Y-%d-%m %H:%M:%S")
                .strftime("%d:%m:%Y %H-%M-%S")
                .replace(":", "/")
                .replace("00-00-00", "")
            )
        except:
            pass
        dates.append(date)
    return dates
