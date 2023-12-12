from flask import Flask, jsonify, render_template
import requests
from champion_data import latest_champ_data, full_champ_data

app = Flask(__name__)



# @app.route('/champion-champion-list')
# def get_champion_list():
#     url_for_champ_list = "https://ddragon.leagueoflegends.com/api/versions.json"
#     champ_list_response = requests.get(url_for_champ_list)
#     champion_list = []
#     if champ_list_response.status_code == 200:
#         versions = champ_list_response.json()
#         latest_version = versions[]
#         latest_champion_data_url = requests.get(latest_champion_data_url)
#         if latest_champion_data_response.status_code == 200:
#             aggregate_champ_data = 
#     champion_data = champion_list()
#     return jsonify(champion_data)
# if __name__ == '__main__':
#     app.run(debug=True)

# def fetch_champion_data_list():
#     full_champion_data_list = champion_data_list

#     return full_champion_data_list

# def latest_champ_data():


# def full_champ_data(champion_list):

@app.route('/')
def index():
    champion_list = latest_champ_data()
    champion_data_list = full_champ_data(champion_list)
    return render_template('base_champ_select.html', champion_data_list=champion_data_list)

@app.route('/champion/<champion_name>')
def get_champion(champion_name):
    champion_list = latest_champ_data()
    champion_data_list = full_champ_data(champion_list)
    champion_info = next ((champion for champion in champion_data_list if champion['name'] == champion_name), None)
    if champion_info:
        return jsonify(champion_info)
    else:
    # champion_list = latest_champ_data()
    # champion_data_list = full_champ_data(champion_list)
    # return jsonify({"champion_data_list": champion_data_list})
        return jsonify({"error": "Champion not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)