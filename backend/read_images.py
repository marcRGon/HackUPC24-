import pandas as pd
import requests
import os
import time

def is_nan(string):
    try:
        # Convert string to float and check if it is NaN
        return pd.isna(float(string))
    except ValueError:
        # If conversion fails, it's not NaN
        return False

# Path to the CSV file
csv_file = 'inditextech_hackupc_challenge_images.csv'
#domain_urls = ['https://static.zara.net/photos///2023/I/4/1/p/3265/206/072/2/w/2048/', 'https://sttc-stage-zaraphr.inditex.com/photos/2023/V/0/1/p/3046/081/756/2/']

start_index = 3591
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'if-modified-since': 'Thu, 22 Feb 2024 09:30:26 GMT',
    'if-none-match': '0x8DC3388E71A3BF6',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

# Path to save the downloaded images
save_path = 'dataset'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    def download_image(image_url):
        if is_nan(image_url):
            return

        # Extract the image filename from the URL and remove the end of the string after '?'
        filename = os.path.basename(image_url).split('?')[0]
        # Check if the image already exists in the save path
        if os.path.exists(os.path.join(save_path, filename)):
            print(f"Image {index+1}/{len(df)} already exists as {filename}. Skipping...")
            return
        while True:
            # Send a GET request to download the image
            response = requests.get(image_url, headers=headers)

            if "Access Denied" not in str(response.content):
                # Save the image to the specified path
                with open(os.path.join(save_path, filename), 'wb') as f:
                    f.write(response.content)
            
                print(f"Image {index+1}/{len(df)} downloaded and saved as {filename}")
                break
            else:
                print(f"Error: Access denied for image {index+1}/{len(df)}. URL: {image_url}. Retrying in 10 seconds...")
                time.sleep(10)
    if index >= start_index:
        download_image(row['IMAGE_VERSION_1'])
        download_image(row['IMAGE_VERSION_2'])
        download_image(row['IMAGE_VERSION_3'])

print("All images downloaded and saved successfully.")