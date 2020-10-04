from flask import Flask, jsonify, request
from flask_cors import CORS

compositions = [
    {
        'title' : 'Moonlight Sonata',
        'composer' : 'Ludwig Van Beethoven',
        'finished': True
    },
    {
        'title' : 'Kiss the Rain',
        'composer': 'Yiruma',
        'finished' : True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/compositions', methods=['GET', 'POST'])
def all_compositions():
    response_obj = {'status' : 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        compositions.append({
            'title' : post_data.get('title'),
            'composer' : post_data.get('composer'),
            'finished' : post_data.get('finished')
        })
        response_obj['message'] = 'Composition added!'
    else:
        response_obj['compositions'] = compositions
    return jsonify(response_obj)

if __name__ == '__main__':
    app.run()

