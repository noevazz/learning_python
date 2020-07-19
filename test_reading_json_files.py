import json

def deserialization_with_file(path): # deserialization = decode = read
    with open(path) as json_file:
        result = json.load(json_file)
        print(result, type(result))
        #for a in result:
            #print(a)
def deserialization_with_string(string):
	print(json.loads(string))

if __name__ == "__main__":
    path = "./json_file.json"
    deserialization_with_file(path)

    string= """
    {
        "name":"noe",
        "pets": ["taro", "ptomo"]
    }
    """
    deserialization_with_string(string )