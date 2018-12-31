import hug
import core
import os


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
    import pdb; pdb.set_trace()
    cur_path = os.path.dirname(os.path.abspath(__file__))
    doc_path = os.path.join(cur_path, 'documents')
    doc_dir = os.listdir(doc_path)
    result = len(doc_dir)
    assert result == 0

    # 2.1
    file_name = 'test.txt'
    file_path = os.path.join(doc_path, file_name)
    f = open(file_path, 'w')
    f.close()
    doc_dir = os.listdir(doc_path)
    result = len(doc_dir)
    assert result == 1

    # clean documents directory
    os.remove(doc_path, file_name)
