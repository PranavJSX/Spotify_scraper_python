import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def scrap_function(website):
    res = requests.get(website)
    print(res.text)
    print(res.status_code)
    print(res.content)


if __name__ == '__main__':
    print_hi('PyCharm')
    website = input("Enter the website url : ")
    scrap_function(website)



