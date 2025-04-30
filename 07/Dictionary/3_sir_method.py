# Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.
def dict3():
    empdata = {(1,28):50000, (1,63):25000, (2,72):30000}
    depdata = {}
    for k, v in empdata.items():
        if k[0] not in depdata:
            depdata[k[0]] = {'max': v, 'min': v, 'total': v}
        else:
            if v > depdata[k[0]]['max']:
                depdata[k[0]]['max'] = v
            elif v < depdata[k[0]]['min']:
                depdata[k[0]]['min'] = v
            depdata[k[0]]['total'] += v
    print(depdata)

dict3()
