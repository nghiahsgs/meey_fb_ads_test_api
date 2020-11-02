from googletrans import Translator
from utils_db import *

def gg_translate(str_input):
    translator = Translator()
    return translator.translate(str_input, src="en",dest='vi').text

#list ong noi
list_target_interest_lv_0 = Target_interest.select().where(Target_interest.id_cha == 0)
# for