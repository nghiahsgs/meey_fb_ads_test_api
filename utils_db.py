from peewee import *
# from utils import *
import requests
import json
import datetime

host='45.77.36.114'
db_name = 'meey_fb_ads'
db_user='nghiahsgs4'
db_pass='261997'

db = MySQLDatabase(db_name,host=host, user=db_user, passwd=db_pass)


class Target_interest(Model):
    name_en = CharField()
    name_vi= CharField()
    id_api= CharField()
    id_cha= IntegerField()
    lv= IntegerField()
    class Meta:
        database=db

def create_table_Target_interest():
    token = 'EAAFFZBH9rZB4wBALzsZBZBL9OwQ5iitVJTD2ZBfF2vk85aZB2GQl4NZBTm3SlumvkAJyZAygugL2q8h8eiNFWcN1crLpgL99X7fpes1EjF179gU5kr0ZBvbJZCeATHAmyMYGgk4MOdBzbClalJ4ZCZAScndfbmFGMg93Pmk0IHNwGQCwvQZDZD'
    url = 'https://graph.facebook.com/v8.0/search?type=adTargetingCategory&class=interests&access_token=%s'%token
    data = requests.get(url).json()

    for ele in data['data']:
        id = ele['id']
        path = ele['path']
        print(path)
        # name = ele['name']
        # print(name)


        # if len(path)==2:
        #     #import cha
        #     # check if cha exist
        #     list_target = Target_interest.select().where(Target_interest.name_en == path[0])
        #     if not len(list_target):
        #         name_en = path[0]
        #         name_vi = ''#gg_translate(name_en)
        #         id_api= 0
        #         id_cha = 0 
        #         lv = 0
        #         instance = Target_interest(name_en = name_en,name_vi= name_vi,id_api= id_api,id_cha= id_cha,lv= lv)
        #         instance.save()
        #         id_cha = instance.id
        #     else:
        #         id_cha = list_target[0].id


        #     #import con
        #     name_en = path[1]
        #     name_vi = ''#gg_translate(name_en)
        #     id_api= ele['id']
        #     # id_cha = instance.id
        #     lv = 1
        #     instance = Target_interest(name_en = name_en,name_vi= name_vi,id_api= id_api,id_cha= id_cha,lv= lv)
        #     instance.save()

        if len(path)==3:
            #bo qua ong noi, tim xem cha o dau
            list_target = Target_interest.select().where(Target_interest.name_en == path[1])
            if len(list_target):
                id_cha = list_target[0].id
                #import con
                name_en = path[2]
                name_vi = ''#gg_translate(name_en)
                id_api= ele['id']
                # id_cha = instance.id
                lv = 2
                instance = Target_interest(name_en = name_en,name_vi= name_vi,id_api= id_api,id_cha= id_cha,lv= lv)
                instance.save()
            else:
                print('ko thay')

if __name__=="__main__":
    Target_interest.create_table()
    create_table_Target_interest()