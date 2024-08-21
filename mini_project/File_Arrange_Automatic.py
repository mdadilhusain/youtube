#clear files clutter
import os 
#creating folder functions
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        
def move(folder_names , files):       
        for file in files:
            os.replace(file, f"{folder_names}/{files}")      
print("i am importing")
if __name__ == "__main__":

    files = os.listdir()
    files.remove("File_Arrange_Automatic.py")
    
    #create a folder (directory)
    createIfNotExist("Images")
    createIfNotExist("Docs")
    createIfNotExist("Medias")
    createIfNotExist("Others")
    
    
    ###    categorize files with help of these extensoions
    imgExts = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]


    docExts = [".txt", ".pdf", ".docx", "doc"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


    mediaExts = [".mp4", ".mp3" ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1]    #splittext (fucntion ) it is uesed for split extension
        if ((ext not in images) and (ext not in docExts) and (ext not in medias) and os.path.isfile(file)):
            others.append(file)
            
    #moving files into folders     
    move("Images",images)        
    move("Docs",docs)        
    move("Medias",medias) 
    move("Others",others)       

    print("Run successfully ....")
