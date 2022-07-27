import requests
base_url = 'https://www.thecolorapi.com/id?'
params = 'rgb=20,40,60'

def job_b():
    
    r = requests.get(base_url + params)

    if r.ok:
        data = r.json()
        val = data['name']['value']  # should be "Big Stone"
        print(val)
        return val
    else:
        print('request failed, status: ', r.status_code)