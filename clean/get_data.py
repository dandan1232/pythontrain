import pandas
import numpy
import json
import sqlalchemy


def get_pie_data():
    engine = sqlalchemy.create_engine("mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata")
    sql = "select * from book"
    data_frame = pandas.read_sql(sql=sql, con=engine)
    names = data_frame['name'].values
    value = data_frame['value'].values

    json_array = []
    for i in range(0, names.__len__()):
        json_array.append({'name': names, 'value': value})
    json_data_array = {
        'pie_data': json_array
    }
    json_string = json.dumps(json_data_array, ensure_ascii=False)
    return json_string


def get_bar_data():
    engine = sqlalchemy.create_engine("mysql+pymysql://root:ldd123789dd@localhost:3306/bigdata")
    sql = "select * from book1"
    data_frame = pandas.read_sql_table(sql=sql, con=engine)
    xvalues = data_frame['name'].values
    yvalues = data_frame['value'].values

    json_data = {
        'xvalues': xvalues.tolist(),
        'yvalues': yvalues.tolist(),
    }
    json_string = json.dumps(json_data, ensure_ascii=False)
    return json_string
