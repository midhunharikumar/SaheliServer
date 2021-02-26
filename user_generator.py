import sys
from randomuser import RandomUser


from dbconnector import MongoConnector, Customer


def create_sample_customers(num_customers: int = 100):
    pass


def schedule_sample_jobs(num_jobs: int = 100):
    pass


def generate_fake_customers(num_customers: int = 10):
    def generate_address(user):
        street = user.get_street()
        city = user.get_city()
        state = user.get_state()
        address = ','.join([street, city, state])
        return address
    user_list = RandomUser.generate_users(10)
    user_list = list(map(lambda x: dict(first_name=x.get_first_name(),
                                        last_name=x.get_last_name(),
                                        email=x.get_email(),
                                        address=generate_address(x),
                                        pincode=x.get_zipcode(),
                                        cellphone=x.get_cell()), user_list))
    return user_list


def generate_fake_providers(num_customers: int = 10):
    def generate_address(user):
        street = user.get_street()
        city = user.get_city()
        state = user.get_state()
        address = ','.join([street, city, state])
        return address
    user_list = RandomUser.generate_users(10)
    user_list = list(map(lambda x: dict(first_name=x.get_first_name(),
                                        last_name=x.get_last_name(),
                                        email=x.get_email(),
                                        address=generate_address(x),
                                        pincode=x.get_zipcode(),
                                        cellphone=x.get_cell()), user_list))
    return user_list


if __name__ == '__main__':

    fake_customers = generate_fake_customers()
    print(fake_customers)
    mgc = MongoConnector("random", "saheli-prime", "customer_info")
    customers = [Customer.fromdict(i) for i in fake_customers]
    for customer in customers:
        mgc.add_item(customer.serialize())

    # Insert the customers into the 1
