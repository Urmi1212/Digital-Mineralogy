import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Quartz':37.5435, 'K-feldspar':9.2736, 'Plagioclase':9.7701, 'Dolomite':0.3667, 'Magnesite':0.1752, 'Halloysite':3.2236, 'Dickite':0.132, 'Chlorite':0.1164, 'Serpentine':2.2743, 'Olivine':0.1185, 'Titanite':0.8694, 'Epidote':0.7077, 'Ilmenite':0.7838,	'Tourmaline':2.5091, 'Spinel':0.2516, 'Kerogen':3.0542, 'Pyroxene':2.834, 'Boehmite':0.0857, 'Hematite':0.3728, 'Chalcopyrite':0.3242, 'Natrite':0.7025, 'Nahcolite':0.7364, 'Organic matter':19.5873, 'Illite':0, 'Anhydrite':0, 'Muscovite':0, 'Opal':0, 'Mica (Tri)':0, 'Alunite':0, 'Calcite':0, 'Aragonite':0,	'Amphibole':0, 'Kaolinite':0, 'Ferrihydrite':0, 'Vermiculite':0, 'Smectite (Di)':0, 'Tephra':0, 'Carbon (%)':8.0634887, 'Horz_Position':1})

print(r.json())













