from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)



# @app.route('/rgb/<ip>',methods=['GET', 'POST'])
# def rgbLight(ip):
#     key = request.values['key']
#     print('key='+key+',ip:'+ip)






