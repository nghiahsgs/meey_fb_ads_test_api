from utils import *
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)


access_token = 'EAAFFZBH9rZB4wBALzsZBZBL9OwQ5iitVJTD2ZBfF2vk85aZB2GQl4NZBTm3SlumvkAJyZAygugL2q8h8eiNFWcN1crLpgL99X7fpes1EjF179gU5kr0ZBvbJZCeATHAmyMYGgk4MOdBzbClalJ4ZCZAScndfbmFGMg93Pmk0IHNwGQCwvQZDZD'

@app.route('/list_bm', methods=['GET','POST'])
def list_bm():
    if request.method=="GET":
        list_bm = get_list_bm(access_token)
        return list_bm

@app.route('/list_ad_accounts/<bm_id>', methods=['GET','POST'])
def list_ad_accounts(bm_id):
    if request.method=="GET":
        data = get_ad_accounts(access_token,bm_id)
        return data

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3000)