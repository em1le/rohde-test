import os
import hug
import authentication
import core

from base64 import b64encode



def test_home_route():
    """ Test home route (actually the root of the api) """
    result = hug.test.get(core, '/api/v1')
    expected = hug.HTTP_200
    assert result.status == expected

def test_list_document():
    """ Test list all document """
    # 1. test the status code
    result = hug.test.get(core, '/api/v1/list/all')
    expected = hug.HTTP_200
    assert result.status == expected

    # 2. test the directory listing
    cur_path = os.path.dirname(os.path.abspath(__file__))
    doc_path = os.path.join(cur_path, 'test_documents')
    doc_dir = os.listdir(doc_path)
    result = len(doc_dir)
    assert result == 1  # Because __init__.py

def test_list_document_by_title():
    """ Test list specific document by its title """
    # 1. test if a document is retrieved by its title
    cur_path = os.path.dirname(os.path.abspath(__file__))
    doc_path = os.path.join(cur_path, 'test_documents')

    # create a temp file   
    temp_f = open(os.path.join(doc_path, 'test.txt'), 'w')
    temp_f.close()

    result= os.listdir(doc_path)

    assert 'test' in result[0]

    result = hug.test.get(core, '/api/v1/list?title=test')
    assert result == hug.HTTP_200

    # clean
    os.remove(os.path.join(doc_path, 'test.txt'))

def test_create_document_without_credentials():
    result = hug.test.post(core, '/api/v1/create')
    expected = hug.HTTP_401
    assert result.status == expected

def test_create_document():
    token = b64encode('{0}:{1}'.format('Emile', '1234').encode('utf8')).decode('utf8')
    result = hug.test.post(core, '/api/v1/create',
        name='Emile',
        headers={'Authorization': 'Basic {0}'.format(token)},
        body={'title': 'title', 'content': 'this is content'}
    )
    expected = hug.HTTP_200
    assert result.status == expected

def test_delete_document():
    cur_path = os.path.dirname(os.path.abspath(__file__))
    doc_path = os.path.join(cur_path, 'test_documents')

    # create a temp file   
    temp_f = open(os.path.join(doc_path, 'test.txt'), 'w')
    temp_f.close()

    result= os.listdir(doc_path)

    assert 'test' in result[0]

    token = b64encode('{0}:{1}'.format('Emile', '1234').encode('utf8')).decode('utf8')
    result = hug.test.delete(core, '/api/v1/delete',
        name='Emile',
        headers={'Authorization': 'Basic {0}'.format(token)},
        body={'title': 'test'}
    )
    assert result.status == hug.HTTP_200