import pickle
from app import app

r = app.redis


def save(key, object):
    pickled_object = pickle.dumps(object)
    r.set(key, pickled_object)


def fetch(key):
    try: 
        unpacked_object = pickle.loads(r.get(key))
        return unpacked_object
    except:
        return None


def wipe(key):
    r.delete(key)
