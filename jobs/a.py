import requests
base_url = 'https://www.thecolorapi.com/id?'
params = 'rgb=255,100,200'

def job_a():
    
    r = requests.get(base_url + params)

    if r.ok:
        data = r.json()
        val = data['name']['value']  # should be "Hot Pink"
        print(val)
        return val
    else:
        print('request failed, status: ', r.status_code)