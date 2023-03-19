# Run
python3 src/server.py

# Testing
python3 -m unittest discover

## Coverage
coverage run --source=. -m unittest discover
coverage report -m --omit=test/*,*/__init__.py,src/injection/*