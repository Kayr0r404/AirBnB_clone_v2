from models.state import State
from models import storage

states = list(storage.all(State).values())
print(type(states))
