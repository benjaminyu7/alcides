# Run
python3 src/server.py

# Testing
python3 -m unittest discover

## Coverage
coverage report -m --omit=test/*,*/__init__.py,src/injection/*