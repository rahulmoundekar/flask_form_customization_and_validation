from flask import Flask, render_template, redirect, flash, request
import os
from forms import StudentForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=('GET', 'POST'))
def contact():
    form = StudentForm()
    if request.method == 'POST' and form.validate_on_submit():
        print("saved")
        flash('Student Successfully saved!', "success")
        return render_template('index.html', form=form)
    print("not validate")
    return render_template('index.html', form=form)


# run always put in last statement or put after all @app.route
if __name__ == '__main__':
    app.run(host='localhost')
