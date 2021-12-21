import Start

ResultFile = 'test-results'

#Save to file
def SaveToFile(Result):
    file = open(ResultFile, "w")
    file.write(Result + "\n")
    file.close()
    print(Result)

#test method for getRequest()
def TestGetRequest(url):
    result = Start.getRequest(url)
    assert result and not result.isspace()
    SaveToFile("TestGetRequest() OK!")

#test method for getSubstring()
def TestGetSubstring():
    str = "String to test"
    result = Start.getSubstring(str, str.find("String")+len("String"), str.find("test"))
    assert result.strip() == "to"
    SaveToFile("TestGetSubstring() OK!")

#test method for contains()
def TestContains():
    str = "321Bitcliq123"
    assert Start.contains(str, "Bitcliq")
    SaveToFile("TestContains() OK!")

def RunTests():
    TestGetRequest("http://www.bitcliq.com")
    TestGetSubstring()
    TestContains()


if __name__ == "__main__":
    RunTests()