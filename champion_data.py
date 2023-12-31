# copy pasted code from LOL_final_Project repository 

import json
import requests

# with open ('keys.json', 'r') as config_file:
#     config = json.load(config_file)


def latest_champ_data():
    url_for_champ_list = "https://ddragon.leagueoflegends.com/api/versions.json"
    # "https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/champion.json"

    champ_list_response = requests.get(url_for_champ_list)

    champion_list = []
    if champ_list_response.status_code == 200:
        """
        finds the latest version/patch of the aggregate champion data
        """
        # champion_list = []
        # aggregate_champ_list = champ_list_response.json()
        versions = champ_list_response.json()
        latest_version = versions[0]
        latest_champion_data_url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/champion.json"
        latest_champion_data_response = requests.get(latest_champion_data_url)
        if latest_champion_data_response.status_code == 200:
            """
            takes the json file that contains all basic champion data in the game and stores it 
            """
            aggregate_champ_data = latest_champion_data_response.json()
            champ_data_temp = aggregate_champ_data["data"]
            print(champion_list)
            for champ in champ_data_temp.values():
                """
                it iterates through the stored data to pull the id which is the champ's name
                that is used when accessing champion specific json files
                """
                champion_list.append(champ["id"])
    else:
        print("Unable to pull champion data")
    return champion_list
# latest_champ_data()

# def extract_first_id(champion_data):
#     base_url = "https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/champion/"
#     first_ids = []
#     for champ in champion_lists:
#         champion_url = f"{base_url}{champ}.json"
#         response = requests.get(champion_url)
#         if response.status_code == 200:
#             data = response.json()
#             first_champion_key = list(data['data'].keys())[0]
#             first_champion_data = data['data'][first_champion_key]
#             first_champion_id = first_champion_data['id']
#             first_ids.append(first_champion_id)
#         else:
#             first_ids.append(None)
#     return first_ids
#     first_id = next(iter(champion_data['id'].values()))
#     return first_id

def full_champ_data(champion_list):
    base_url = "https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/champion/"

    champion_data_list = []
    for champ in champion_list:
        """
        takes the base url and inserts the champion id from champion_list 
        """
        champion_url = f"{base_url}{champ}.json"
        response = requests.get(champion_url)

        if response.status_code == 200:
            """
            stores individual champ json data in champion_data
            """
            champion_data = response.json()
            # temp_champ_data = champion_data[champ]
            # first_id = temp_champ_data["data"]["id"]
            if champ in champion_data["data"]:
                """
                iterates through each individual champion json file and pulls specific data
                and appends that data into champion_data_list
                """
                temp_champ_data = champion_data["data"][champ]
                champion_info = {
                    "id": temp_champ_data["id"],
                    "name": temp_champ_data["name"],
                    "allytips": temp_champ_data.get("allytips", []),
                    "enemytips": temp_champ_data.get("enemytips", []),
                    "tags": temp_champ_data.get("tags", []),
                    "image_full": temp_champ_data["image"]["full"]
                }
                champion_data_list.append(champion_info)
            else:
                print(f"Unable to pull {champ} data")

        else:
            print(f"Unable to load {champ} data ")
    return champion_data_list
# full_champ_data()

def show_champ_data(champion_data_list):
    for champion_info in champion_data_list:
        """
        prints champion data in a formatted way for each champion
        """
        
        print("ID:", champion_info["id"])
        print("Champion Name:", champion_info["name"])
        print("Ally Tips:", champion_info["allytips"])
        print("Enemy Tips:", champion_info["enemytips"])
        print("Tags:", champion_info["tags"])
        print("Image:", champion_info["image_full"])
        # will need to add code where if a field is blank, it should print a statement
        # saying that there is no data on that field
# print (champion_list)

champion_list = latest_champ_data()
champion_data_list = full_champ_data(champion_list)
show_champ_data(champion_data_list)