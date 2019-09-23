import sys
#Add path to PATH
sys.path.insert(0,'../x86')

from Deliverable import DELIVERABLE

new_deliverable = DELIVERABLE()


#Initialize
new_deliverable.Remove_Dir()
new_deliverable.Make_Dir()
    
#Infinite Loop
new_deliverable.Run_Forever()


print(pygameWindow)