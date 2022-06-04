def validation_data(data1:str, data2:str) ->bool:
    if data2 !=None:
        if len(data1) == 0 or len(data2) == 0:
            return False
        if len(data1) >= 100 or len(data2) >= 100:
            return False
        return True
    else :
        if len(data1) == 0:
            return False
        if len(data1) >= 100:
            return False
        return True
