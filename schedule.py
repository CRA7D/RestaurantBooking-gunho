class Schedule:
    def __init__(self, date_time, number_of_people, customer):
        self.date_time = date_time
        self.number_of_people = number_of_people
        self.customer = customer

    def get_date_time(self):
        return self.date_time

    def get_number_of_people(self):
        return self.number_of_people

    def get_customer(self):
        return self.customer