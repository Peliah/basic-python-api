from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS
from flask_caching import Cache

app = Flask(__name__)
CORS(app)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/', methods=['GET'])
@cache.cached(timeout=60)
def get_info():

    data = {
        "email": "pelepoupa@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Peliah/basic-python-api"
    }
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)