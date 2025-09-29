# Winnipeg Transit App

This project is a Python-based application, developed in a Jupyter Notebook, for interacting with the **live Winnipeg Transit API**. It fetches real-time schedule and stop data, allows the user to make a selection, and displays color-coded arrival times.

### Key Concepts Demonstrated:
* **API Integration:** Connecting to a live web service and handling responses using the `requests` library.
* **JSON Data Handling:** Parsing complex JSON data into Python dictionaries and lists for easy access.
* **Date & Time Manipulation:** Converting API timestamp strings into `datetime` objects for comparison and formatting using `dateutil.parser`.
* **Conditional Terminal Output:** Using the `colorama` library to dynamically color-code the terminal output based on bus status (late, early, or on time).

### Files in this Project:
* **`winnipeg_transit_app.ipynb`**: The main Jupyter Notebook containing the Python code to query the API and display results.
* **`schedule_data.json`**: An output file containing a sample of the schedule data retrieved from the API.
* **`stops_data.json`**: An output file containing a sample of the stop data retrieved from the API.

### How to Run:
1.  Install the required Python libraries: `pip install requests python-dateutil colorama notebook`.
2.  Get a free API key from the [Winnipeg Transit API website](https://api.winnipegtransit.com) and paste it into the `API_KEY` variable inside the notebook.
3.  Launch Jupyter Notebook from your terminal.
4.  Navigate to this project's directory, open the `.ipynb` file, and run the cells.