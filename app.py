from flask import Flask, render_template
from calc import calculate_statistics

app = Flask(__name__)

@app.route('/')
def index():
    stats = calculate_statistics()
    print(stats)
    return render_template('index.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)