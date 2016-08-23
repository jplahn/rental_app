# Some sort of website
Comparing rental cities and stuff

## Setup
- Follow these instructions - http://flask.pocoo.org/docs/0.11/installation/
- Create a `.env` file in the application root
- Put the following in that -

```python
# .env
source venv/bin/activate

export SECRET_KEY='get_this_from_repo_owner'

# Mongo DB Configuration
export MONGO_HOST='get_this_from_repo_owner'
export MONGO_PORT='get_this_from_repo_owner'
export MONGO_DBNAME='get_this_from_repo_owner'
export MONGO_USERNAME='get_this_from_repo_owner'
export MONGO_PASSWORD='get_this_from_repo_owner'

# App Config
export FLASK_DEBUG=True
export ASSETS_DEBUG=True
export FLASK_APP=app.py
```

### BASH Users
```bash
echo "source `which activate.sh`" >> ~/.bashrc
source ~/.bashrc
```
### ZSH Users
```bash
echo "source `which activate.sh`" >> ~/.zshrc
source ~/.zshrc
```
- Move out of the application directory and get back in to initialize the ENV variables
- Run the application `flask run`

## Handling assets
- We are using https://flask-assets.readthedocs.io/en/latest/ to manage our assets
- Define the assets required in the layout file. It uses relative path from `/static` folder
- Turn on Assets Debug if required using configuration in your .env file
- Access images directly from the `/static/img` folder path
- Run the following in your terminal

## Basic Flow
1. User hits the homepage and are able to select a city they want to view rental data for. Right now I have a text box for city selection, probably need to make that a drop down list initially since supported cities will likely be limited (since we will have to manually populate a DB due to lack of available APIs)
2. Once the user selects a city, they're presented with a summary of the city's rental statistics (statistics TBD) and maybe related visuals. If it makes sense, this summary can also include a "ranking" relative to other cities we've charted
3. Somewhere on the city summary page, a user can select a certain metric to get more detailed information on. For example, the user can choose to get a visualization charting YoY growth of population, or price / sq. ft., or whatever else.
4. The visualizations should be interactive, so they'll likely be built out with D3 (except in cases where D3 is overkill).
5. At some point, it would be nice to have the ability to select two cities and compare them along different metrics.

## Notes
* Treat Issues as a backlog of sorts
* Better architecture document to come# Some sort of website
