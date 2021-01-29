from flask import Flask
from flask import request, redirect

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def index():
    list = ['html', 'css']
    str = ''
    for i in list:
        str = f"<li><a href='{i}'>{i}</a></li>"
   
    if request.method == 'GET':
        print(request)
        print(request.args.get('id'))

    print(str)
    
    f = open('./public/template.html', 'r', encoding="utf8")
    template = f.read()
    f.close()
    return template.format('SSAC', str)


@app.route('/html')
def html():
    f = open('./public/template.html', 'r', encoding="utf8")
    template = f.read()
    f.close()
    return template.format('HTML ...')

@app.route('/css')
def css():
    f = open('./public/template.html', 'r', encoding="utf8")
    template = f.read()
    f.close()
    return template.format('CSS ...')

app.run(port=5001)
