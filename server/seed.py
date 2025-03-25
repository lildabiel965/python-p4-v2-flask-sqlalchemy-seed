#!/usr/bin/env python3


from app import app
from models import db, Pet
from faker import Faker
from random import choice as rc

with app.app_context():
    try:
        # Delete all rows in the "pets" table
        Pet.query.delete()

        # Create and initialize a faker generator
        fake = Faker()

        # Create an empty list
        pets = []

        species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

        # Add some Pet instances to the list
        for n in range(10):
            pet = Pet(name=fake.first_name(), species=rc(species))
            pets.append(pet)

        # Insert each Pet in the list into the database table
        db.session.add_all(pets)

        # Commit the transaction
        print("Current pets in the database:", Pet.query.all())
        db.session.commit()
        print("Seeding completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
