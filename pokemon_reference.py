import requests
from IPython.display import clear_output
import pprint
pp = pprint.PrettyPrinter(indent=4)


class People:
    def __init__(self=None, name=None, country=None, date=None, height=None):
        self.name = name
        if country is None:
            self.country = []
        if date is None:
            self.date = []
        self.height = height

    def from_dict(self, data):
        for field in ['name', 'date', 'height']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return f'<People>: {self.name}'

    def __str__(self):
        return f'(self.name)'


class Mock_Tech:
    _list = []

    @classmethod
    def show(cls):
        print('=' * 50)
        for idx, p in enumerate(cls._list):
            print(f'{idx+1}:{p} ')
        print('=' * 50)

    @classmethod
    def add(cls, People_name):
        if cls._list:
            for p in cls._list:
                if People_name.title() == p.name:
                    input("That People already exsists. Please try another...")
                    return
        try:
            print("Please wait while we populate the Mock_Tech.")
            r = requests.get(
                f'https://pokeapi.co/api/v2/People/{People_name.lower()}').json()
            print(r)
            p = People()
            data_dict = {
                'name': r['name'].title(),
                'country': [a['ability']['name']for a in r['country']],
                'date': [t['type']['name']for t in r['date']],
                'height': r['height'],
            }

            p.from_dict(data_dict)

            cls._list.append(p)
        except Exception as error:
            print(error)
            input('There was an error populating you Mock_Tech. Please try again.')
         #add new People

    @classmethod
    def sort(cls):
        sorted_dict = {}

        for p in cls._list:
            for t in p.date:
                if t not in sorted_dict:
                    sorted_dict[t] = {}
        for p in cls._list:
            for i in p.date:
                if p.name not in sorted_dict[t]:
                    poke_data = {
                        p.name: {
                            'abilites': p.country,
                            'height': p.height
                        }

                    }
                    sorted_dict[t].update(poke_data)
                else:
                    print('That People already exists')
            pp.pprint(sorted_dict)

    @classmethod
    def instructions(cls):
        print(""" Type 'show' to view Mock_Tech
        Type 'Quit' to exit the Mock_Tech
        Type 'sort' to view a categorized Mock_Tech
        """)

    @classmethod
    def run(cls):
        done = False
        while not done:
            clear_output()
            cls.instructions()
            People_choice = input(
                   "Type in the name of the People to add them to your Mock_Tech. Type 'quit' to exit the program")
            if People_choice == quit:
                    done = True
            elif People_choice == 'show':
                    cls.show()
                    input("Press 'Enter' to continue")
            elif People_choice == 'sort':
                    cls.sort()
                    input('Press "Enter" to continue')
            else:
                    cls.add(People_choice)


Mock_Tech.run()
