import os
import hug
import json
from authentication import authenticated_area

api = hug.API(__name__).http.base_url = '/api'

_CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
# Restfull API constraints
# I - Uniform Interface
# II - Stateless
# III - Cacheable
# IV - Client-Server
# V - Layered System
# VI - Code on demand

@hug.get('/', versions=1)
def home():
    """ Simple welcoming url """
    message = 'Hi there ! Welcome to a small document api'
    return {'message': message}


@hug.get('/list/all', version=1)
def list_document():
    """ List all documents """
    documents_path = os.path.join(_CURRENT_PATH, 'documents')

    if not os.path.isdir(documents_path):
        os.mkdir(documents_path)
    documents_dir = os.listdir(documents_path)
    return {
        'message': 'There is {n} file in the documents directory'.format(n=len(documents_dir)),
        'files': [file for file in documents_dir],
    }


@hug.get('/list', version=1)
def list_document_by_title(title: hug.types.text):
    """ List a specific document by its title"""
    documents_path = os.path.join(_CURRENT_PATH, 'documents')
    documents_dir = os.listdir(documents_path)

    message = "No file with title : {title}".format(title=title)
    for filename in documents_dir:
        if title in filename:
            message = "A document has been found : {filename}".format(filename=filename)
            break
    return {'message': message}


@authenticated_area.post('/create', version=1)
def create_document(title: hug.types.text, content: hug.types.text):
    """ In this API context a document consist of : 
        - a title : text   
        - a content : text
    """
    data = {'content': content}
    documents_path = os.path.join(_CURRENT_PATH, 'documents')
    file_path = os.path.join(documents_path, '{}.json'.format(title)) 

    with open(file_path, 'w+') as out_file:
        json.dump(data, out_file)
    return {'message': 'document posted {}'.format(title)}


@authenticated_area.delete('/delete', version=1)
def delete_document(title: hug.types.text):
    """ Delete file by title """
    documents_path = os.path.join(_CURRENT_PATH, 'documents')
    documents_dir = os.listdir(documents_path)

    message = {'message': 'no document named {} was found'.format(title)}
    for filename in documents_dir:
        if title in filename:
            os.remove(os.path.join(documents_path, filename))
            message = {
                'message': 'Deleted document {}'.format(filename)
            }
            break
    return message