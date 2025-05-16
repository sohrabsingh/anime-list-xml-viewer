import os
import json
import requests
import xml.etree.ElementTree as ET

# === CONFIG ===
XML_FILE = 'myanimelist.xml'     # Path to your exported MAL XML
SAVE_FOLDER = './anime_images'   # Folder to save images
TOKEN_FILE = './authorization/token.json'        # Path to the token JSON file

# === Load OAuth token from file ===
def load_token() -> str:
    with open(TOKEN_FILE, "r") as file:
        token_data = json.load(file)
    return token_data["access_token"]

# === Extract (title, id) tuples from XML ===
def extract_anime_info_from_xml(xml_path: str) -> list:
    tree = ET.parse(xml_path)
    root = tree.getroot()

    anime_info = []
    for anime in root.findall('anime'):
        title_elem = anime.find('series_title')
        id_elem = anime.find('series_animedb_id')
        if title_elem is not None and id_elem is not None:
            title = title_elem.text
            anime_id = id_elem.text
            anime_info.append((title, anime_id))
    return anime_info

# === Search MAL API for image URL by title ===
def fetch_image_url(anime_name: str, access_token: str) -> str:
    url = "https://api.myanimelist.net/v2/anime"
    params = {
        "q": anime_name,
        "limit": 1,
        "fields": "id,title,main_picture"
    }
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    if "data" in data and data["data"]:
        anime = data["data"][0]["node"]
        return anime.get("main_picture", {}).get("large", anime.get("main_picture", {}).get("medium", None))
    return None

# === Download image to path ===
def download_image(url: str, save_path: str):
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, 'wb') as file:
        file.write(response.content)

# === Main function ===
def download_all_anime_images(xml_path: str, folder: str):
    access_token = load_token()
    anime_list = extract_anime_info_from_xml(xml_path)

    if not os.path.exists(folder):
        os.makedirs(folder)

    for title, anime_id in anime_list:
        file_name = f"anime_{anime_id}.jpg"
        file_path = os.path.join(folder, file_name)

        # Skip if already exists
        if os.path.exists(file_path):
            print(f"Skipping (already exists): {file_name}")
            continue

        print(f"Fetching image for: {title} (ID: {anime_id})")
        try:
            image_url = fetch_image_url(title, access_token)
            if image_url:
                download_image(image_url, file_path)
                print(f"Downloaded: {file_path}")
            else:
                print(f"Image not found for: {title}")
        except Exception as e:
            print(f"Skipped: {title} (ID: {anime_id}) — Error: {e}")

if __name__ == "__main__":
    download_all_anime_images(XML_FILE, SAVE_FOLDER)
