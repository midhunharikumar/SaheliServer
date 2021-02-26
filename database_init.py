import pymongo
from dbconnector import Job, JobScheduler, MongoConnector
import random
from utils import get_fake_date_time

scheduler = JobScheduler()


def get_random_customer():
    mgc = MongoConnector('random', 'saheli-prime', 'customer_info')
    customers = mgc.get_all()
    return random.choice(customers)


def schedule_jobs(num_jobs=10):

    for _ in range(num_jobs):
        customer = get_random_customer()
        service_id = "a1311"
        print(customer['_id'])
        time_duration = get_fake_date_time()
        job = Job(str(customer['_id']),
                  service_id,
                  time_duration)
        scheduler.create(job)


if __name__ == '__main__':
    schedule_jobs()
