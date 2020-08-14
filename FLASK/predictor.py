import lightgbm as lgb
import pandas as pd

def predict(data_predict):
    model = lgb.Booster(model_file='model')
    stations = pd.read_csv('stations.csv')
    try:
        data_predict['station'] = stations.loc[stations['Metro'] == data_predict['station']]['ind'].tolist()[0]
    except:
        return -1
    data = pd.DataFrame(data_predict, index=[0])
    price = model.predict(data)
    return price

def train():
    return 0

def get_data(data_predict, request):
    square = request.form.get('square')
    max_floor = request.form.get('max_floor')
    floor = request.form.get('floor')
    kitchen = request.form.get('kitchen')
    station = request.form.get('station')
    time = request.form.get('time')
    try:
        data_predict['square'] = float(square)
        data_predict['max_floor'] = int(max_floor)
        data_predict['floor'] = int(floor)
        data_predict['kitchen'] = float(kitchen)
        data_predict['time'] = int(time)
        data_predict['station'] = station.replace(' ', '')
    except ValueError:
        msg = -1