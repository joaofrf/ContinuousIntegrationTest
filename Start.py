#import requests and sys
import requests
import sys

#Get request from url
def getRequest(url):
    response = requests.get(url)
    return response.text

#Method to get substring by indexof starting string and indexof ending string.
def getSubstring(string, start, end):
    return string[start:end].strip()


#Check if string contains a substring
def contains(string, substring):
    return string.find(substring) != -1


#Main init function for the program.
def main():
    print("Test Request!")
    result = getRequest(url="http://www.bitcliq.com") #Call getRequest function
    print(getSubstring(result, result.find("<title>")+7, result.find("</title>"))) #Call getSubstring function
    print(contains(result, "Bitcliq")) #Call contains function


if __name__ == "__main__":
    main()