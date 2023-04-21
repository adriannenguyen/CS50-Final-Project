<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" />
</p>

# <p align="center"> NASA Astronomy Picture of the Day
## 🎥 Video Demo
<https://www.youtube.com/watch?v=Uny-0qB5-40>
## 🌌 About the Project
NASA Astronomy Picture of the Day (APOD) is a simple program that prompts the user for a date, accesses NASA's APOD API to retrieve the APOD for the given date, and creates a folder containing the APOD image. Users can run the program as many times as they would like, as the APOD images will save into the same folder.

With the execption of File I/O (Week 6), this project essentially covers every topic covered in HarvardX CS50's Introduction to Programming with Python. In `project.py`, functions (Week 0), variables (Week 0), conditionals (Week 1), exceptions (Week 3) and libraries (Week 4) are incorporated throughout the entire program. A `while` loop (Week 2) is used in `get_user_input()` to continue reprompting the user until a date is inputted in the correct format. A regular expression (Week 7) is utilized in `validate_date(user_input: str)` to validate the user input matches the YYYY-MM-DD format. Object-oriented programming (Week 8) is used to define a class with instance variables and methods for retrieving them.
Additionally, function annotations (Week 9) are included in `validate_date(user_input: str)` and `get_apod(user_input: str, api_key: str) -> str`. Lastly, in `test_project.py`, unit tests (Week 5) are created to test each function in `project.py`.
## 📂 Project Files
- project.py - The main file that runs NASA's Astronomy Picture of the Day.
- test_project.py - The file that tests each function in project.py.
- requirements.txt - Where all `pip`-installable libraries used in the project reside.
- .env - Where your NASA API Key will reside as an environment variable.
## ✨ How it Works
First, obtain your [NASA API Key](https://api.nasa.gov/).

Next, create a `.env` file to store your NASA API Key.
```r
NASA_API_KEY={insert NASA API Key}
```
Run project.py.
```
$ python project.py
```
Once prompted, enter a date in YYYY-MM-DD format. For example, 1999-11-12 for November 12, 1999.
```
YYYY-MM-DD: 1999-11-12
```
The program will create a folder called "Astronomy Picture of the Day" with NASA's APOD image for the inputted date in it. The title for the image is the filename. Try as many dates as you would like!
## 🏆 Credits
💁🏻‍♀️ Adrianne Nguyen

📓 HarvardX CS50's Introduction to Programming with Python