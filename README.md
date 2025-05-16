# 🎥 MyAnimeList XML Viewer

A lightweight, browser-based tool to visualize your exported MyAnimeList (MAL) anime list in an elegant grid format. This tool parses your `.xml` export file and displays grouped anime entries based on their status (e.g., Watching, Completed, Plan to Watch).

## 🌟 Features

- Upload and parse MyAnimeList `.xml` export files directly in the browser.
- Automatically displays only the anime marked for update (`update_on_import = 1`).
- Groups anime by status (e.g., Watching, Completed).
- Clean and modern user interface using HTML, CSS, and JavaScript.
- Shows AnimeDB ID, title, and a corresponding image (if available in `images/` folder).

## 📂 Folder Structure
```
project/
│
├── index.html # Main HTML file (includes inline CSS and JavaScript)
├── images/
│ └── anime_<id>.jpg # Optional folder containing anime cover images
└── README.md # Project documentation (this file)
```
> 💡 Anime images are expected to follow the naming format: `anime_<id>.jpg` (where `<id>` is the AnimeDB ID).

## 🚀 How to Use

1. Clone or download the repository to your local system.
2. Open `index.html` in any modern web browser.
3. Click the file input and upload your exported MAL `.xml` file.
4. View your anime list organized by status with images and metadata.

## 📤 Exporting from MyAnimeList

1. Go to [MyAnimeList](https://myanimelist.net/).
2. Log in and navigate to your profile.
3. Choose **Export** from the anime list page.
4. Download the `.xml` file.
5. Use this file in the viewer.

## 🖼️ Optional Image Support

If you have cover images stored locally:
- Place them in the `images/` folder.
- Name them as `anime_<anime_id>.jpg` (e.g., `anime_12345.jpg`).

If no image is found, the card will still display properly without it.

## 🛠️ Tech Stack

- **HTML5**
- **CSS3**
- **Vanilla JavaScript**
- **FileReader API**
- **DOMParser API**

## 📌 Limitations

- No server-side code — works entirely in the browser.
- Only displays entries with `<update_on_import>1</update_on_import>`.
- Anime cover images must be manually downloaded and named correctly.

## 📄 License

This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).

---

🎉 Enjoy organizing and exploring your anime list in a new visual way!
