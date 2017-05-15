from flask import Flask, render_template
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants')
def restaurants():
	restaurants = session.query(Restaurant).all()

	return render_template('restaurants.html', restaurants = restaurants)

@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)

	return render_template('menu.html', restaurant=restaurant, items = items)

@app.route('/restaurants/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	pass

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	item = session.query(MenuItem).filter_by(id = menu_id).one()
	pass

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem():
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	item = session.query(MenuItem).filter_by(id = menu_id).one()
	pass
	

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)