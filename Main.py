# Note : 1. As given in the question, taking the entering customers sequentially as an input at the run time and allocating the best possible table. 
#        2. Allocating a single table if remaining seats in the allocated table are less than or equal to 2 after allocation. Else allocate 
#           (i) best possible table/sequentially clubbed tables (or) (ii) possibly clubbed tables.
from Table_Booking import Table_Booking
def main():
    tabless=[6,2,6,4,4,4,2,2]  # Input list of tables and number of seats per table
    table=Table_Booking(tables=tabless)  # table is the object of class Table_Booking
    while True:
        print("-"*65)
        c=int(input("Enter number of customers:")) # Positive number of customers to be entered
        if c<1:
            print("Invalid!! Please enter valid number of customers")
            continue
        if len(set(table.tables))==1 and table.tables[0]==-1:
            print("-----All seats are booked-----")
            break
        if c not in table.tables:
            state=table.allocate(c)   # To check whether a single table can be allocated
            if state==True:
                print(" ")
            elif len(table.tables)>=1:    # Best possible table allocation / Best possible clubbed tables allocation
                if table.allocate_sequentially_clubbed_tables(c) is False:
                    if table.allocate_possible_tables(c) is False:
                        print("Cannot allocate, Either all the tables are booked or Capacity not enough !!!")
                        continue
                    else:
                        list_of_tables=table.allocate_possible_tables(c)
                        print("*** Possible allocated tables are : " , end=" ")
                        for i in range(len(list_of_tables)):
                            if i<len(list_of_tables)-1:
                                print(list_of_tables[i]+1,end=" , ")
                            else:
                                print(list_of_tables[i]+1, end=" ")
                            table.tables[list_of_tables[i]]=-1
                        print("***")
                        print(table.tables)
                else:
                    [idx1,idx2]=table.allocate_sequentially_clubbed_tables(c)
                    for j in range(idx1-1,idx2):
                        table.tables[j]=-1
                    print(table.tables)
                    if idx1!=idx2:
                        print("*** Best possible tables from", idx1 , "to", idx2, "are allocated ***")
                    else:
                        print("*** Best possible table", idx2, "is allocated ***")
        else:
            table.allocate(c)
        print(" ")
        exit=input("Do you want to exit? y/n: ")
        if exit.lower()=='y':
            print(" ")
            print("-----Exiting------")
            break

if __name__=='__main__':
    main()