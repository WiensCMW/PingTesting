import os

# https://stackoverflow.com/questions/26468640/python-function-to-test-ping
def check_ping():
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

pingResults = check_ping()

print(pingResults)
