import requests
from django.shortcuts import render
from django.http import JsonResponse



def lisboa_view(request):
    # Endpoint da API do IPMA para a previsão do tempo
    url_previsao_lisboa= 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    tipo_tempo_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'



    lisboa_previsao_response = requests.get(url_previsao_lisboa)
    tipo_tempo_response = requests.get(tipo_tempo_url)

    tipo_tempo_dados = tipo_tempo_response.json()
    lisboa_previsao_dados = lisboa_previsao_response.json()


    hoje_lisboa = lisboa_previsao_dados['data'][0]
    cidade = 'Lisboa'
    t_min = hoje_lisboa['tMin']
    t_max = hoje_lisboa['tMax']
    data = hoje_lisboa['forecastDate']

    id_tempo = hoje_lisboa['idWeatherType']

    descricao_tempo = None
    for item in tipo_tempo_dados['data']:
        if item['idWeatherType'] == id_tempo:
            descricao_tempo = item['descWeatherTypePT']
            break

    icone_animado =  f'meteo/w_ic_d_{id_tempo:02}anim.svg'

    context = {
        'cidade': cidade,
        't_min': t_min,
        't_max': t_max,
        'data': data,
        'descricao_tempo': descricao_tempo,
        'icone_animated': icone_animado,
    }

    return render(request, 'meteo/lisboa.html', context)


def view_cinco_dias(request):
    url_cidade = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cidade_response = requests.get(url_cidade)
    dados_cidades = cidade_response.json()
    lista_cidades = dados_cidades["data"]

    forecasts = []

    cidade_escolhida = None
    id_cidade = None

    if request.method == 'POST':
        cidade_escolhida = request.POST.get('cidade_escolhida')

    if cidade_escolhida:
        for cidade in lista_cidades:
            if cidade['local'] == cidade_escolhida:
                id_cidade = cidade['globalIdLocal']
                break

    if id_cidade:
        url_previsao = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{id_cidade}.json'
        tipo_tempo_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

        previsao_response = requests.get(url_previsao)
        tipo_tempo_response = requests.get(tipo_tempo_url)

        tipo_tempo_dados = tipo_tempo_response.json()
        previsao_dados = previsao_response.json()

        weather_type_dict = {item['idWeatherType']: item['descWeatherTypePT'] for item in tipo_tempo_dados['data']}

        for previsao in previsao_dados['data']:
            forecast = {
                'date': previsao['forecastDate'],
                'tMin': previsao['tMin'],
                'tMax': previsao['tMax'],
                'icon': f'meteo/w_ic_d_{previsao["idWeatherType"]:02d}anim.svg',
                'description': weather_type_dict.get(previsao['idWeatherType'], 'No description available')
            }
            forecasts.append(forecast)

    context = {
        'cidades': lista_cidades,
        'cidade':cidade_escolhida,
        'previsoes': forecasts,
    }

    return render(request, 'meteo/cinco_dias.html', context)


