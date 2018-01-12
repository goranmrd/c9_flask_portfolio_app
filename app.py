from flask import Flask, render_template, request, redirect, send_file
import datetime
import pytz # timezone 
import requests
import os
import random
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import prettyplotlib as ppl
import matplotlib.pyplot as plt


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	return render_template('index.html', name=name)


@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      total = 0
  	      try:
  	      	for str_num in request.form['text'].split():
  	      		total += int(str_num)
  	      	return render_template('add_numbers.html', result=str(total))
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! 2 numbers with a space between them please"


@app.route('/converter', methods=['GET','POST'])
def converter_post():
          if request.method == 'GET':
              return render_template('converter.html')
          elif request.method == 'POST':
              meters = 0.0
              try:
                value = float(request.form['text'])                                     
                meters = (0.3048 * value * 10000.0 + 0.5) / 10000.0
                return render_template('converter.html', result=str('{:0.4f}'.format(meters)))
              except ValueError:
                print("Please enter numbers only")

@app.route('/pass_gen', methods=['GET','POST'])
def pass_gen_post():
          if request.method == 'GET':
              return render_template('pass_gen.html')
          elif request.method == 'POST':
              nums = []
              try:
                names = ''
                number = int(request.form['number'])
                if number == 1:
                  names = 'YOUR PASSWORD ='
                elif number == 0:
                  names = 'PLEASE ENTER NUMBER >= 1'
                else:
                  names = 'YOUR PASSWORDS ='
                value = int(request.form['text'])
                chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                
                for i in range(number):
                  passwd = "".join(random.sample(chars, value))
                  nums.append(passwd)
                return render_template('pass_gen.html', result=nums, names=names)
              except ValueError:
                print("Please enter numbers only")
                
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)

@app.route('/fig/')
def fig():
    fig, ax = plt.subplots(1)
    ppl.bar(ax, np.arange(10), np.abs(np.random.randn(10)))
    canvas = FigureCanvas(fig)
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


@app.route('/image/')
def images():
    return render_template("image.html")


@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')

@app.route('/M_Learning')
def machine_learning_page():
	# testing stuff
	return render_template('M_Learning.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')

app.run(host=os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
	app.run(debug=False)
