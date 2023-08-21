def div(t1, t2): 
    result = {}
    result["h"] = t1["h"] - t2["h"]
    result["m"] = t1["m"] - t2["m"]
    result["s"] = t1["s"] - t2["s"]
    result["d"] = t1["d"] - t2["d"]

    if result["s"] <  0:
        result["s"] += 60
        result["m"] -= 1


    if result["m"] < 0:
        result["m"] += 60
        result["h"] -= 1

    if result["h"] < 0:
        result["h"] += 24
        result["d"] -= 1


    return result


def show(r):
    print(f"{Result_time['h']} : {Result_time['m']} : {Result_time['s']}")

t1 = {"d":0, "h": 9, "m" : 25, "s": 35}
t2 = {"d": 0,"h": 7, "m": 35, "s": 20}


Result_time = div(t1 , t2)
show(Result_time)