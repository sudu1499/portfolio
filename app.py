from flask import Flask,request,render_template,url_for,redirect

app=Flask(__name__)
@app.route('/')
def portfolio():
    return render_template('portfolio.html')
if __name__=='__main__':
    app.run(debug=True)
