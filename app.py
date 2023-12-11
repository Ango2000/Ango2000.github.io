from flask import Flask, render_template

from champion_data import champion_list

app = Flask(__name__)

@app.route('/')
def index ():
    return render_template('index.html', champion_list=champion_list)

if __name__ == '__main__':
    app.run(debug=True)