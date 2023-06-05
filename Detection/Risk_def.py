from time import localtime

# 도로형태 미고려 시
def calc_1(car, bus, truck, motor):
    risk = car*0.006 + bus*0.01 + (truck+motor)*0.018
    if (localtime().tm_hour >= 0 & localtime().tm_hour < 2):
        risk *= 1.5
    if (localtime().tm_hour >= 2 & localtime().tm_hour < 4):
        risk *= 2
    if (localtime().tm_hour >= 4 & localtime().tm_hour < 6):
        risk *= 3
    
    casualty = (car+bus+truck)*1.5 + motor*1.2

    return risk, casualty

road_list = ['터널안', '교차로내', '기타/불명', '교량위', '교차로횡단보도내', '고가도로위', '교차로부근', '지하차도내', '기타단일로']

# 도로형태 고려 시
def calc_2(car, bus, truck, motor, road):
    risk = car*0.006 + bus*0.01 + (truck+motor)*0.018
    if (localtime().tm_hour >= 0 & localtime().tm_hour < 2):
        risk *= 1.5
    if (localtime().tm_hour >= 2 & localtime().tm_hour < 4):
        risk *= 2
    if (localtime().tm_hour >= 4 & localtime().tm_hour < 6):
        risk *= 3
    if (road in ['고가도로위', '기타단일로', '터널안']):
        risk *= 2
    if (road in ['교량위', '교차로횡단보도내', '지하차도내']):
        risk *= 3

    casualty = (car+bus+truck)*1.5 + motor*1.2
    if (road == '기타/불명'):
        casualty *= 1.4
    if (road in ['교차로내', '교차로부근', '지하차도내', '기타단일로']):
        casualty *= 1.5
    if (road in ['교량위', '고가도로위']):
        casualty *= 1.6
    if (road == '터널안'):
        casualty *= 2
    
    return risk, casualty
