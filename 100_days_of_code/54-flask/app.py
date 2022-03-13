from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    random_number = random.randint(1, 10)
    currYear = datetime.now().year
    return render_template('index.html', num=random_number, year=currYear)


if __name__ == '__main__':
    app.run()
