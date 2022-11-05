'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions. 

- You MUST complete the functions defined below, except the ones that are already defined. 
'''
tdict={
    '0' : "Tshirt",
    '1' : "Trousers",
    '2' : "Scarf",
    '3' : "Smartphone",
    '4' : "iPad",
    '5' : "Laptop",
    '6' : "Eggs",
    '7' : "Chocolate",
    '8' : "Juice",
    '9' : "Milk"
}
mdict={
    '0': "500",
    '1': "600",
    '2': "250",
    '3': "20000",
    '4': "30000",
    '5': "50000",
    '6': "5",
    '7': "10",
    '8': "100",
    '9': "45"
}


def bulornot():
        print('Would you like to buy in bulk? (y or Y / n or N):')
        c=str(input())
        if c=='y' or c=='Y':
            return True
        elif c=='n' or c=='N':
            return False
        else:
            return bulornot()

def show_menu():
    print('''
    =================================================
                       MY BAZAAR
    =================================================
    Hello! Welcome to my grocery store!
    Following are the products available in the shop:

    -------------------------------------------------
    CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
    -------------------------------------------------
      0  | Tshirt      | Apparels     | 500
      1  | Trousers    | Apparels     | 600
      2  | Scarf       | Apparels     | 250
      3  | Smartphone  | Electronics  | 20,000
      4  | iPad        | Electronics  | 30,000
      5  | Laptop      | Electronics  | 50,000
      6  | Eggs        | Eatables     | 5
      7  | Chocolate   | Eatables     | 10
      8  | Juice       | Eatables     | 100
      9  | Milk        | Eatables     | 45
    ------------------------------------------------
    ''')
    


def get_regular_input():
    
    print('''
    -------------------------------------------------
    ENTER ITEM AND QUANTITIES
    -------------------------------------------------
          ''')
    a=[]
    print("Enter the item codes (space-separated):")
    a.append(input().split())
    n=len(a[0])
    o=0
    while o<n:
        if int(a[0][o])<0 or int(a[0][o])>9:
            print("Invalid Code")
            break
        o+=1
    b=['0','0','0','0','0','0','0','0','0','0']
    i=0
    while i<10:
        j=0
        count=0
        while j<n:
            if i==int(a[0][j]):
                count+=1
            j+=1
        b[i]=str(count)
        i+=1
    b=[int(r) for r in b]
    return b

def get_bulk_input():
    print('''
    -------------------------------------------------
    ENTER ITEM AND QUANTITIES
    -------------------------------------------------
    ''')
    a=[]
    while True:
        print("Enter code and quantity (leave blank to stop):")
        try:
            c,d=input().split()
            e=[c,d]
            if (int(c)>9 or int(c)<0) and (int(d)<0):
                print("Error: Invalid Code and Quantity")
            elif int(c)>9 or int(c)<0:
                print("Error: Invalid Code")
            elif int(d)<0:
                print("Error: Invalid Quantity")
            else:
                print("You added "+str(d)+" "+tdict[str(c)])
        except ValueError:
            print("Your code has been finalized")
            break
        if int(c)<=9 and int(c)>=0 and int(d)>=0:
            a.append(e)
    b=['0','0','0','0','0','0','0','0','0','0']
    i=0
    n=len(a)
    while i<10:
        j=0
        count=0
        while j<n:
            if i==int(a[j][0]):
                count+=int(a[j][1])
            j+=1
        b[i]=str(count)
        i+=1
    b=[int(r) for r in b]
    return b
    


def print_order_details(quantities):
    print('''
    -------------------------------------------------
    ORDER DETAILS
    -------------------------------------------------
    ''')
    n=len(quantities)
    i=0
    t=0
    count=0
    while i<n:
        if int(quantities[i])!=0:
            print("["+str(int(t)+int(1))+"] "+tdict[str(i)]+" * "+str(quantities[i])+" = Rs "+mdict[str(i)]+" * "+str(quantities[i])+" = Rs "+str(int(mdict[str(i)])*int(quantities[i])))
            t+=1
        count+=int(mdict[str(i)])*int(quantities[i])
        i+=1
    print("TOTAL COST = "+str(count))
    


def calculate_category_wise_cost(quantities):
    app=0
    elec=0
    eat=0
    print('''
    -------------------------------------------------
    CATEGORY-WISE COST
    -------------------------------------------------
    ''')
    i=0
    n=len(quantities)
    while i<n:
        if i>=0 and i<=2:
            app=app+int(quantities[i])*int(mdict[str(i)])
        elif i>=3 and i<=5:
            elec+=int(quantities[i])*int(mdict[str(i)])
        else:
            eat+=int(quantities[i])*int(mdict[str(i)])
        i+=1
    if app!=0:
        print("Apparels = Rs "+str(app))
    if elec!=0:
        print("Electronics = Rs "+str(elec))
    if eat!=0:
        print("Eatables = Rs "+str(eat))
    ze=(app,elec,eat)
    return ze


def get_discount(cost, discount_rate):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    print('''
    -------------------------------------------------
    DISCOUNTS
    -------------------------------------------------
    ''')
    a=get_discount(apparels_cost,0.1)
    b=get_discount(electronics_cost,0.1)
    c=get_discount(eatables_cost,0.1)
    if apparels_cost>=2000:
        print('[APPAREL] Rs '+str(apparels_cost)+" - Rs "+str(a)+" = Rs "+str(apparels_cost-a))
    else:
        a=0
    
    if electronics_cost>=25000:
        print('[ELECTRONICS] Rs '+str(electronics_cost)+" - Rs "+str(b)+" = Rs "+str(electronics_cost-b))
    else:
        b=0
    
    if eatables_cost>=500:
        print('[EATABLES] Rs '+str(eatables_cost)+" - Rs "+str(c)+" = Rs "+str(eatables_cost-c))
    else:
        c=0
    print("TOTAL DISCOUNT = Rs "+str(a+b+c))
    print("TOTAL COST = Rs " +str(apparels_cost+electronics_cost+eatables_cost-a-b-c))
    
    ze=(apparels_cost-a,electronics_cost-b,eatables_cost-c)
    return ze
    


def get_tax(cost, tax):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):


    print('''
    -------------------------------------------------
    TAX
    -------------------------------------------------
    ''')
    a=get_tax(apparels_cost,0.1)
    b=get_tax(electronics_cost,0.15)
    c=get_tax(eatables_cost,0.05)
    d=a+b+c
    if apparels_cost!=0:
        print("[APPAREL] Rs "+str(apparels_cost)+" * 0.10 = Rs "+str(a))
    if electronics_cost!=0:
        print("[ELECTRONICS] Rs "+str(electronics_cost)+" * 0.15 = Rs "+str(b))
    if eatables_cost!=0:
        print("[EATABLES] Rs "+str(eatables_cost)+" * 0.05 = Rs "+str(c))
    print("TOTAL TAX = Rs "+str(d))
    print("TOTAL COST = Rs "+str(d+apparels_cost+electronics_cost+eatables_cost))
    ze=(d+apparels_cost+electronics_cost+eatables_cost,d)
    return ze
    

def apply_coupon_code(total_cost):
   
    print('''
    -------------------------------------------------
    COUPON CODE
    -------------------------------------------------
    ''')
    while True:
        print("Enter coupon code (else leave blank):")
        c=input()
        if c=="HELLE25" or c=="CHILL50":
            break
        elif c=="":
            print("No coupon code applied.")
            print("TOTAL COUPON DISCOUNT = Rs 0")
            print("TOTAL COST = Rs "+str(total_cost))
            a=(total_cost,0)
            return a
        else:
            print("Invalid coupon code. Try again.")
    d=0    
    if c=="HELLE25":
        if total_cost>=25000:
            d=min(5000,total_cost*0.25)
            print("[HELLE25] min(5000, Rs "+str(total_cost)+" * 0.25) = Rs "+str(d))
    if c=="CHILL50":
        if total_cost>=50000:
            d=min(10000,total_cost*0.5)
            print("[CHILL50] min(10000, Rs "+str(total_cost)+" * 0.5) = Rs "+str(d))
    print("TOTAL COUPON DISCOUNT = Rs "+str(d))
    print("TOTAL COST = Rs "+str(total_cost-d))
    a=(total_cost-d,d)
    return a


def main():
    show_menu()
    a=[]
    if bulornot()==True:
        a=get_bulk_input()
    else:
        a=get_regular_input()
    print_order_details(a)
    z=calculate_category_wise_cost(a)
    t=calculate_discounted_prices(z[0],z[1],z[2])
    p=calculate_tax(t[0],t[1],t[2])
    r=apply_coupon_code(p[0])
    print("Thank you for visiting!")


if __name__ == '__main__':
	main()
