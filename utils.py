from googletrans import Translator
from utils_db import *
import io

def gg_translate(str_input):
    translator = Translator()
    return translator.translate(str_input, src="en",dest='vi').text

def write_file_line(file_name,line):
    f = io.open(file_name,mode='a')
    f.write('%s\n'%line)
    f.close()

def create_data_list_interest():
    #list ong noi
    list_target_interest_lv_0 = Target_interest.select().where(Target_interest.id_cha == 0)
    for target_interest_lv_0 in list_target_interest_lv_0:
        line = target_interest_lv_0.name_en
        write_file_line('interst.txt',line)

        #list cha
        list_target_interest_lv_1 = Target_interest.select().where(Target_interest.id_cha == target_interest_lv_0.id)
        for target_interest_lv_1 in list_target_interest_lv_1:
            line = '---'+target_interest_lv_1.name_en
            write_file_line('interst.txt',line)
            
            #list con 
            list_target_interest_lv_2 = Target_interest.select().where(Target_interest.id_cha == target_interest_lv_1.id)
            for target_interest_lv_2 in list_target_interest_lv_2:
                line = '------'+target_interest_lv_2.name_en
                write_file_line('interst.txt',line)

def get_all_interest_lv_0():
    list_target_interest_lv_0 = Target_interest.select().where(Target_interest.id_cha == 0)
    res = []
    for target_interest_lv_0 in list_target_interest_lv_0:
        d_dict = {}
        d_dict['id'] = target_interest_lv_0.id
        d_dict['name'] = target_interest_lv_0.name_en
        res.append(d_dict)
    return res

def get_all_interest_lv_1(id_cha):
    list_target_interest_lv_1 = Target_interest.select().where(Target_interest.id_cha ==id_cha)
    res = []
    for target_interest_lv_1 in list_target_interest_lv_1:
        d_dict = {}
        d_dict['id'] = target_interest_lv_1.id
        d_dict['name'] = target_interest_lv_1.name_en
        res.append(d_dict)
    return res

def get_all_interest_lv_2(id_cha):
    list_target_interest_lv_2 = Target_interest.select().where(Target_interest.id_cha == id_cha)
    res = []
    for target_interest_lv_2 in list_target_interest_lv_2:
        d_dict = {}
        d_dict['id'] = target_interest_lv_2.id
        d_dict['name'] = target_interest_lv_2.name_en
        res.append(d_dict)
    return res

if __name__ =="__main__":
    # create_data_list_interest()
    # res = get_all_interest_lv_0()
    # print(res)

    # res = get_all_interest_lv_1(id_cha = 296)
    # print(res)

    # res = get_all_interest_lv_2(id_cha=297)
    # print(res)