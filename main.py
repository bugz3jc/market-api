from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort
from flask_mysqldb import MySQL
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv(path)
app = Flask(__name__)
api = Api(app)

app.config['MYSQL_USER'] = os.getenv('DB_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('DB_PW')
app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_DB'] = os.getenv('DB_DB')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

cors = CORS(app, resources={r"/*": {"origins":"*"}})

class Product(Resource):
    def get(self, sku=None,category=None, search=None):        
        cur = mysql.connection.cursor()
        if(sku):
            cur.execute('''SELECT * FROM product WHERE sku = "{}" '''.format(sku))
        elif(category):
            cur.execute('''SELECT p.product_id, p.sku, p.image, p.name, p.price FROM product_category pc
	            LEFT JOIN product p ON p.product_id = pc.product_id
	            WHERE pc.category_id IN ({})'''.format(category))
        elif(search):
             cur.execute('''SELECT * FROM product WHERE name LIKE "%{}%" '''.format(search))

        else:
            cur.execute('''SELECT * FROM product''')

        result = cur.fetchall()
        return jsonify(result)
    
class Categories(Resource):
    def get(self, product_id=None):
        cur = mysql.connection.cursor()
        if(product_id):
            cur.execute('''SELECT c.* FROM product_category pc
                        LEFT JOIN category c ON c.category_id = pc.category_id
                        WHERE pc.product_id ={}'''.format(product_id))
        else:
            cur.execute('''SELECT * FROM category''')
        result = cur.fetchall()
        return jsonify(result)

class Test(Resource):
    def get(self):
        return {'error':'forbidden access'}

api.add_resource(Product,"/product/list","/product/sku/<string:sku>","/product/category/<int:category>","/product/search/<string:search>")
api.add_resource(Categories,"/category/list","/category/product/<int:product_id>")
api.add_resource(Test,"/")

#if __name__ == "__main__":
#    app.run(debug=True)