# https://developers.facebook.com/docs/business-sdk/getting-started


from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount #abstract object

my_app_id = '358408568699788'
my_app_secret = '70e465c562e7c7ce1f97b12dc620a30a'
my_access_token = 'EAAFFZBH9rZB4wBALzsZBZBL9OwQ5iitVJTD2ZBfF2vk85aZB2GQl4NZBTm3SlumvkAJyZAygugL2q8h8eiNFWcN1crLpgL99X7fpes1EjF179gU5kr0ZBvbJZCeATHAmyMYGgk4MOdBzbClalJ4ZCZAScndfbmFGMg93Pmk0IHNwGQCwvQZDZD'
ads_account_id = 'act_559010095051592'

#get all camps
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount(ads_account_id)
campaigns = my_account.get_campaigns()
print(campaigns)

