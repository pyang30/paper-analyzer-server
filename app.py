from app import app
from app.user import login

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
