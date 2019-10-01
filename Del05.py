import sys
#Add path to PATH
sys.path.insert(0,'../x86')

from Recorder import RECORDER

new_recorder = RECORDER()


#Initialize
new_recorder.Remove_Dir()
new_recorder.Make_Dir()
    
#Infinite Loop
new_recorder.Run_Forever()


print(pygameWindow)