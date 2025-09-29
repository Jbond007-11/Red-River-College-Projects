# NASA Mars Rover Photo Viewer

The application interacts directly with the NASA API to fetch rover data and images. The project was initially developed and tested in a Jupyter Notebook (`nasa.ipynb`) and then formalized into a final Python script (`nasa.py`).

### Key Features
* **Interactive Terminal Menu:** Utilizes the `Menu` library to provide a user-friendly, navigable command-line interface.
* **Live API Integration:** Fetches data directly from the NASA Mars Rover Photos API using the `requests` library.
* **Dynamic Photo Display:** Retrieves and displays images from URLs using the `Pillow` (PIL) library.
* **Structured Code:** The application is organized into functions for fetching data, handling user selections, and displaying menus.
* **Photo Pagination:** Displays the first 10 photos from the results to avoid overwhelming the user in a single menu.

### API Key Setup (Required)

This application requires a personal API key from NASA to function.

* **Generate Your Key:** Visit the NASA API website to generate your own free API key: https://api.nasa.gov.
* **Add Key to the Script:** Open the nasa.py file in a text editor. Find the line 
* **API_KEY =** `"YOUR_API_KEY_HERE"` and replace the placeholder text with the key you just generated.

### Quick Test Instructions
To quickly test the application with a known working example, run the script and follow this **exact input sequence** when prompted:

1. At the main menu, choose 'Search Mars Rover Photos': `1`

2. At the rover selection menu, choose 'Curiosity': `1`

3. When prompted for a date, enter Curiosity's landing date: `2012-08-06`

This will search for photos taken by the Curiosity rover on August 6, 2012, which is a date known to have many available photos.

### How to Run
1.  Ensure you have Python installed.
2.  [cite_start]Install the required libraries: `pip install requests Pillow Menu`[cite: 73, 75, 77].
3.  Navigate to the project directory in your terminal.
4.  Run the Python script: `python nasa.py`.
5.  Follow the on-screen menus.

### Project Files
* `nasa.py`: The final, executable Python script for the application.
* `nasa.ipynb`: The developmental Jupyter Notebook used for prototyping and testing.