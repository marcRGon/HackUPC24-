from flask import Flask, request, jsonify
from image_embeddings import extract_features
import base64

app = Flask(__name__)

@app.route('/extract_embedding', methods=['POST'])
def extract_embedding():
    # Get the image file from the request
    image_file = request.files['image']
    # Extract features from the image
    feature_vector = extract_features(image_file)
    # Convert the feature vector to a list for JSON serialization
    feature_list = feature_vector.tolist()
    # Return the feature vector as JSON
    return jsonify({'embedding': feature_list})
    #feature_string = base64.b64encode(feature_vector.tobytes()).decode('utf-8')
    # Return the feature vector as a string
    #return jsonify({'embedding': feature_string})

if __name__ == '__main__':
    app.run(debug=True)