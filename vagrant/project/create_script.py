from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

# The create engine function lets our program know which database we want to communicate with
engine = create_engine('sqlite:///restaurantmenu.db')

# Bind the engine to the base class
Base.metadata.bind = engine

# This establishes a link of communication between our code executions and the engine we created
# In order to do CRUD operations on a database sqlalchemy uses an INTERFACE called session
# A session allows us to write down all the commands we want to execute but not call them until we do a commit
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
cheesepizza = MenuItem(name="Cheese Pizza", description="Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
session.query(MenuItem).all()