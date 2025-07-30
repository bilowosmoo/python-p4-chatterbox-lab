# server/seed.py

from app import app, db
from models import Message

with app.app_context():
    db.drop_all()
    db.create_all()

    messages = [
        Message(body="Hello world!", username="Alice"),
        Message(body="Hey, how’s it going?", username="Bob"),
    ]

    db.session.add_all(messages)
    db.session.commit()
    print("🌱 Seeded the database!")
