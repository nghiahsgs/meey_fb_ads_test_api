import requests


graph_api_version = 'v8.0'
app_id = '358408568699788'
app_secret = '70e465c562e7c7ce1f97b12dc620a30a'

def convert_to_long_live_token(token):
    url = 'https://graph.facebook.com/%s/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s'%(graph_api_version,app_id,app_secret,token)
    # print(url)
    data = requests.get(url).json()
    # print(data)
    access_token = data['access_token']
    # print(access_token)
    return access_token

def get_list_bm(access_token):
    url = 'https://graph.facebook.com/%s/me/businesses?access_token=%s'%(graph_api_version,access_token)
    data = requests.get(url).json()
    return data

def get_ad_accounts(access_token,bm_id):
    url = 'https://graph.facebook.com/%s/%s/owned_ad_accounts?access_token=%s'%(graph_api_version,bm_id,access_token)
    # print(url)
    data = requests.get(url).json()
    return data


if __name__ =="__main__":
    # token = 'EAAFFZBH9rZB4wBABKZB5Y54A3TzsZBJxL81VB3EKy6KPKLAqROy6PZANplr7D8ZApPvhtqHFwE4NpoxyZAq3vBZBFhYQcpfuvwFbWHLCglXBvhjt1qh02ucdkTKqg3JXQd6TzFsk3hX1hiXbwZCUxO2ZCzBOjKZCre82v0UIX0QmkH2LSzTooZBSbEiD47TjRYEVWRGOYUvCM2MfMgZDZD'
    # access_token = convert_to_long_live_token(token)
    # print(access_token)
    access_token = 'EAAFFZBH9rZB4wBALzsZBZBL9OwQ5iitVJTD2ZBfF2vk85aZB2GQl4NZBTm3SlumvkAJyZAygugL2q8h8eiNFWcN1crLpgL99X7fpes1EjF179gU5kr0ZBvbJZCeATHAmyMYGgk4MOdBzbClalJ4ZCZAScndfbmFGMg93Pmk0IHNwGQCwvQZDZD'
    bm_id = '357782781672762'
    data = get_ad_accounts(access_token,bm_id)
    print(data)