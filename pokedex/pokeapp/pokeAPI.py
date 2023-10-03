import requests

def get_pokeinfo(dex_num):
    url = "https://pokeapi.co/api/v2/pokemon/"+dex_num+"/"
    pokemon_data = requests.get(url, timeout=5)
    pokemon_data = pokemon_data.json()#jsonファイルを取得

    id=pokemon_data['id']
    height = pokemon_data['height']/10
    weight = pokemon_data['weight']/10

    spices=requests.get(pokemon_data['species']['url'], timeout=5).json()#日本語名で取得するためにさらにjsonを読み込む
    name=list(filter(lambda item : item['language']['name'] == 'ja',spices['names'] ))[0]['name']
    genus=list(filter(lambda item : item['language']['name'] == 'ja',spices['genera'] ))[0]['genus']
    explanations=list(filter(lambda item : item['language']['name'] == 'ja-Hrkt',spices['flavor_text_entries'] ))
    try:
        red_exp=explanations[7]['flavor_text'].split('\n')
    except:
        red_exp=explanations[0]['flavor_text'].split('\n')

    exp1=red_exp[0]
    exp2=red_exp[1]
    exp3=red_exp[2] 
    #green_exp=explanations[6]['flavor_text']
    #types=pokemon_data['types']
    #type1=types[0]['type']['name']

    #try:                               #2つ目のタイプがあるか確認し、なければハイフンにする
        #type2=types[1]['type']['name']
    #except:
        #type2='-'

    pic=pokemon_data['sprites']['versions']['generation-i']['red-blue']['front_default']

    #hp=pokemon_data['stats'][0]['base_stat']
    #attack=pokemon_data['stats'][1]['base_stat']
    #defence=pokemon_data['stats'][2]['base_stat']
    #special_attack=pokemon_data['stats'][3]['base_stat']
    #$special_defence=pokemon_data['stats'][4]['base_stat']
    #speed=pokemon_data['stats'][5]['base_stat']
    #total_stats=hp+attack+defence+special_attack+special_defence+speed

    request={'id':id,'name':name,'height':height,'weight':weight,'pic':pic,
             'genus':genus,'exp1':exp1,'exp2':exp2,'exp3':exp3}
    
    return request
    
