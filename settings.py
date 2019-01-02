import os
import hug
# Settings file

# Path of the project folder
_CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

# Path of the documents folder
_DOCUMENT_PATH = os.path.join(_CURRENT_PATH, 'documents')

# Credentials
USERNAME = 'Emile'
PASSWORD = '1234'

authenticated_area= hug.http(requires=hug.authentication.basic(hug.authentication.verify(USERNAME, PASSWORD)))
