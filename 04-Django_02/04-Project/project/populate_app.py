import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

## FAKE POPULATION SCRIPT
import random
from app.models import User
from faker import Faker

fakegen = Faker()
topics = [
    'Search',
    'Social',
    'Marketplace',
    'News',
    'Games'
]

def populate(N: int=5):

    for entry in range(N):

        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(
            first_name=fake_first_name, 
            last_name=fake_last_name, 
            email=fake_email
        )[0]

if __name__ == '__main__':
    print('[+] populating script')
    populate(20)
    print('[+] populating complete')