#------------------------------------------#
# Title: CDInventory.py
# Desc: Script for Assignment05: Modification of starter script to use lists of dictionaries instead of lists, and completes TODOs
# Change Log: (John Czarnek, 21-Aug-08, Modified script to use lists of dictionaries and load and delete)
# DBiesinger, 21-Jan-01, Created File
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
#lstTbl = []  # list of lists to hold data
lstTbl = []
#lstRow = []  # list of data row
dicRow = {}
lstRow = []
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l':

        lstTbl=[]
        dicRpw = {}
        objF = open('newDataFile.txt', 'r')
        
        for row in objF:
            lstRow = row.strip().split(',')
            strID = lstRow[0]
            strTitle = lstRow[1]
            strArtist = lstRow[2]
            intID = int(strID)
            dicRow = {'id':intID,'title':strTitle,'artist':strArtist}
            lstTbl.append(dicRow)
        objF.close()
        
                
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        
        strID = input('Enter ID: ')
        strTitle = input('Enter Title: ')
        strArtist = input('Enter Artist: ')
        intID = int(strID)
        dicRow = {'id':intID,'title':strTitle,'artist':strArtist}
        lstTbl.append(dicRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row['id'],', ',row['title'],', ',row['artist'])
        
        
            
    elif strChoice == 'd':
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row['id'],', ',row['title'],', ',row['artist'])
        print()
        sel = int(input('Enter ID of CD to delete: '))
        tmpTbl = []
        for row in lstTbl:
            if row['id']!= sel:
                tmpTbl.append(row)
        lstTbl = tmpTbl

    elif strChoice == 's':

        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open('CDInventory.txt', 'w')
        for row in lstTbl:
           objFile.write(str(row['id'])+','+str(row['title'])+','+str(row['artist'])+'\n')
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

