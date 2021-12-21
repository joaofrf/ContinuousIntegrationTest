import Start


#test method for getRequest()
def TestGetRequest(url):
    result = Start.getRequest(url)
    assert result and not result.isspace()
    print("TestGetRequest() OK!")

#test method for getSubstring()
def TestGetSubstring():
    str = "String to test"
    result = Start.getSubstring(str, str.find("String")+len("String"), str.find("test"))
    assert result.strip() == "to"
    print("TestGetSubstring() OK!")

#test method for contains()
def TestContains():
    str = "321Bitcliq123"
    assert Start.contains(str, "Bitcliq")
    print("TestContains() OK!")

def RunTests():
    TestGetRequest("http://www.bitcliq.com")
    TestGetSubstring()
    TestContains()


if __name__ == "__main__":
    RunTests()