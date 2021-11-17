# import json
import requests

data = requests.get('https://ct-mock-tech-assessment.herokuapp.com/')
# packages_json = r.json()

# packages_str = json.dumps(packages_json, indent=2)

# installs_30 = packages_json
# print(r.text)

persons = data.json()['partners']


# print(persons)
class Person:
    _all = []

    def __init__ (self, availableDates, country, email, firstName, lastName):
        self.availableDates = availableDates
        self.country = country
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self._all.append(self)
    
    
    
    @classmethod
    def run(cls):
        pass

    def __repr__(self):
        return f'Person: {self.firstName}{self.lastName}'



for i in persons:
    Person(
        availableDates=i['availableDates'],
        country=i['country'],
        email=i['email'],
        firstName=i['firstName'],
        lastName=i['lastName']

    )

print(Person._all)

# class country:
#     pass


# class email:
#     pass


# class name:
#     pass



# Person._all[0].__dict__
