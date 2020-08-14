from flask import Flask,request, render_template
from predictor import predict, train_model, get_data

app = Flask(__name__, static_url_path='/static')

data_predict = {
    'max_floor': 0,
    'floor': 0,
    'square': 0.0,
    'kitchen': 0.0,
    'station': '',
    'time': 0
}

@app.route('/', methods=['post', 'get'])
# def main():
#     msg = '0'
#     thanks = False
#     training_set = {}
#     improve = False
#     if request.method == 'POST':
#         get_data(data_predict , request)
#         if (request.form.keys()):
#             msg = predict(data_predict)
#             if msg == -1:
#                 msg = ['NO SUCH STATION EXISTS']
#             else:
#                 improve = True
#             print('predicting')
#         else:
#             training_set = data_predict.copy()
#             training_set['price'] = request.form.get('price')
#             train()
#             thanks = True
#             improve = True
#             print('training')
#         print(request.form)
#     return render_template('index.html', msg=msg, improve = improve, thanks = thanks)

def main():
    msg = '0'
    thanks = False
    training_set = {}
    improve = False
    if request.method == 'POST':
        get_data(data_predict, request)
        if msg != -1:
            msg = predict(data_predict)
            if msg == -1:
                msg = ['NO SUCH STATION EXISTS']
            else:
                improve = True
        print(request.form)
    return render_template('index.html', msg=str(msg) + ' rub.', improve = improve, thanks = thanks)

@app.route('/train', methods=['post', 'get'])
def train():
    thanks = False
    if request.method == "POST":
        get_data(data_predict, request)
        data_predict['price'] = int(request.form.get('price'))
        thanks = True
        if not train_model(data_predict):
            thanks = True
        
    return render_template('train.html', thanks = thanks)

@app.route('/about')
def about():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
