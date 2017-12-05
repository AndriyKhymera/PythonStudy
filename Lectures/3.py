import requests
import  time
import random

# def print_current_time():

def get_request_to(URL):
    return requests.get(URL)


def main():
    for i in range(0, 5):
        time.sleep(random.randint(0, 5))
        print (get_request_to("http://google.com"))

def checKArray(*URL_array):
    for url in URL_array:
        try:
            res = get_request_to(url)
            if(res.status_code == 200):
                print ("url: {} is okay".format(url))
        except:
            print ("url: {} is bad".format(url))

def print_file(path_to_file):
    with open(path_to_file, "r") as file:
        print (file.read())


URL_ARR={
    "http://google.com",
    "http://wikipedia.org",
    "http://qealksdjlasj.com",
    "http://yahoo.com"
}

print_file("3_lecture_json_example.json")
# checKArray(*URL_ARR)
# main()

# if __name__ == "__main__":
#     main()