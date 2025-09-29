from requests import get
import json
from PIL import Image
from io import BytesIO
from menu import Menu

API_KEY = "YOUR_API_KEY_HERE"

def fetch_rovers_data(api_key):

    # API endpoint URL construction
    url_rovers = f"https://api.nasa.gov/mars-photos/api/v1/rovers?api_key={api_key}"
    try:
        # Making GET request to NASA API
        response = get(url_rovers)
        response.raise_for_status()

        #Parse JSON response
        all_rovers = response.json() # Storing the raw json data 
        rovers_list = all_rovers.get('rovers', []) # Extracting Rovers

        print(f"Found {len(rovers_list)} rovers.")
        return rovers_list # Return the list of rover data
    
    # Error handling
    except Exception as e:
        # Handing errors during API request or json prasing
        print(f"Error fetching rover data: {e}")
        return [] # Returns empty list if error occurs
rovers_list = fetch_rovers_data(API_KEY)

def display_photo(url):
    """Displays the photo found at url."""
    img_resp = get(url)
    img_resp.raise_for_status()
    img = Image.open(BytesIO(img_resp.content))
    img.show()
    img.close()

# Lets the user select a rover and returns its name, or None if they exit
# Lets the user select a rover and returns its name, or None if they exit
def select_rover(rovers):
    
    # Display menu header
    print("\nSelect a Mars Rover:")

    # Display numbered list of available rovers
    for i, rover in enumerate(rovers, 1):
        print(f"{i}. {rover['name']}")
    
    # add exit option at the end
    print(f"{len(rovers) + 1}. Return to Main Menu")
    
    # Validation loop where it continues till valid selection
    while True:
        try:
            # Use a lambda to capture user input
            get_input = lambda: int(input("> "))
            choice = get_input()
            
            # Check if user selected Return to Main Menu
            if choice == len(rovers) + 1:
                return None # Exit selection return to prev menu
            
            # Validate choice is within valid rover range
            if 1 <= choice <= len(rovers):
                selected_rover = rovers[choice - 1]['name']
                print(f"Selected: {selected_rover}")
                return selected_rover
            else:
                # choice out of range, need valid range
                print(f"Please enter a number between 1 and {len(rovers) + 1}")
        except ValueError:
            # Handling non-integer input
            print("Please enter a valid number")

def get_date():
    return input("Enter a date (YYYY-MM-DD format): ") # Example: 2012-08-06

def get_photos(rover_name, date, api_key):

    # Fetching photos for a given rover & date from the NASA API 
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover_name.lower()}/photos?earth_date={date}&api_key={api_key}"
    
    # Let user know search in progress
    print(f"Searching for photos from {rover_name} on {date}...")
    
    try:
        # Make GET request to NASA API
        response = get(url)
        response.raise_for_status()
        
        #Extract photos array from JSON response defaulting to empty list if key missing
        photos = response.json().get('photos', [])

        # Display results
        print(f"Found {len(photos)} photos.")
        return photos # Returning list  of photo data
    
    except Exception as e:
        #Handle errors API request or JSON parsing
        print(f"Error fetching photos: {e}")
        return []
    
def display_photo_and_wait(url):
    # Helper function to display a photo and wait for user input before continuing
    display_photo(url)

    #Once user close the photo press any key to go back to menu options
    input("Press Enter to continue...")

# Shows a menu of available photos for the user to select and view
def show_photo_menu(photos, rover_name, date):
    
    # first  check if photos are available
    if not photos:
        input("No photos available for this date. Press Enter to continue...")
        return
    
    # Build list of menu options for each photo max 10
    photos_to_show = photos[:10] # using list slicing to limit display of 10 max photos

    # Letting user know about photo count and display limirs
    print(f"Showing first {len(photos_to_show)} of {len(photos)} total photos")
    
    # Building list of menu options foe  each photo
    photo_options = []
    for photo in photos_to_show:

        # Extracing metadata fr menu display 
        camera_name = photo['camera']['full_name']
        photo_id = photo['id']
        option_text = f"Photo ID {photo_id} ({camera_name})"
        
        # Use a lambda to pass the display_photo_and_wait function with the specific URL
        photo_options.append((option_text, lambda url=photo['img_src']: display_photo_and_wait(url)))
    
    # Adding exit option to return tomain menu
    photo_options.append(("Return to Main Menu", Menu.CLOSE))
    
    #Create and display the  photoselction menu
    photo_menu = Menu(
        options=photo_options,
        title=f"{rover_name} Photos - {date}"
    )
    photo_menu.open() #Starting intreactive menu

# Main function to search and display Mars rover photos
def search_mars_photos():
    
    #Acessing global variables 
    global rovers_list, API_KEY

    # First let user select a rover from options
    selected_rover = select_rover(rovers_list)
    
    # check if user chosen toreturn to main menu instead of selecting
    if selected_rover is None:
        return
    
    #get data input from user
    date = get_date()
    
    # fetch the photos from NASA API using selected rover and date
    photos = get_photos(selected_rover, date, API_KEY)

    # Display photo menu  for viewing
    show_photo_menu(photos, selected_rover, date)

    # Returning a close signal to exit the current menu
    return Menu.CLOSE

# Main application function and loop
def mars_rover_app():
    
    # Creating the actual app menu with options available
    main_menu = Menu(
        options=[
            ("Search Mars Rover Photos", search_mars_photos), #Start photo search
            ("Exit", Menu.CLOSE) # close app
        ],
        title="NASA Mars Rover Photos" # App title
    )
    #start the system
    main_menu.open()

    #once user exit display Goodbye!
    print("Goodbye!")

# start the app
mars_rover_app()