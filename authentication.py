import hug


# Basic auth 
USERNAME = 'Emile'
PASSWORD = '1234'

authenticated_area= hug.http(requires=hug.authentication.basic(hug.authentication.verify(USERNAME, PASSWORD)))