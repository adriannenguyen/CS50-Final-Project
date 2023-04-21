import os
import re
import urllib
import requests
from datetime import datetime
from dotenv import load_dotenv

# load .env file
load_dotenv()

class UserInput:
    """
    Class representing user's input and NASA API key.
    """
    def __init__(self, user_input: str, api_key: str):
        self.user_input = user_input
        self.api_key = api_key

    @classmethod
    def get(cls):
        """
        Get NASA API key from environment variable
        and user's date input.
        """
        try:
            api_key = os.getenv("NASA_API_KEY")
        except KeyError:
            raise Exception("NASA_API_KEY environment variable not set.")

        user_input = get_user_input()

        return cls(user_input, api_key)

def main():
    """
    Main function for running code.
    """
    try:
        user_input = UserInput.get()
        apod_url, apod_title = get_apod(
            validate_date(user_input.user_input), user_input.api_key)
        apod_ext = os.path.splitext(apod_url)[1]
        urllib.request.urlretrieve(
            apod_url, os.path.join(make_dir(), f"{apod_title}{apod_ext}"))
    except Exception as e:
        print(f"Error: {e}")

def get_user_input():
    """
    Prompt user for date input and validate it,
    reprompting if it is invalid.
    """
    while True:
        user_input = input("YYYY-MM-DD: ")
        try:
            validate_date(user_input)
            return user_input
        except Exception as e:
            print(f"Error: {e}")

def validate_date(user_input: str):
    """
    Validate user input date format is correct,
    is not in the future, and is not too far into the past.
    """
    if not re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", user_input):
        raise ValueError("Invalid Date. Incorrect format.")

    today_obj = datetime.today()
    date_obj = datetime.strptime(user_input, "%Y-%m-%d")
    min_obj = datetime.strptime("1995-06-16", "%Y-%m-%d")

    if date_obj > today_obj:
        raise ValueError("Invalid Date. Cannot obtain APOD for a future date.")
    elif date_obj < min_obj:
        raise ValueError("Invalid Date. Cannot obtain APOD before 1995-06-16.")
    return user_input

def get_apod(user_input: str, api_key: str) -> str:
    """
    Get NASA Astronomy Picture of the Day (APOD) URL
    and title based on user's input.
    """
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={user_input}")
    response_data = response.json()
    apod_url = response_data["url"]
    apod_title = response_data["title"].replace(" ", "_").replace(":", "_").replace(",", "_")
    return apod_url, apod_title

def make_dir():
    """
    Create a directory for APOD images.
    """
    apod_dir = "Astronomy Picture of the Day"
    if os.path.exists(apod_dir) == False:
        os.mkdir(apod_dir)
    return apod_dir

if __name__ == "__main__":
    main()
