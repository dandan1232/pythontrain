from flask import Flask ,render_template
from clean import get_data

app = Flask(__name__)

@app.route('pie',methods=['GET','POST'])
def pie():
    return render_template('pie.html');


@app.route('bar',methods=['GET','POST'])
def pie():
    return render_template('bar.html');





@app.route('piedata',methods=['GET','POST'])
def pie_data():
    return get_data.get_pie_data();


@app.route('bardata',methods=['GET','POST'])
def pie_data():
    return get_data.get_bar_data();



if __name__ == '__main__':
    app.run(debug=True,port='5000')
