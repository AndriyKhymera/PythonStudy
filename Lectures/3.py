import requests

def main():
    res = requests.get("http://google.com")
    print (res.text)

main()

# if __name__ == "__main__":
#     main()