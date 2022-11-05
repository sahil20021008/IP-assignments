# Name - Sahil Goyal
# Roll No - 2020326

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


# Write the code here for creating an interactive program.
import waka

print("Hello!")
print("these are the possible queries for you to ask")
print('''
1. read_data_from_file
2. filter_by_first_name
3. filter_by_last_name
4. filter_by_full_name
5. filter_by_age_range
6. count_by_gender
7. filter_by_address
8. find_alumni
9. find_topper_of_each_institute
10. find_blood_donors
11. get_common_friends
12. is_related
13. delete_by_id
14. add_friend
15. remove_friend
16. add_education
''')
print("Which queries would you like to perform")

while True:
    c=int(input("please input an integer for a query code"))
    if c== (-1):
        break
    elif c==1:
        records=a2.read_data_from_file()
        print(records)
    elif c==2:
        d=input("please enter first name of person")
        a=a2.filter_by_first_name(records,d)
        print(a)
    elif c==3:
        d=input("please enter last name of person")
        a=a2.filter_by_last_name(records,d)
        print(a)
    elif c==4:
        d=input("please enter full name of person")
        a=a2.filter_by_full_name(records,d)
        print(a)
    elif c==5:
        d=int(input("please enter minimmum age"))
        e=int(input("please enter maximum age"))
        a=a2.filter_by_age_range(records,d,e)
        print(a)
    elif c==6:
        print("these are count of males and females")
        a=a2.count_by_gender(records)
        print(a)
    elif c==7:
        b={}
        d=input("please enter house no else leave blank")
        if d!="":
            b["house_no"]=int(d)
        e=input("please enter block else leave blank")
        if e!="":
            b["block"]=e
        f=input("please enter town else leave blank")
        if f!="":
            b["town"]=f
        g=input("please enter city else leave blank")
        if g!="":
            b["city"]=g
        h=input("please enter state else leave blank")
        if h!="":
            b["state"]=h
        j=input("please enter pincode else leave blank")
        if j!="":
            b["pincode"]=int(j)
        a=a2.filter_by_address(records,b)
        print(a)
    elif c==8:
        print("please enter institute name")
        d=str(input()).upper()
        a=a2.find_alumni(records,d)
        print(a)
    elif c==9:
        print("these are toppers of each institute")
        a=a2.find_topper_of_each_institute(records)
        print(a)
    elif c==10:
        d=int(input("please enter id of receiver"))
        a=a2.find_blood_donors(records,d)
        print(a)
    elif c==11:
        d=input("please enter space separated integers")
        d=list(map(int,d.split()))
        a=a2.get_common_friends(records,d)
        print(a)
    elif c==12:
        d=int(input("enter first persons id"))
        e=int(input("enter second persons id"))
        a=a2.is_related(records,d,e)
        print(a)
    elif c==13:
        d=int(input("please enter id you want to delete"))
        records=a2.delete_by_id(records,d)
        print(records)
    elif c==14:
        d=int(input("enter first persons id"))
        e=int(input("enter second persons id"))
        records=a2.add_friend(records,d,e)
        print(records)
    elif c==15:
        d=int(input("enter first persons id"))
        e=int(input("enter second persons id"))
        records=a2.remove_friend(records,d,e)
        print(records)
    elif c==16:
        d=int(input("please enter person id"))
        e=input("please enter institute name")
        f=input("please enter ongoing status")
        if f[0]=="F" or f[0]=="f":
            g=float(input("please enter percentage"))
            records=a2.add_education(records,d,e,False,g)
        else:
            g=0
            records=a2.add_education(records,d,e,True,g)
        print(records)
        

        
print("We hope your queries were answered")