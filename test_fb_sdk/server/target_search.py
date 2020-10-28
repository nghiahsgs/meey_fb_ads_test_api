
# Targeting Search
#https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-search
# {
# "data":[
#     {
#         "id":"<TARGETING_OPTION_ ID>",
#         "current_status":"NON-DELIVERABLE"
#     },
#     {
#         "id":"<TARGETING_OPTION_ID>",
#         "current_status":"NON-DELIVERABLE",
#         "future_plan":[
#             {
#             "key":"2018-05-10T00:00:00+0000",
#             "value":"DEPRECATING"
#             }
#         ]
#     }
# ]

# url = 'https://graph.facebook.com/<API_VERSION>/search'
# 'type=targetingoptionstatus'
# 'targeting_option_list=[<TARGETING_OPTION_ ID>,<TARGETING_OPTION_ID>]'


# Geographic
# url = 'https://graph.facebook.com/%s/search?location_types=["country"]&type=adgeolocation&q=un&access_token=%s'%(graph_api_version,access_token)
# print(url)

# {
# key: "BA", => quan trong
# name: "Bosnia and Herzegovina",
# type: "country",
# country_code: "BA",
# country_name: "Bosnia and Herzegovina",
# supports_region: false,
# supports_city: true
# },


url = 'https://graph.facebook.com/%s/search?location_types=["city"]&type=adgeolocation&q=Manhattan&access_token=%s'%(graph_api_version,access_token)
# print(url)
# {
# key: "2481740",
# name: "Manhattan",
# type: "city",
# country_code: "US",
# country_name: "United States",
# region: "Nevada",
# region_id: 3871,
# supports_region: true,
# supports_city: true #co ho tro target thanh pho nay ko
# },


# curl -G \
#   -d 'location_types=["zip"]' \
#   -d 'type=adgeolocation' \
#   -d 'q=9' \
#   -d 'access_token=<ACCESS_TOKEN>' \
#   https://graph.facebook.com/v2.11/search

url = 'https://graph.facebook.com/v2.11/search?location_types=["zip"]&type=adgeolocation&q=9&access_token=%s'%access_token
# print(url)
# key: "GB:BD24 9",
# name: "BD24 9",
# type: "zip",
# country_code: "GB",
# country_name: "United Kingdom",
# region: "England",
# region_id: 4079,
# primary_city: "Settle, North Yorkshire",
# primary_city_id: 815818,
# supports_region: true,
# supports_city: true
# },


# curl -G \
#   -d 'latitude=37.449478' \
#   -d 'longitude=-122.173016' \
#   -d 'type=adradiussuggestion' \
#   -d 'access_token=<ACCESS_TOKEN>' \
#   https://graph.facebook.com/v<API_VERSION>/search
url = 'https://graph.facebook.com/v8.0/search?latitude=37.449478&longitude=-122.173016&type=adradiussuggestion&access_token=%s'%access_token
# print(url)


#Interests
# curl -G \
#   -d 'type=adinterest' \
#   -d 'q=baseball' \
#   -d 'access_token=<ACCESS_TOKEN>' \
#   https://graph.facebook.com/v<API_VERSION>/search

url = 'https://graph.facebook.com/%s/search?type=adinterest&q=baseball&access_token=%s'%(graph_api_version,access_token)
# print(url)
# {
# id: "6003087413192",
# name: "Baseball",
# audience_size: 530276610,
# path: [
# "Interests",
# "Sports and outdoors",
# "Sports",
# "Baseball"
# ],
# description: "",
# topic: "Sports and outdoors"
# },


#Interest Suggestions
# curl -G \
#   -d 'interest_list=["Basketball"]' \
#   -d 'type=adinterestsuggestion' \
#   -d 'access_token=<ACCESS_TOKEN>' \
url = 'https://graph.facebook.com/%s/search?interest_list=["Basketball"]&type=adinterestsuggestion&access_token=%s'%(graph_api_version, access_token)
# print(url)


# curl -G \
#   -d 'interest_list=["Japan","nonexistantkeyword"]' \
#   -d 'type=adinterestvalid' \
#   -d 'access_token=<ACCESS_TOKEN>' \
#   https://graph.facebook.com/v<API_VERSION>/search
# url = 'https://graph.facebook.com/%s/search?interest_list=["Japan","nonexistantkeyword"]&type=adinterestvalid&access_token=%s'(graph_api_version, access_token)
# print(url)


#Behaviors
# curl -G \
#   -d 'type=adTargetingCategory' \
#   -d 'class=behaviors' \
#   -d 'access_token=<ACCESS_TOKEN>' \
#   https://graph.facebook.com/v<API_VERSION>/search

url = 'https://graph.facebook.com/%s/search?type=adTargetingCategory&class=behaviors&access_token=%s'%(graph_api_version, access_token)
# print(url)


#Demographics
# curl -G \
#   -d 'type=adeducationschool' \
#   -d 'q=ha' \
#   -d 'access_token=<ACCESS_TOKEN>' \
#   https://graph.facebook.com/v<API_VERSION>/search



