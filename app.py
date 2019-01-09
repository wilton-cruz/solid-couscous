from flask import Flask, url_for, render_template
from flask_assets import Environment, Bundle
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)
app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
assets = Environment(app)

js = Bundle('js/plugins.js', 'js/main.js',
    filters='rjsmin', output='gen/packed.js')
assets.register('js_all', js)

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])



@app.route("/contact/", methods=('GET', 'POST'))
def contact():
    form = MyForm()
    if form.validate_on_submit():
        return redirect("/seccess")
    return render_template('contact.html', form=form)

@app.route("/", methods=('GET', 'POST'))
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/work/")
def portfolio():
    return render_template('work.html')


if __name__ == '__main__':
    app.run(debug=True)