from flask import Flask,render_template,redirect,request

app=Flask(__name__)

@app.route('/index',methods=['GET','POST'])

def index():
    #请求相关
    # 请求相关信息
    #常用的
    # request.method
    # request.args
    # request.form
    # request.cookies
    # request.headers
    # request.path
    # request.files
    # obj = request.files['the_file_name']
    # obj.save('/var/www/uploads/' + secure_filename(f.filename))

    #不常用的
    # request.values
    # request.full_path
    # request.script_root
    # request.url
    # request.base_url
    # request.url_root
    # request.host_url
    # request.host


    #响应相关
    return ""
    return json.dumps({})#return jsonify()
    return render_template('index.html',n1=123)
    return redirect('/index')

    # response = make_response(render_template('index.html'))
    # response是flask.wrappers.Response类型
    # response.delete_cookie('key')
    # response.set_cookie('key', 'value')
    # response.headers['X-Something'] = 'A value'
    # return response

if __name__ == '__main__':
    app.run()