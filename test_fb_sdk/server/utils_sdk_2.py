# BM => tai khoan quang cao (ad Account) => 1 ad account => tao duọc nhieu camp
# 1 camp => nhieu ads set => 1 ads set nhieu ads (ads creative)
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.targetingsearch import TargetingSearch
from facebook_business.adobjects.targeting import Targeting
from facebook_business.adobjects.adimage import AdImage

# from facebookads.adobjects.adset import AdSet

import datetime

access_token = 'EAAFFZBH9rZB4wBALzsZBZBL9OwQ5iitVJTD2ZBfF2vk85aZB2GQl4NZBTm3SlumvkAJyZAygugL2q8h8eiNFWcN1crLpgL99X7fpes1EjF179gU5kr0ZBvbJZCeATHAmyMYGgk4MOdBzbClalJ4ZCZAScndfbmFGMg93Pmk0IHNwGQCwvQZDZD'
app_secret = '70e465c562e7c7ce1f97b12dc620a30a'
app_id = '358408568699788'
ad_account_id = 'act_559010095051592'
page_id = ''
graph_api_version = 'v8.0'

# FacebookAdsApi.init(access_token=access_token)
FacebookAdsApi.init(app_id, app_secret, access_token)

#0# create campain
# params = { 
#     'name': 'ENTER CAMPAIGN NAME HERE', 
#     'objective': 'POST_ENGAGEMENT', 
#     # 'status': 'ACTIVE',
#     'status': 'PAUSED',
#     'special_ad_categories':'NONE'
# }
# campaign_result = AdAccount(ad_account_id).create_campaign(params=params)

#1# create ad set (where we select: our targets and cost etc.)
''' Target
1. Đối tượng tùy chỉnh (chưa cần)

2. Các đối tượng thuộc vị trí
3. Độ tuổi
4. Giới tính
5. Nhắm đối tượng theo sở thích, hành vi, nhân khẩu học

'''
# adset = AdSet(parent_id=ad_account_id)
# adset.update({    
#     'name': 'ENTER ADSET NAME HERE',    
#     'campaign_id': campaign_result["id"],    
#     'daily_budget': 150,    
#     'billing_event': 'IMPRESSIONS',    
#     'optimization_goal': 'REACH',    
#     'bid_amount': 10,    
#     'targeting': {'geo_locations': {'countries': {'TR'}},      'publisher_platforms': 'facebook'},    
#     'start_time': 'ENTER START DATE HERE',    
#     'end_time': 'ENTER END DATE HERE',
# })
# adset.remote_create(params={'status': 'ACTIVE'})

#2# upload image to using for AD
# image = AdImage(parent_id=ad_account_id)
# image[AdImage.Field.filename] = 'messiGod.jpg'
# image.remote_create() 
# image_hash = image[AdImage.Field.hash]
image_hash = '5bb2c9016ce52eef24aa4359ce8de72d'

#3# create Ad creative
# fields = []
# params = {  
#     'name': 'ENTER CREATIVE NAME HERE',  
#     'object_story_spec': {'page_id':page_id,'link_data':{'image_hash':image_hash,'link':'ENTER FACEBOOK PAGE LINK-PAGE_ID HERE','message':'ENTER AD MESSAGE HERE'}},}
# adcreative = AdAccount(ad_account_id).create_ad_creative(fields=fields, params=params)

#4# create Ad
# fields = []
# params = {  
#     'name': 'ENTER AD NAME HERE',  
#     'adset_id': adset['id'],  
#     'creative': {'creative_id': adcreative['creative_id']},
#     'status': 'ACTIVE'}
# AdAccount(ad_account_id).create_ad(fields=fields, params=params)




# API TAGET: BASIC TARGETING (audience api facebook)
# Demographics and Events
#  Typically you get data to define targeting from Targeting Search, then specify options in Targeting Spec. 

#cai dat target o trong AdSet
# adset = AdSet(parent_id='act_<AD_ACCOUNT_ID>')
# adset.update({
#     AdSet.Field.name: 'My AdSet',
#     AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
#     AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
#     AdSet.Field.bid_amount: 150,
#     AdSet.Field.daily_budget: 2000,
#     AdSet.Field.campaign_id: <CAMPAIGN_ID>,
#     AdSet.Field.targeting: {
#         'geo_locations': {
#             'countries': ['US'],
#         },
#         'relationship_statuses': [2, 4],
#         'life_events': [
#             {
#                 'id': 6003054185372,
#                 'name': 'Recently Moved',
#             },
#         ],
#         'industries': [
#             {
#                 'id': 6009003307783,
#                 'name': 'Accounting and finance',
#             },
#         ],
#     },
# })
# adset.remote_create(params={
#     'status': AdSet.Status.active,
# })


# Location
# from facebook_business.adobjects.adaccount import AdAccount
# from facebook_business.adobjects.adset import AdSet
# from facebook_business.api import FacebookAdsApi

# access_token = '<ACCESS_TOKEN>'
# app_secret = '<APP_SECRET>'
# app_id = '<APP_ID>'
# id = '<AD_ACCOUNT_ID>'
# FacebookAdsApi.init(access_token=access_token)

# fields = [
# ]
# params = {
#   'name': 'My Reach Ad Set',
#   'optimization_goal': 'REACH',
#   'billing_event': 'IMPRESSIONS',
#   'bid_amount': '2',
#   'daily_budget': '1000',
#   'campaign_id': '<adCampaignLinkClicksID>',
#   'targeting': {'geo_locations':{'countries':['US']},'facebook_positions':['feed']},
#   'status': 'PAUSED',
#   'promoted_object': {'page_id':'<pageID>'},
# }
# print AdAccount(id).create_ad_set(
#   fields=fields,
#   params=params,
# )
# Interests
# Behaviors




# Search And Targeting
# To target males age 20-24 within 10 miles of Menlo Park, CA or living in Texas or in Japan:


# First, get Japan's country code
from facebookads.adobjects.targetingsearch import TargetingSearch
params = {
    'q': 'japan',
    'type': 'adgeolocation',
    'location_types': ['country'],
}

resp = TargetingSearch.search(params=params)
print(resp)

# Get Texas's region code:
# params = {
#     'q': 'texas',
#     'type': 'adgeolocation',
#     'location_types': ['region'],
# }

# resp = TargetingSearch.search(params=params)


# Search Menlo Park, CA city code:
# params = {
#     'q': 'menlo',
#     'type': 'adgeolocation',
#     'location_types': ['city'],
# }

# resp = TargetingSearch.search(params=params)

# from facebookads.adobjects.adset import AdSet
# from facebookads.adobjects.targeting import Targeting

# adset = AdSet(parent_id='act_<AD_ACCOUNT_ID>')
# adset.update({
#     AdSet.Field.name: 'My AdSet',
#     AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
#     AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
#     AdSet.Field.bid_amount: 150,
#     AdSet.Field.daily_budget: 2000,
#     AdSet.Field.campaign_id: <CAMPAIGN_ID>,
#     AdSet.Field.promoted_object: {'page_id': <PAGE_ID>},
#     AdSet.Field.targeting: {
#         Targeting.Field.geo_locations: {
#             'countries': ['JP'],
#             'regions': [
#                 {'key': '3886'},
#             ],
#             'cities': [
#                 {
#                     'key': '2420605',
#                     'radius': '10',
#                     'distance_unit': 'mile',
#                 },
#             ],
#         },
#         Targeting.Field.genders: [1],
#         Targeting.Field.age_min: 20,
#         Targeting.Field.age_max: 24,
#         Targeting.Field.publisher_platforms: ['facebook', 'audience_network'],
#         Targeting.Field.device_platforms: ['mobile'],
#     },
# })
# adset.remote_create(params={
#     'status': AdSet.Status.active,
# })


# from facebookads.adobjects.adaccount import AdAccount
# from facebookads.adobjects.adset import AdSet

# ad_account = AdAccount(fbid='act_<AD_ACCOUNT_ID>')

# params = {
#     AdSet.Field.name: 'My AdSet',
#     AdSet.Field.optimization_goal: AdSet.OptimizationGoal.reach,
#     AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
#     AdSet.Field.bid_amount: 150,
#     AdSet.Field.daily_budget: 2000,
#     AdSet.Field.campaign_id: <CAMPAIGN_ID>,
#     AdSet.Field.targeting: {
#         'geo_locations': {
#             'custom_locations': [
#                 {
#                     'custom_type': 'multi_city',
#                     'min_population': 500000,
#                     'max_population': 1000000,
#                     'country': 'BR',
#                 },
#                 {
#                     'custom_type': 'multi_city',
#                     'country_group': 'Europe',
#                 },
#             ],
#             'location_types': ['recent', 'home'],
#         },
#     },
#     AdSet.Field.status: AdSet.Status.active,
# }
# adset = ad_account.create_ad_set(params=params)


# Interest Targeting
# curl -G \
#   -d 'type=adinterest' \
#   -d 'q=soccer' \
#   -d 'access_token=<ACCESS_TOKEN>' \
#   https://graph.facebook.com/v2.11/search

# {
#     "targeting": {
#         "facebook_positions": [
#             "feed"
#         ],
#         "geo_locations": {
#             "countries": [
#                 "US"
#             ],
#             "regions": [
#                 {
#                     "key": "4081"
#                 }
#             ],
#             "cities": [
#                 {
#                     "key": 777934,
#                     "radius": 10,
#                     "distance_unit": "mile"
#                 }
#             ]
#         },
#         "genders": [
#             1
#         ],
#         "age_max": 24,
#         "age_min": 20,
#         "publisher_platforms": [
#             "facebook",
#             "audience_network"
#         ],
#         "device_platforms": [
#             "mobile"
#         ],
#         "flexible_spec": [
#             {
#                 "interests": [
#                     {
#                         "id": "<adsInterestID>",
#                         "name": "<adsInterestName>"
#                     }
#                 ]
#             }
#         ]
#     }
# }
