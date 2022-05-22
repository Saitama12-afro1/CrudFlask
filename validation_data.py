def validation_data(data1, data2):
    if data2 !=None:
        if (len(data1) or len(data2)) == 0:
            return False
        if (len(data1) or len(data2)) >= 100:
            return False
        return True
    else :
        if len(data1) == 0:
            return False
        if len(data1) >= 100:
            return False
        return True



    