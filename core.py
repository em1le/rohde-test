import hug
import os

api = hug.API(__name__).http.base_url = '/api'

# Restfull API constraints
# I - Uniform Interface
# II - Stateless
# III - Cacheable
# IV - Client-Server
# V - Layered System
# VI - Code on demand

@hug.get('/', versions=1)
def home(response):
    """ Simple welcoming url """
    return {'message': 'Hi there, welcome to the Rohde&Swartz document management api'}


@hug.get('/list/all', version=1)
def list_document(response):
    """ List all documents """
    current_path = os.path.dirname(os.path.abspath(__file__))
    documents_path = os.path.join(current_path, 'documents')
    documents_dir = os.listdir(documents_path)
    return {
        'message': 'There is {n} file in the documents directory'.format(n=len(documents_dir))
    }
