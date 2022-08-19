from app import app
from os import environ as env

if __name__ == '__main__':
    port = 5000 | env["PORT"]
    app.run(debug=False,host='0.0.0.0',port=port)