
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/book/<int:id>')
def book_detail(id):
    return render_template('book_detail.html', book_id=id)

@app.route('/admin')
def admin_panel():
    return render_template('admin_panel.html')

if __name__ == '__main__':
    app.run(debug=True)
