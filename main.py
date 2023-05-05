from flask import Flask, redirect,render_template,request


app=Flask(__name__)

@app.route('/')
def input():
    return render_template('main.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result=dict()
        result['이름'] = request.form.get('name')
        result['학번'] = request.form.get('StudentNumber')
        result['전공'] = request.form.get('major')
        result['이메일'] = request.form.get('email_id')+"@"+request.form.get('email_addr')
        result['성별'] = request.form.get('gender')
        result['프로그래밍 언어'] = request.form.get('languages')
        sorted_result = dict(sorted(result.items(), key=lambda x: x[1]))
        return render_template('result.html', result=sorted_result)
    
@app.route('/add_row', methods=['POST'])
def add_row():
    if request.method == 'POST':
        return redirect('/')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)