#import sqlite3
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type =float,
        required = True,
        help = "This field cannot be left blank"
    )
    parser.add_argument('store_id',
        type =int,
        required = True,
        help = "Every item needs a store id."
    )
    
    # def get(self, name):
    #     for item in items:
    #         if item['name'] == name:
    #             return item
    #     return{'item': None}, 404

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return{'message': 'Item not found'}, 404

         #item = next(filter(lambda x : x['name'] == name, items), None)
         #return{'item': item}, 200 if item  else 404

        ## connection = sqlite3.connect('data.db')
        ## cursor = connection.cursor()

        ## query = "SELECT * FROM items WHERE name=?"
        ## result = cursor.execute(query,(name,))
        ## row = result.fetchone()
        ## connection.close()

        ## if row:
        ##     return {'item': {'name': row[0], 'price': row[1]}}
        
    def post(self,name):
       # if next(filter(lambda x : x['name'] == name, items), None):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400 

        data = Item.parser.parse_args()

        #item = ItemModel(name, data['price'], data['store_id'])
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return{"message": "An error occurred inserting the item."}, 500 # Internal Server Error

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO items VALUES (?, ?)"
        # cursor.execute(query,(item['name'], item['price']))

        # connection.commit()
        # connection.close()
        
        #items.append(item)
        return item.json(), 201

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        #global items
        #items =list(filter(lambda x : x['name'] != name, items))

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query,(name,))

        # connection.commit()
        # connection.close()

        return{'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        #item = next(filter(lambda x : x['name'] == name, items), None)
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name, data['price'])

        if item is None:
            #item = ItemModel(name, data['price'], data['store_id'])
            item = ItemModel(name, **data)
            #item = {'name':name, 'price': data['price']}
            # try:
            #     updated_item.insert()
            # except:
            #     return{"message": "An error occurred inserting the item."}, 500
        else:
            item.price = data['price']
            # try:
            #     updated_item.update()
            # except:
            #     return{"message": "An error occurred updating the item."}, 500
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        #return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        return {'items': [x.json() for x in ItemModel.query.all()]}
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name':row[0], 'price':row[1]})

        # connection.close()
        
        # return{'items': items}