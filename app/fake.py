from random import randint
from faker import Faker
from .models import User, Post
from app import db
from sqlalchemy.exc import IntegrityError


def users(count=100):
    fake = Faker()
    i = 0
    while i < count:
        u = User(email=fake.email(),
        username=fake.user_name(),
        password='password',
        confirmed=True,
        name=fake.name(),
        location=fake.city(),
        about_me=fake.text(),
        member_since=fake.past_date())
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()

def posts(count=100):
    fake = Faker()
    user_count = User.query.count()
    for i in range(count):
        u = User.query.offset(randint(0, user_count - 1)).first()
        p = Post(body=fake.text(), author=u)
        db.session.add(p)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()