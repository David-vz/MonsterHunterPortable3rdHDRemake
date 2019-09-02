# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 0  
    file1 = open("list.txt","w")
    L = ["This is Delhi \n","This is Paris \n","This is London \n"]
    # \n is placed to indicate EOL (End of Line) 


    
    listDir = os.listdir("rename")
	
    for filename in listDir: 
        dst = str(i+1) + ".png"
        src = 'rename/' + filename 
        dst = 'rename/' + dst 
        os.rename(src, dst)
		
        file1.write(os.path.splitext(filename)[0] + " = " + str(i+1) + ".png \n")
        # rename() function will 
        # rename all the files 
         
        i += 1
		
    file1.close() #to change file access modes 
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 