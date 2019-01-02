import os
import hug
import json
from settings import _CURRENT_PATH, _DOCUMENT_PATH, authenticated_area

api = hug.API(__name__).http.base_url = '/api'


@hug.get('/', versions=1)
def home():
    """ Simple welcoming url """
    message = 'Hi there ! Welcome to a small document api'
    return {'message': message}


@hug.get('/list/all', version=1)
def list_document():
    """ List all documents """
    files = {}
    for doc in documents_dir:
        with open(os.path.join(_DOCUMENT_PATH, doc), 'r') as f:
            files[doc] = f.read()
    return {
        'message': 'There is {n} file in the documents directory'.format(n=len(documents_dir)),
        'files': files
    }


@hug.get('/list', version=1)
def list_document_by_title(title: hug.types.text):
    """ List a specific document by its title """
    documents_dir = os.listdir(_DOCUMENT_PATH)

    message = "No file with title : {title}".format(title=title)
    for filename in documents_dir:
        if title in filename:
            with open(os.path.join(_DOCUMENT_PATH, filename), 'r') as f:
                message = "A document has been found : {filename} \n with following content : {content}".format(filename=filename, content=f.read())
            break
    return {'message': message}


@authenticated_area.post('/create', version=1)
def create_document(title: hug.types.text, content: hug.types.text):
    """ In this API context a document consist of :
        - a title : text
        - a content : text
    """
    data = {'content': content}
    file_path = os.path.join(_DOCUMENT_PATH, '{}.json'.format(title))

    with open(file_path, 'w') as out_file:
        json.dump(data, out_file)
    return {'message': 'document posted {}'.format(title)}


@authenticated_area.delete('/delete', version=1)
def delete_document(title: hug.types.text):
    """ Delete file by title """
    documents_dir = os.listdir(_DOCUMENT_PATH)

    message = {'message': 'no document named {} was found'.format(title)}
    for filename in documents_dir:
        if title in filename:
            os.remove(os.path.join(_DOCUMENT_PATH, filename))
            message = {
                'message': 'Deleted document {}'.format(filename)
            }
            break
    return message


@authenticated_area.patch('/update', version=1)
def update_document(title: hug.types.text, content: hug.types.text):
    """ Update file by title """
    message = {'message': 'No file to update was found'}
    for filename in os.listdir(_DOCUMENT_PATH):
        if title in filename:
            with open(os.path.join(_DOCUMENT_PATH, filename), 'w+') as f:
                f.write(content)
            message = {'message': 'The document named {doc_name} was updated with the content : {content}'.format(
                doc_name=filename,
                content=content
            )}
            break
    return message
