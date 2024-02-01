# HW8.py
# Author: James Railey Cabrera

# This homework will exapnd upon the code for Lab9.py. If you did not complete Lab9.py, you should do so before attempting this homework.

# Copy the code from Lab9.py into this file. I'll add some comments to help you out.


# Import statements (activate venv and install streamlit if you haven't already)
import streamlit as st
import datetime as dt

# Streamlit title, subtitle, date, and button

st.title("Webby Applicationy")
st.subheader("Days until...") 
date = st.date_input("enter a date: ")
calculate_button = st.button("Calculate")
new_years_button = st.button("Days until New Year's Day")
end_of_semester_button = st.button("Days until the end of the semester")
birthday_button = st.button("Days until your birthday")

# The calculate_days function from Lab9.py

def calculate_days(date) -> int:
    current_datetime = dt.datetime.now()
    current_date = current_datetime.date()
    days_difference = (date - current_date).days
    return days_difference

# START OF HOMEWORK Questions

# 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday.
# The function should take in the user's birthday as a parameter and return the number of days until their birthday. 
# The function should also display the number of days until their birthday in the Streamlit app. 
# The function should be called in the app function.
def calculate_days_until_birthday(birthday: dt.date) -> int:
    current_date = dt.datetime.now().date()
    days_difference = (birthday - current_date).days
    return days_difference

# 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester.
#  The function should take in the current date as a parameter and return the number of days until the end of the semester.
#  The function should also display the number of days until the end of the semester in the Streamlit app. 
# The function should be called in the app function.
# Hint: You can use the date object to create a date for the end of the semester. IE.
# end_of_semester = dt.date(2023, 12, 8)

def days_until_semester_ends(current_date: dt.date) -> int:
    end_of_semester = dt.date(2023, 12, 8)
    days_difference = (end_of_semester - current_date).days
    return days_difference
# 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. The function should take in the current date as a parameter and return the number 
# of days until New Year's Day. The function should also display the number of days until New Year's Day in the Streamlit app. 
# The function should be called in the app function. Also includean emoji of a party popper in the Streamlit app.
# Hint: You can use the date object to create a date for New Years. IE. 
# new_years = dt.date(2024, 1, 1)
# Hint: To add an emoji, use the st.write() function. IE. st.write("🎉")
def days_until_new_years(current_date: dt.date) -> int:
    new_years = dt.date(2024, 1, 1)
    days_difference = (new_years - current_date).days
    return days_difference

# 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day".
#  The button should call the days_until_new_years function when clicked.
#  The button should be placed below the "Calculate" button.Inside the app function call the days_until_new_years function when the button is clicked.

# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date. 
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉


# app function from Lab9.py
def app():
    if calculate_button:
        try:
            result = calculate_days(date)
            st.write("Number of days until the entered date:", result)
        except ValueError:
            st.write("Wrong date")
            return
        st.write(f"current date: {dt.datetime.now().date()}")
        st.write(f"target date: {date}")
        st.write(f"days until target date: {result}")

    if birthday_button:
        result_birthday = calculate_days_until_birthday(date)
        st.write("Number of days until your birthday:", result_birthday)

    if end_of_semester_button:
        result_semester = days_until_semester_ends(date)
        st.write("Number of days until the end of the semester:", result_semester)

    if new_years_button:
        result_new_year = days_until_new_years(date)
        st.write("Number of days until New Year's Day:", str(result_new_year) + "🎉")
    


if __name__ == '__main__':
    app()