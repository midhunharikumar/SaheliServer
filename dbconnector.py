# Customer format

# first_name, last_name, email, cellphone, address, pincode

from datetime import datetime
import uuid
import pymongo
import datetime


class MongoConnector:
    #(TODO) refactor all the customer code here

    def __init__(self, clientURL, base_db_key, sub_db_key):
        self.client = pymongo.MongoClient()
        self.base_database_key = base_db_key  # 'saheli-prime'
        self.sub_database_key = sub_db_key  # 'customer_info'

    def add_item(self, customer):
        print(customer)
        return self.client[self.base_database_key][self.sub_database_key].insert_one(customer)

    def find_item(self, customer):
        db = self.client[self.base_database_key][self.sub_database_key]
        mydoc = db.find(customer)
        for x in mydoc:
            print(x)
        return []

    def delete_item(self, customer):
        db = self.client[self.base_database_key][self.sub_database_key]
        db.delete_many(customer)

    def get_all(self):
        db = self.client[self.base_database_key][self.sub_database_key]
        return list(db.find({}))


class Job:

    def __init__(self, customer_id: str, service_id: str):
        #(TODO) investigate if UUID is the best way to handle this.
        self._id = str(uuid.uuid4())[:5]
        self.job_id = self._id
        self.service_id = service_id
        self.customer_id = customer_id
        self.date = datetime.datetime.now()
        # Add a time delta for expiration
        self.expiry = self.date + datetime.timedelta(days=1)

    def serialize(self):
        serial = {"_id": self.job_id,
                  "job_id": self.job_id,
                  "service_id": self.service_id,
                  "customer_id": self.customer_id,
                  "date": self.date,
                  "expiry": self.expiry}
        return serial


class JobDBConnector(MongoConnector):
    ''' Base class that connects to MongoDB'''

    def __init__(self, base_db_key, sub_db_key):
        super().__init__(self, base_db_key, sub_db_key)

    def add(self, job):
        print(job.serialize())
        self.add_item(job.serialize())

    def get(self):
        return self.get_all()


class JobScheduler:
    ''' Class defines and creates new jobs and adds them to the DB.
        (TODO) Make async '''

    def __init__(self):
        self.dbconnector = JobDBConnector('jobs_db', 'scheduled')

    def create(self, job):
        self.dbconnector.add(job)


class JobEnumerator:

    def __init__(self):
        self.dbconnector = JobDBConnector('jobs_db', 'scheduler')

    def get_jobs(self):
        jobs = self.dbconnector.get_all()
        return jobs


class User:

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.address = None
        self.phone = None
        self.pincode = None


class Provider(User):

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
        self.service_id = service_id_list
        self.location = location
        self.cellphone = cellphone

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
                    "creation_date": datetime.datetime.timestamp(self.creation_date)}
        for key, value in dict(out_dict).items():
            if value is None:
                del out_dict[key]
        return out_dict


class Customer(User):

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
                      datadict.get('_id', str(uuid.uuid4())))
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


class MongoDatabaseOrchestrator:

    def __init__(self, clientURL):
        self.client = pymongo.MongoClient()


if __name__ == '__main__':
    print('Hello')
    mgc = MongoConnector('random', 'saheli-prime', 'customer_info')
    print(mgc.client.database_names())
    print(mgc.get_all())
