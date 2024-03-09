import os 
import shutil

def dirmk(path=""):
    
    if path == "":
        directory = os.getcwd()
    else:
        os.chdir(path)
        directory = path
       
    files = os.listdir()
    
    extension = ""
    
    for file in files:
        
        isfile = os.path.isfile(file)
        
        if isfile == True:
            file_name = file.split(".")
            extension += f"{file_name[-1]},"
    
    extension = extension.split(",")
    extension.remove("")

    for dir in set(extension):
        
        try:
            os.mkdir(dir.capitalize())       
        except FileExistsError as err:
            print(err)
        except ValueError as err:
            print(err)
        except Exception as err:
            print(err)
            
    for move in files:
        
        issfile = os.path.isfile(move)
        
        if issfile == True:
            moves_file = move.split(".")
            move_file = moves_file[-1]
            
            try:
                shutil.move(f"{directory}/{move}",f"{directory}/{move_file.capitalize()}/{move}")
            except FileNotFoundError as err:
                print(err)
            except FileExistsError as err:
                print(err)
            except Exception as err:
                print(err)
    
        
if __name__ == "__main__":
    print("Path defult at working directory")
    dirmk(path= input("Path >> "))
    print("Done!")
    input()