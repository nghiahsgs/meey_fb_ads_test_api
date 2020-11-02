import requests


graph_api_version = 'v8.0'
app_id = '358408568699788'
app_secret = '70e465c562e7c7ce1f97b12dc620a30a'
access_token = 'EAAFFZBH9rZB4wBALzsZBZBL9OwQ5iitVJTD2ZBfF2vk85aZB2GQl4NZBTm3SlumvkAJyZAygugL2q8h8eiNFWcN1crLpgL99X7fpes1EjF179gU5kr0ZBvbJZCeATHAmyMYGgk4MOdBzbClalJ4ZCZAScndfbmFGMg93Pmk0IHNwGQCwvQZDZD'

# man hinh login
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


# man hinh tao quang cao step 1
def get_all_page_of_account(access_token):
    url = 'https://graph.facebook.com/%s/me?fields=name,accounts&access_token=%s'%(graph_api_version,access_token)
    data = requests.get(url).json()
    return data['accounts']


#man hinh tao quang cao step 2 (tao doi tuong, ie. target)



# 1 so api choi choi

#BM API
## get people trong 1 bm
# type_user = 'business_users'
# type_user = 'system_users'
type_user = 'pending_users'

bm_id = '357782781672762'
url = "https://graph.facebook.com/%s/%s/%s?access_token=%s"%(graph_api_version,bm_id,type_user,access_token)
data = requests.get(url).json()
print(data)



if __name__ =="__main__":
    # token = 'EAAFFZBH9rZB4wBABKZB5Y54A3TzsZBJxL81VB3EKy6KPKLAqROy6PZANplr7D8ZApPvhtqHFwE4NpoxyZAq3vBZBFhYQcpfuvwFbWHLCglXBvhjt1qh02ucdkTKqg3JXQd6TzFsk3hX1hiXbwZCUxO2ZCzBOjKZCre82v0UIX0QmkH2LSzTooZBSbEiD47TjRYEVWRGOYUvCM2MfMgZDZD'
    # access_token = convert_to_long_live_token(token)
    # print(access_token)
    access_token = 'EAAFFZBH9rZB4wBALzsZBZBL9OwQ5iitVJTD2ZBfF2vk85aZB2GQl4NZBTm3SlumvkAJyZAygugL2q8h8eiNFWcN1crLpgL99X7fpes1EjF179gU5kr0ZBvbJZCeATHAmyMYGgk4MOdBzbClalJ4ZCZAScndfbmFGMg93Pmk0IHNwGQCwvQZDZD'
    url = "https://graph.facebook.com/v8.0/me?fields=id,name,accounts&access_token=%s"%access_token

    # token page
    # EAAFFZBH9rZB4wBANRV8koLajCKcSbDFWZBpajJZAlWYiRZB48fcyCEwEGWEReQOlKZBuuJ5j9D7plgjZBw2AX0tlS85ZActYrh9ApXX0QbJoHdtr1RmmFTcmTqCtuW5eueEph5oSuApNZAVlSJ0mFORl5xsNbYooUhSF3NzH4j7ChWZBHveZAVcZCO63

    # get all post in one page
    # https://graph.facebook.com/v8.0/me?fields=id,name,feed&access_token=EAAFFZBH9rZB4wBAFLI4PTt1tP8cWxaLF9hTkcznPhxCnVcylILu82qRfZAJepJDsdTXeVrGDi1oaGPINZBWjUdLIbUw6JRQFF8zNJkBVYGQA1WFBc9iHwby13hRTj3nqls0XxMhFl6cc5KLt5tXad48HDhVl5T4MYyPVmGKy1ZCZBRzOKSCgaf

    #get detail one page
    # https://graph.facebook.com/v8.0/106219194277553_114323280133811?fields=message,likes,comments&access_token=EAAFFZBH9rZB4wBAFLI4PTt1tP8cWxaLF9hTkcznPhxCnVcylILu82qRfZAJepJDsdTXeVrGDi1oaGPINZBWjUdLIbUw6JRQFF8zNJkBVYGQA1WFBc9iHwby13hRTj3nqls0XxMhFl6cc5KLt5tXad48HDhVl5T4MYyPVmGKy1ZCZBRzOKSCgaf

