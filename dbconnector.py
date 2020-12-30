# Customer format

# first_name, last_name, email, cellphone, address, pincode

from datetime import datetime
import uuid
import pymongo


class Provider:

    def __init__(self,
                 id_image,
                 face_image,
                 service_id,
                 location,
                 cellphone,
                 _id=None):
        self._id = str(uuid.uuid4()) if _id == None else _id
        self.id_image = id_image
        self.face_image = face_image
        self.service_id = service_id
        self.location = location,
        self.cellphone = cellphone,

    @classmethod
    def fromdict(cls, datadict):
        in_dict = cls(datadict.get('id_image', None),
                      datadict.get('face_image', None),
                      datadict.get('service_id', None),
                      datadict.get('location', None),
                      datadict.get('cellphone', None),
                      datadict.get('_id', None))
        return in_dict

    def serialize(self):
        out_dict = {"id_image": self.first_name,
                    "face_image": self.last_name,
                    "service_id": self.address,
                    "location": self.pincode,
                    "cellphone": self.cellphone,
                    "creation_date": datetime.timestamp(self.creation_date)}
        for key, value in dict(out_dict).items():
            if value is None:
                del out_dict[key]
        return out_dict


class Customer:

    def __init__(self,
                 first_name,
                 last_name,
                 address,
                 pincode,
                 email,
                 cellphone,
                 _id=None):
        self._id = str(uuid.uuid4()) if _id == None else _id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.pincode = pincode
        self.email = email
        self.cellphone = cellphone
        self.creation_date = datetime.now()

    @classmethod
    def fromdict(cls, datadict):
        in_dict = cls(datadict.get('first_name', None),
                      datadict.get('last_name', None),
                      datadict.get('address', None),
                      datadict.get('pincode', None),
                      datadict.get('email', None),
                      datadict.get('cellphone', None),
                      datadict.get('_id', None))
        return in_dict

    def serialize(self):
        out_dict = {"_id": self._id,
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "address": self.address,
                    "pincode": self.pincode,
                    "email": self.email,
                    "cellphone": self.cellphone,
                    "creation_date": datetime.timestamp(self.creation_date)}
        for key, value in dict(out_dict).items():
            if value is None:
                del out_dict[key]
        return out_dict


class MongoConnector:

    def __init__(self, clientURL):
        self.client = pymongo.MongoClient(clientURL)
        self.base_database_key = 'saheli-prime'
        self.customer_database_key = 'customer_info'

    def add_customer(self, customer):
        return self.client[self.base_database_key][self.customer_database_key].insert_one(customer)

    def find_customer(self, customer):
        db = self.client[self.base_database_key][self.customer_database_key]
        mydoc = db.find(customer)
        for x in mydoc:
            print(x)
        return []

    def delete_customer(self, customer):
        db = self.client[self.base_database_key][self.customer_database_key]
        db.delete_many(customer)

    def get_all_customer(self):
        db = self.client[self.base_database_key][self.customer_database_key]
        return list(db.find({}))
