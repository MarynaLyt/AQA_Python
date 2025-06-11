import requests
import os

NASA_API_URL = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
sol = 1000
camera = 'fhaz'
api_key = 'DEMO_KEY'
New_Folder = "mars_photos"


def get_mars_photos():
    params = {
        "sol": sol,
        "camera": camera,
        "api_key": api_key
    }
    try:
        response = requests.get(api_key, params=params)
        response.raise_for_status()
        return response.json().get("photos", [])
    except requests.exceptions.RequestException as e:
        print(f"Error while requesting NASA API: {e}")
        return []


def download_photo(url, path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(path, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False


def main():
    os.makedirs(New_Folder, exist_ok=True)
    try:
        response = requests.get(NASA_API_URL, params={'sol': sol, 'camera': camera, 'api_key': api_key})
        response.raise_for_status()
        photos = response.json().get('photos', [])[:5]
    except Exception as e:
        print(f"API error: {e}")
        return

    count = sum(
        download_photo(photo['img_src'], os.path.join(New_Folder, f"mars_photo_{i + 1}.jpg"))
        for i, photo in enumerate(photos) if 'img_src' in photo
    )
    print(f"Successfully downloaded {count} photos")


if __name__ == "__main__":
    main()

