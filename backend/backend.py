from flask import Flask, request, jsonify
from retrieve_duplicates import find_files_with_low_distance
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# @app.route('/extract_embedding', methods=['POST'])
# def extract_embedding():
#     # Get the image file from the request
#     image_file = request.files['image']
#     # Extract features from the image
#     feature_vector = extract_features(image_file)
#     # Convert the feature vector to a list for JSON serialization
#     feature_list = feature_vector.tolist()
#     # Return the feature vector as JSON
#     return jsonify({'embedding': feature_list})
#     #feature_string = base64.b64encode(feature_vector.tobytes()).decode('utf-8')
#     # Return the feature vector as a string
#     #return jsonify({'embedding': feature_string})

@app.route('/similarProducts/<id>/<version>', methods=['GET'])
@cross_origin()
def similar_products(id, version):
    similar_ids = find_files_with_low_distance(id, version)
    return jsonify({'products': similar_ids})


if __name__ == '__main__':
    app.run(debug=True)
