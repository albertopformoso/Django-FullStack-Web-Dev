import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

## FAKE POPULATION SCRIPT
import random
from app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = [
    'Search',
    'Social',
    'Marketplace',
    'News',
    'Games'
]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]  # tuple (entry, random_thing)
    t.save()
    return t

def populate(N: int=5):

    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a face access recor for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('[+] populating script')
    populate(20)
    print('[+] populating complete')