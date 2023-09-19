import requests

def get_pokeinfo(dex_num):
    url = "https://pokeapi.co/api/v2/pokemon/"+dex_num+"/"
    pokemon_data = requests.get(url, timeout=5)
    pokemon_data = pokemon_data.json()#jsonファイルを取得

    name = pokemon_data['name']
    height = pokemon_data['height']
    weight = pokemon_data['weight']

    types=pokemon_data['types']
    type1=types[0]['type']['name']

    try:                               #2つ目のタイプがあるか確認し、なければハイフンにする
        type2=types[1]['type']['name']
    except:
        type2='-'

    pokemon_data['sprites']['front_default']

    hp=pokemon_data['stats'][0]['base_stat']
    attack=pokemon_data['stats'][1]['base_stat']
    defence=pokemon_data['stats'][2]['base_stat']
    special_attack=pokemon_data['stats'][3]['base_stat']
    special_defence=pokemon_data['stats'][4]['base_stat']
    speed=pokemon_data['stats'][5]['base_stat']
    total_stats=hp+attack+defence+special_attack+special_defence+speed

    request={'name':name,'height':height,'weight':weight,'type1':type1,'type2':type2,
            'hp':hp,'attack':attack,'defence':defence,'special_attack':special_attack,'special_defence':special_defence,
            'speed':speed,'total_stats':total_stats}
    
    return request
    
