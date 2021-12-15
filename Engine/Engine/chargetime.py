
# import datetime
def ChargeTime(chargetime):
    chargeList = []
    # print(chargetime["Unnamed: 3"].astype(float))

    for charge in chargetime["Unnamed: 3"].to_list():
        # lol = int(datetime.timedelta(hours=charge.hour, minutes=charge.minute, seconds=charge.second).total_seconds())
        seconds = (charge.hour * 60 + charge.minute) * 60 + charge.second
        chargeList.append(seconds)
    return chargeList
    #      chargeList.append(ts)
    # return chargeList