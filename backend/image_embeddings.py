import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Load pre-trained ResNet model
resnet = models.resnet18(pretrained=True)
# Set the model to evaluation mode
resnet.eval()

# Define a function to preprocess the image
def preprocess_image(image_path):
    # Define transformation pipeline
    preprocess = transforms.Compose([
        transforms.Resize(256),           # Resize to 256x256
        transforms.CenterCrop(224),       # Crop the center 224x224 region
        transforms.ToTensor(),            # Convert to tensor
        transforms.Normalize(             # Normalize with ImageNet mean and std
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    # Load and preprocess the image
    img = Image.open(image_path)
    img = preprocess(img)
    # Add batch dimension to the image tensor
    img = img.unsqueeze(0)
    return img

# Define a function to extract features from the image using ResNet
def extract_features(image_path):
    # Preprocess the image
    img = preprocess_image(image_path)
    # Forward pass through the ResNet model
    with torch.no_grad():
        features = resnet(img)
    # Flatten the feature tensor to a one-dimensional vector
    features = torch.flatten(features, start_dim=1)
    # Convert the feature tensor to a numpy array
    feature_vector = features.numpy()
    # Modify the shape from (1, 1000) to (1000,)
    feature_vector = feature_vector.squeeze()
    print(feature_vector)
    return feature_vector

# Example usage:
"""image_path = "example.jpg"
feature_vector = extract_features(image_path)
print("Feature vector shape:", feature_vector.shape)
print("Feature vector:", feature_vector)
"""