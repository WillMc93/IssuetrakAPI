import IssuetrakAPI

key = IssuetrakAPI.read_api_key('api.key')['apiv1']
url = 'https://harbert.issuetrak.com/api/v1'
api = IssuetrakAPI.IssuetrakAPI(key, url)

r = api.perform_get('users')
print(r)
print(r.status_code)
