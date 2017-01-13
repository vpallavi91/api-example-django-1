import requests

def data_from_url(request,url, filter={}):
    '''
    MAIN FUNCTION TO GET DATA FROM DRCHRONO API
    '''
    data = []
    headers = {'Authorization': 'Bearer %s' %request.session['access_token'],}
    while url:
        page = requests.get(url, filter, headers=headers).json()
        data.extend(page['results'])
        url = page['next']
    return data
