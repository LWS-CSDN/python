from flask import Flask,render_template,redirect

app=Flask(__name__)
app.config.from_object('settings.DevelopmentConfig')

@app.route('/index',methods=['GET','POST'])
def index():
    return ""

if __name__ == '__main__':
    app.run()