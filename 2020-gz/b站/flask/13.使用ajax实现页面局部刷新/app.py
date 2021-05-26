from flask import Flask
from flask import request
from flask import render_template

app=Flask(__name__)



@app.route('/ajax',methods=["get","post"])
def hello_world():
    name=request.values.get("name")
    score=request.values.get("score")
    print(f'name:{name},score:{score}')
    return "10000"

@app.route('/tem')
def hello_world3():
    return render_template('index.html')



if __name__=='__main__':
    app.run()