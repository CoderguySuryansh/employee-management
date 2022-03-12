stud = []
c='y'
while c=='y':
    
    print("1. Add records:  ")
    print("2. Search records:  ")
    print("3. Update records:  ")
    print("4. Delete records:  ")
    print("5. Display records(individual / All):  ")
    n = int(input("Enter the choice:  "))
    if n==1:        
        ch = 'y'
        while ch=='y':
            print("********** IDA employee management ************* ")
            join = int(input("joining number:\t"))
            name = input("Name:\t")
            salary  = float(input("salary:\t"))
            stud_data = [join , name ,salary]  
            stud.append(stud_data)            
            ch = input("Wana add more..... 'y' / 'n' : ")
            
            
    elif n==2:
        a = len(stud)
                
        join = int(input(" Enter joining number:  ")) 
        flag = 0           
        for i in range(a):                    
                if stud[i][0]==join:
                    print("joining number: " , stud[i][0])
                    print("Name:   " , stud[i][1])
                    print("salary:    " , stud[i][2])
                    print()
                    flag=1
                    break
        if flag==0:
            print("Record not found:  ")
            
      
       
    elif n==3:
        a = len(stud)
        b='y'
        while b=='y':
            print(stud)
            print()
            
            join = int(input(" Enter joining number to update  choose:  'joining number  , Name & salary: '   "))
            flag = 0
              
            print("************ Details are here ************** ")
            for i in range(a):                
                if stud[i][0]==join:
                    print("joining number: " , stud[i][0])
                    print("Name:   " , stud[i][1])
                    print("salary:    " , stud[i][2])
                    print()
                    flag=1
                    print("1. joining number  2. Name  3. salary: ")
                    c = int(input("Enter the choice:  "))
                    if c==1:
                        if stud[i][0]==join:
                            print("joining  number: " , stud[i][0])
                            print("Name:   " , stud[i][1])
                            print("salary:    " , stud[i][2])
                            print()                           
                            new = int(input("Enter the new join number:  ")) 
                            stud[i][0]=new
                            print("joining number: " , stud[i][0])
                            print("Name:   " , stud[i][1])
                            print("salary:    " , stud[i][2])
                            print("****record is updated*******")
                            print()
                            break
                        
                    elif c==2:
                        nam = input("Enter the Name :  ")
                        
                        stud[i][1]=nam
                        print("joining number: " , stud[i][0])
                        print("Name:   " , stud[i][1])
                        print("salary:    " , stud[i][2])
                        print("****record is updated*******")
                        print()
                        break
                        
                        
                    elif c==3:
                        p = float(input("Enter the salary :  ")) 
                        stud[i][2]=p
                        print("joining number: " , stud[i][0])
                        print("Name:   " , stud[i][1])
                        print("salary:    " , stud[i][2])
                        print("****record is updated*******")
                        print()
                        break
                        
                    else:
                        print("Not found the option:  ")
                
            b = input("Want to do more updation:  'y'  /  'n'  ")            
                
            if flag==0:
                print("Record not found no updation allowed:  ")
                break
               
                   
    elif n==4:
        
        a = len(stud)
                
        join = int(input(" Enter joining number for deletion the details :  "))  
        flag = 0           
        for i in range(a):                    
                if stud[i][0]==join:                  
                    print("joining number: " , stud[i][0])
                    print("Name:   " , stud[i][1])
                    print("salary:    " , stud[i][2])
                    flag=1
                    
                    m = 'y'
                    m = input(" Press 'y' to delete or 'n' not to delete:  ")
                    if m=='y':
                        stud.pop(i)
                        print("Record has been deleted:  ")
                    break
                
                   
        if flag==0:
            print("Record not found:  ")
            
            
            
            
    elif n==5:
        a = len(stud)
        print("Choose the option:  1. Display all    2.  Display individual:  ")
        n = int(input(" Enter the choice:  "))
        if n == 1:
            for i in range(a):
                print("joining number: " , stud[i][0])
                print("Name:   " , stud[i][1])
                print("salary:    " , stud[i][2])
                print()
        else:
            join = int(input(" Enter joining number:  "))
            for i in range(a):
                if stud[i][0]==join:
                    print("joining number: " , stud[i][0])
                    print("Name:   " , stud[i][1])
                    print("salary:    " , stud[i][2])
                    print()
                    break    
                
            
            
        
   
        
        
    
    
    
    
    
    
    
    
    
    
    
















        
    



 
