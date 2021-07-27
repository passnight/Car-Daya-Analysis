import datetime
def dateRange(beginDate, endDate):
    dateList = []
    date = beginDate
    while date.__le__(endDate):
        dateList.append(date)
        if date.month < 12:
            date = datetime.datetime(date.year,date.month+1,date.day)
        else:
            date = datetime.datetime(date.year+1,1,date.day)
    return dateList

dateList=dateRange(datetime.datetime.strptime('2017-8', '%Y-%m'),datetime.datetime.strptime('2021-8', '%Y-%m'))
print (dateList)