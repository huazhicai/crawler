import pymongo
import xlwt
import csv

client = pymongo.MongoClient('localhost')
db = client.test
collection = db.ctrip4


def get_data():
    values = []
    for i, item in enumerate(collection.find()):
        values.append([item['aircraft_type'], item['start_time'], item['start_station_name'], item['arrive_time'],
                       item['arrive_station_name'], item['week_schedule'], item['punctuality'], item['price']])
    return values


def write_excel_xls(path, sheet_name, value):
    index = len(value)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(sheet_name)
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])
    workbook.save(path)
    print('ok')


def write_csv(value):
    headers = ['aircraft_type', 'start_time', 'start_station_name', 'arrive_time', 'arrive_station_name', 'week_schedule',
               'punctuality', 'price']
    with open('test.csv', 'w')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(value)


if __name__ == '__main__':
    values = get_data()
    write_excel_xls('ctrip_air.xls', 'aircraft', values)
