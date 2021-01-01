import sys
from randomuser import RandomUser

from dbconnector import


def create_sample_customers(num_customers: int = 100):
    pass


def schedule_sample_jobs(num_jobs: int = 100):
    pass


def generate_fake_customers(num_customers: int = 10):
	def generate_address(self, user):
		street = user.get_street()
		city = user.get_city()
		pincode = user.get_pincode()
		state = user.get_state()
		address = ','.join([street, city, state])
    user_list = RandomUser.generate_users(10)
    user_list = list(map(lambda x: dict("first_name": x.get_first_name(),
                                        "last_name": x.get_last_name(),
                                        "email": x.get_email(),
                                        "address":address,
                                        "pincode":pincode,
                                        "cellphone":x.get_cell())))
    return user_list


if __name__ == '__main__':
    fake_customers = generate_fake_customers()
    # Insert the customers into the db
