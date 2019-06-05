from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/left_page')
def left_page():
    return render_template('left_page.html')


@app.route('/right_page')
def rigth_page():
    return render_template('right_page.html')

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry! No response. Try again.'

if __name__ == "__main__":
    app.run(debug=True)