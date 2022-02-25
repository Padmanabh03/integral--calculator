from flask import Flask,render_template,url_for,flash,request
from sympy import oo,Symbol,integrate

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def index():
    z = ''
    if request.method == 'POST' and 'upper-bound' in request.form and 'function' in request.form and 'lower-bound' in request.form:
        fun = request.form['function']
        a = request.form['lower-bound']
        b = request.form['upper-bound']

        a1 = a.replace('-infinity', '-oo')
        b1 = b.replace('infinity', 'oo')

        x = Symbol("x")
        if (a == '-infinity' and b == 'infinity'):
            z = integrate(fun, (x, a1, b1))
        elif (a == '-infinity'):
            z = integrate(fun, (x, a1, b))
        elif (b == 'infinity'):
            z = integrate(fun, (x, a, b1))
        else:
            z = integrate(fun, (x, a, b))
        #print(z)
        return render_template("index.html", a=a ,b=b,fun=fun,z=z)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
