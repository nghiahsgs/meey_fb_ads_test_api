# target audience
# https://docs.google.com/spreadsheets/d/1VUoe_PXtsRfT_7SQH5UhbHy6BzN4xY1XXHadbswkbBA/edit#gid=0

import requests
import io


def write_file_line(file_name,line):
    f = io.open(file_name,mode='a')
    f.write('%s\n'%line)
    f.close()



type_class = 'user_os'
token = 'EAAFFZBH9rZB4wBALzsZBZBL9OwQ5iitVJTD2ZBfF2vk85aZB2GQl4NZBTm3SlumvkAJyZAygugL2q8h8eiNFWcN1crLpgL99X7fpes1EjF179gU5kr0ZBvbJZCeATHAmyMYGgk4MOdBzbClalJ4ZCZAScndfbmFGMg93Pmk0IHNwGQCwvQZDZD'
url = 'https://graph.facebook.com/v8.0/search?type=adTargetingCategory&class=%s&access_token=%s'%(type_class,token)
data = requests.get(url).json()

# len(data['data'])

# for ele in data['data']:
#     id = ele['id']
#     path = ele['path']
#     print(path)
    
#     line = '"%s","'%id
#     line += '","'.join(path)
#     line += '"'

#     write_file_line('%s.csv'%type_class,line)

# type_class = 'user_device'
# for ele in data['data']:
#     name = ele['name']
#     description = ele['description']
#     platform = ele['platform']
#     audience_size = ele['audience_size']
#     type = ele['type']

#     line = '%s,%s,%s,%s,%s'%(name,description,platform,audience_size,type)
    
#     write_file_line('%s.csv'%type_class,line)

# for ele in data['data']:
#     name = ele['type']
#     description = ele['name']
#     platform = ele['platform']
#     audience_size = ele['description']
    

#     line = '%s,%s,%s,%s,%s'%(name,description,platform,audience_size,type)
    
#     write_file_line('%s.csv'%type_class,line)
