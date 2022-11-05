# Assignment - 2
# Name - Sahil Goyal
# Roll No - 2020326

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''


def read_data_from_file(file_path="data.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):

    a=[]
    for i in records:
        if first_name.lower()==i["first_name"].lower():
            a.append(i["id"])
    return a


def filter_by_last_name(records, last_name):
    
    a=[]
    for i in records:
        if last_name.lower()==i["last_name"].lower():
            a.append(i["id"])
    return a


def filter_by_full_name(records, full_name):
    
    a=[]
    for i in records:
        b=i["first_name"]+" "+i["last_name"]
        if full_name.lower()==b.lower():
            a.append(i["id"])
    return a
        


def filter_by_age_range(records, min_age, max_age):
    

    a=[]
    for i in records:
        b=i["age"]
        if b>=min_age and b<=max_age:
            a.append(i["id"])
    return a


def count_by_gender(records):

    c1=0
    c2=0
    for i in records:
        if i["gender"]=="male":
            c1+=1
        elif i["gender"]=="female":
            c2+=1
    d={
        "male":c1,
        "female":c2
    }
    return d


def filter_by_address(records, address):
    
    if address=={}:
        return records
    a=[]
    for i in records:
        f=True
        for j in address:
            if j=="house_no" or j=="pincode":
                if i["address"][j]!=address[j]:
                    f=False
                    break
            else:
                if str(i["address"][j]).lower()!=str(address[j]).lower():
                    f=False
                    break
        if f==True:
            b={
                "first_name":i["first_name"],
                "last_name":i["last_name"]
            }
            a.append(b)
    return a
                


def find_alumni(records, institute_name):
    
    a=[]
    for i in records:
        n=len(i["education"])
        for j in range(n-1,-1,-1):
            if i["education"][j]["institute"].lower()==institute_name.lower():
                if i["education"][j]["ongoing"]==False:
                    b={
                        "first_name":i["first_name"],
                        "last_name":i["last_name"],
                        "percentage":i["education"][j]["percentage"]
                    }
                    a.append(b)
                    break
                    
    return a

def find_topper_of_each_institute(records):
    
    a=[]
    for i in records:
        for j in i["education"]:
            if j["institute"] not in a:
                a.append(j["institute"])
    b={}
    for to in a:
        m=0
        it=0
        for i in records:
            n=len(i["education"])
            for j in range(n-1,-1,-1):
                if to==i["education"][j]["institute"]:
                    if i["education"][j]["ongoing"]==False and m<i["education"][j]["percentage"]:
                        m=i["education"][j]["percentage"]
                        it=i["id"]
                        break
        b[to]=it
    return b
    


def find_blood_donors(records, receiver_person_id):
    
    a={}
    for j in records:
        if j["id"]==receiver_person_id:
            b=j["blood_group"]
            break
    for i in records:
        if i["id"]!=receiver_person_id:
            if b=="O":
                if i["blood_group"]=="O":
                    a[i["id"]]=i["contacts"]
            elif b=="A":
                if i["blood_group"]=="A" or i["blood_group"]=="O":
                    a[i["id"]]=i["contacts"]
            elif b=="B":
                if i["blood_group"]=="B" or i["blood_group"]=="O":
                    a[i["id"]]=i["contacts"]
            else:
                a[i["id"]]=i["contacts"]
    return a
    
def inter(records,i1,ls):
    for i in records:
        if i["id"]==i1:
            a=i
            break
    c=[]
    for b in ls:
        if b in a["friend_ids"]:
            c.append(b)
    return c

def get_common_friends(records, list_of_ids):
    
    for i in records:
        if list_of_ids[0]==i["id"]:
            a=i["friend_ids"]
            break
    for j in list_of_ids:
        a=inter(records,j,a)
    return a
    

def is_related(records, person_id_1, person_id_2):
    
    for i in records:
        if i["id"]==person_id_1:
            a=i["friend_ids"]
            break
    for b in a:
        for j in records:
            if j["id"]==b:
                for k in j["friend_ids"]:
                    if k not in a:
                        a.append(k)
                break
    if person_id_2 in a:
        return True
    else:
        return False


def delete_by_id(records, person_id):

    c=records
    for i in c:
        if i["id"]==person_id:
            for j in i["friend_ids"]:
                for k in c:
                    if j==k["id"]:
                        k["friend_ids"].pop(k["friend_ids"].index(i["id"]))
                        break
            c.pop(c.index(i))
            break
    return c
        


def add_friend(records, person_id, friend_id):
    
    for i in records:
        if i["id"]==person_id:
            if friend_id not in i["friend_ids"]:
                i["friend_ids"].append(friend_id)
        if i["id"]==friend_id:
            if person_id not in i["friend_ids"]:
                i["friend_ids"].append(person_id)
    return records


def remove_friend(records, person_id, friend_id):
    
    for i in records:
        if i["id"]==person_id:
            if friend_id in i["friend_ids"]:
                i["friend_ids"].pop(i["friend_ids"].index(friend_id))
        if i["id"]==friend_id:
            if person_id in i["friend_ids"]:
                i["friend_ids"].pop(i["friend_ids"].index(person_id))
    
    return records


def add_education(records, person_id, institute_name, ongoing, percentage):

    for i in records:
        if i["id"]==person_id:
            if ongoing==False:
                b={
                    "institute":institute_name.upper(),
                    "ongoing":ongoing,
                    "percentage":percentage
                }
            else:
                b={
                    "institute":institute_name.upper(),
                    "ongoing":ongoing
                }
            i["education"].append(b)
            break
    return records

