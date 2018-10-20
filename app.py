from flask import Flask, url_for, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)
assets = Environment(app)

js = Bundle('js/plugins.js', 'js/main.js',
    filters='rjsmin', output='gen/packed.js')
assets.register('js_all', js)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/work/")
def portfolio():
    return render_template('work.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)