# Lab4
# Author: james railey cabrera

"""_summary_
This lab is designed to get you familiar with Python virtual environments as well as import statments to use external libraries.
"""

# 1. Create a virtual environment called "venv" in the current directory. (Type command here in comments)
# python -m venv venv

# 2. Activate the virtual environment. (Type command here in comments)

# source venv/bin/activate
# 3. Install the requests library. (Type command here in comments)

# pip install requests
# 4. import requests library here

# import requests
# import requests as rq (to make it shorter)
# 5. Use the requests library to make a GET request to https://api.github.com/events
import requests
get = requests.get('https://api.github.com/events')
print (get)
# 6. Print out the status code of the response.
print(get.status_code)
# # 7. Print out the content of the response.
print(get.content)
# # 8. Print out the headers of the response.
print(get.headers)
# 9. Deactivate the virtual environment. (Type command here in comments)
# source venv/bin/deactivate
