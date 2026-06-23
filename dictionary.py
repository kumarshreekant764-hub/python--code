info = {
    "key": "value",
    "name": "shree",
    "learning": "python",
    "age": 25,
    "is_student": True,
    "marks" : 85.9,
    "subjects": ["math", "science", "english"],
    "topics" : ("data structures", "algorithms", "web development"),

}
#print(info)
#print(type(info))

#print the value of a specific key

#print(info["name"])
#print(info["subjects"])
#print(info["topics"])

#changing the value of a specific key

info["age"] = 26
info["is_student"] = False
info["name"] = "shree kant"
info["city"] = "New York" #adding a new key-value pair to the dictionary

#print(info)


#print the changed values of the specific keys

#print(info["age"])
#print(info["city"])
#print(info["is_student"])
#print(info["name"])




#__________________________________________________

#nested dictionary
student_info = {
    "name": "shree kant",
    "age": 26,
    "marks":{
        "math": 90,
        "science": 85,
        "english": 80,
        "history": 75
    }
}

#print(student_info) #printing the whole nested dictionary
#print(student_info["marks"]) #printing the nested dictionary in specific key
#print(student_info["marks"]["math"]) #printing the value of a specific key in nested dictionary


#dictionary methods

#print(student_info.keys()) #printing all the keys in the dictionary
#print(list(student_info.keys())) #printing all the keys in the dictionary in the form of a list
#print(len(student_info.keys())) #printing length of the dictionary

#print(student_info.values()) #printing all the values in the dictionary
#print(list(student_info.values())) #printing all the values in the dictionary in the form of a list

#print(student_info.items()) #printing all the key-value pairs in the dictionary
#print(list(student_info.items())) #printing all the key-value pairs in the dictionary in the form of a list
pairs = list(student_info.items())
#print(pairs[0]) #printing the first key-value pair in the dictionary
#print(pairs[1]) #printing the second key-value pair in the dictionary   

print(student_info.get("name")) #printing the value of a specific key using get() method
print(student_info.get("marks")) #printing the value of a specific key using get() method

student_info.update({"city": "New York"}) #adding a new key-value pair to the dictionary using update() method
print(student_info) #printing the whole dictionary after adding a new key-value pair    
