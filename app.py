from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os
import random
from string import ascii_lowercase



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


@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              
              shop_list.append(item)

              
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in shop_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
         
@app.route('/piglatin', methods=['GET','POST'])
def pig_latin_post():
          if request.method == 'GET':
                return render_template('piglatin.html')
          elif request.method == 'POST':
                allletters = list(ascii_lowercase)
		consonants = allletters
		vowels = ['a', 'e', 'i', 'o', "u"]
		vowelchoose = ["way", "yay", "ay"]
		newword = []
		wordlist = []
		for i in consonants:
		       for j in vowels:
			      if i == j:
				     consonants.remove(i)

		item = request.form['text'].split()
		for word in item:
		       if word.isalpha():
			      wordlistvowels = list(word)
			      wordlist = list(word)
			      if wordlistvowels[0] in vowels:
				     choose = random.choice(vowelchoose)
				     print(word + choose)
				     finalword = word + choose
				     print(finalword)
				     return render_template('piglatin.html', result=finalword)
			      else:
				     for m in wordlistvowels:
					    if m in vowels:
						   break
					    elif m in consonants:
						   newword.append(m)
						   wordlist.remove(m)
						   continue
					    else:
						   pass
				     wordlist.extend(newword)
				     new = "".join(wordlist)
				     print(new + "ay")
				     finalword = new + "ay"
				     print(finalword)

				     return render_template('piglatin.html', result=finalword)

@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          for item in request.form['text'].split():
            answer = (datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime('Time = ' + '%H:%M:%S' + ' IST ' + ' Date = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')

              
              
            return render_template('time.html', result=answer)

         

@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')

app.run(host=os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
	app.run(debug=False)
