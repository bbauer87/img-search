import os
from PIL import Image

def answer(x):
    while True:
        print("\n" + "-" * 100 + "\n")
        resp = input(">>>   ")
        if not resp.isdigit():
            print("\nChoose a option!\n")
            continue
        resp = int(resp)
        if resp < 1 or resp > x:
            print("\nInvalid option, try again.\n")
            continue
        print("\n" + "-" * 100 + "\n")
        return resp

def verif(path):
    img = Image.open(path)
    w, h = img.size
    img.close()
    return w,h

def specific(mydir,what_to_search,operation,extention,var_wid=0,var_hei=0):

    result=[]

    if what_to_search == "width and height": ## operation[0] width, operation[1] height
        print(f"\nSearching for {extention} files with width {operation[0]} {var_wid} and height {operation[1]} {var_hei}:\n")
        for file in os.listdir(mydir):
            if file.endswith(f".{extention}".lower()):
                search = verif(mydir+"\\"+file)
                if operation[0] == operation[1] == "equal":
                    if search[0] == var_wid and search[1] == var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "equal" and operation[1] == "less":
                    if search[0] == var_wid and search[1] < var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "equal" and operation[1] == "less or equal":
                    if search[0] == var_wid and search[1] <= var_hei:
                        result.append(mydir + "\\" + file)
                        continue
                
                if operation[0] == "equal" and operation[1] == "bigger":
                    if search[0] == var_wid and search[1] > var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "equal" and operation[1] == "bigger or equal":
                    if search[0] == var_wid and search[1] >= var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "equal" and operation[1] == "not":
                    if search[0] == var_wid and search[1] != var_hei:
                        result.append(mydir + "\\" + file)
                        continue
                    
#########################################################################################
                if operation[0] == "less" and operation[1] == "equal":
                    if search[0] < var_wid and search[1] == var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == operation[1] == "less":
                    if search[0] < var_wid and search[1] < var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "less" and operation[1] == "less or equal":
                    if search[0] < var_wid and search[1] <= var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "less" and operation[1] == "bigger":
                    if search[0] < var_wid and search[1] > var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "less" and operation[1] == "bigger or equal":
                    if search[0] < var_wid and search[1] >= var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "less" and operation[1] == "not":
                    if search[0] < var_wid and search[1] != var_hei:
                        result.append(mydir + "\\" + file)
                        continue
                
#########################################################################################
                if operation[0] == "less or equal" and operation[1] == "equal":
                    if search[0] <= var_wid and search[1] == var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "less or equal" and operation[1] == "less":
                    if search[0] <= var_wid and search[1] < var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == operation[1] == "less or equal":
                    if search[0] <= var_wid and search[1] <= var_hei:
                        result.append(mydir + "\\" + file)
                        continue
                
                if operation[0] == "less or equal" and operation[1] == "bigger":
                    if search[0] <= var_wid and search[1] > var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "less or equal" and operation[1] == "bigger or equal":
                    if search[0] <= var_wid and search[1] >= var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "less or equal" and operation[1] == "not":
                    if search[0] <= var_wid and search[1] != var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

#########################################################################################
                if operation[0] == "bigger" and operation[1] == "equal":
                    if search[0] > var_wid and search[1] == var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "bigger" and operation[1] == "less":
                    if search[0] > var_wid and search[1] < var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "bigger" and operation[1] == "less or equal":
                    if search[0] > var_wid and search[1] <= var_hei:
                        result.append(mydir + "\\" + file)
                        continue
                
                if operation[0] == operation[1] == "bigger":
                    if search[0] > var_wid and search[1] > var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "bigger" and operation[1] == "bigger or equal":
                    if search[0] > var_wid and search[1] >= var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "bigger" and operation[1] == "not":
                    if search[0] > var_wid and search[1] != var_hei:
                        result.append(mydir + "\\" + file)
                        continue
                    
#########################################################################################
                if operation[0] == "bigger or equal" and operation[1] == "equal":
                    if search[0] >= var_wid and search[1] == var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "bigger or equal" and operation[1] == "less":
                    if search[0] >= var_wid and search[1] < var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "bigger or equal" and operation[1] == "less or equal":
                    if search[0] >= var_wid and search[1] <= var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "bigger or equal" and operation[1] == "bigger":
                    if search[0] >= var_wid and search[1] > var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == operation[1] == "bigger or equal":
                    if search[0] >= var_wid and search[1] >= var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "bigger or equal" and operation[1] == "not":
                    if search[0] >= var_wid and search[1] != var_hei:
                        result.append(mydir + "\\" + file)
                        continue
                
#########################################################################################
                if operation[0] == "not" and operation[1] == "equal":
                    if search[0] != var_wid and search[1] == var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "not" and operation[1] == "less":
                    if search[0] != var_wid and search[1] < var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "not" and operation[1] == "less or equal":
                    if search[0] != var_wid and search[1] <= var_hei:
                        result.append(mydir + "\\" + file)
                        continue
                
                if operation[0] == "not" and operation[1] == "bigger":
                    if search[0] != var_wid and search[1] > var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == "not" and operation[1] == "bigger or equal":
                    if search[0] != var_wid and search[1] >= var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

                if operation[0] == operation[1] == "not":
                    if search[0] != var_wid and search[1] != var_hei:
                        result.append(mydir + "\\" + file)
                        continue                

    else:        
        if what_to_search == "width":            string = f"width {operation} {var_wid}"            
        if what_to_search == "height":           string = f"height {operation} {var_hei}"
        print(f"\nSearching for {extention} files with {string}:\n")
        
        for file in os.listdir(mydir):
            if file.endswith(f".{extention}".lower()):
                search = verif(mydir + "\\" + file)   
                if what_to_search == "width":
                    param = search[0]; comparison = var_wid
                    
                if what_to_search == "height":
                    param = search[1]; comparison = var_hei              
                
                if operation == "equal":
                    if param == comparison:
                        result.append(mydir + "\\" + file)
                        continue
                    
                if operation == "less":
                    if param < comparison:
                        result.append(mydir + "\\" + file)
                        continue
                    
                if operation == "less or equal":
                    if param <= comparison:
                        result.append(mydir + "\\" + file)
                        continue
                    
                if operation == "bigger":
                    if param > comparison:
                        result.append(mydir + "\\" + file)
                        continue
                
                if operation == "bigger or equal":
                    if param >= comparison:
                        result.append(mydir + "\\" + file)
                        continue
                    
                if operation == "not":
                    if param != comparison:
                        result.append(mydir + "\\" + file)
                        continue

    return result

                    
def recursive(mydir,what_to_search,operation,extention,var_wid=0,var_hei=0):

    result=[]

    if what_to_search == "width and height": ## operation[0] width, operation[1] height
        print(f"\nSearching for {extention} files with width {operation[0]} {var_wid} and height {operation[1]} {var_hei}:\n")
        for root, dirs, files in os.walk(mydir):
            for file in files:
                if file.endswith(f".{extention}".lower()):
                     search = verif(root + "\\" + file)
                     if operation[0] == operation[1] == "equal":
                        if search[0] == var_wid and search[1] == var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "equal" and operation[1] == "less":
                        if search[0] == var_wid and search[1] < var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "equal" and operation[1] == "less or equal":
                        if search[0] == var_wid and search[1] <= var_hei:
                            result.append(root + "\\" + file)
                            continue
                
                     if operation[0] == "equal" and operation[1] == "bigger":
                        if search[0] == var_wid and search[1] > var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "equal" and operation[1] == "bigger or equal":
                        if search[0] == var_wid and search[1] >= var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "equal" and operation[1] == "not":
                        if search[0] == var_wid and search[1] != var_hei:
                            result.append(root + "\\" + file)
                            continue
                    
#########################################################################################
                     if operation[0] == "less" and operation[1] == "equal":
                        if search[0] < var_wid and search[1] == var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == operation[1] == "less":
                        if search[0] < var_wid and search[1] < var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "less" and operation[1] == "less or equal":
                        if search[0] < var_wid and search[1] <= var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "less" and operation[1] == "bigger":
                        if search[0] < var_wid and search[1] > var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "less" and operation[1] == "bigger or equal":
                        if search[0] < var_wid and search[1] >= var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "less" and operation[1] == "not":
                        if search[0] < var_wid and search[1] != var_hei:
                            result.append(root + "\\" + file)
                            continue
                
#########################################################################################
                     if operation[0] == "less or equal" and operation[1] == "equal":
                        if search[0] <= var_wid and search[1] == var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "less or equal" and operation[1] == "less":
                        if search[0] <= var_wid and search[1] < var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == operation[1] == "less or equal":
                        if search[0] <= var_wid and search[1] <= var_hei:
                            result.append(root + "\\" + file)
                            continue
                
                     if operation[0] == "less or equal" and operation[1] == "bigger":
                        if search[0] <= var_wid and search[1] > var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "less or equal" and operation[1] == "bigger or equal":
                        if search[0] <= var_wid and search[1] >= var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "less or equal" and operation[1] == "not":
                        if search[0] <= var_wid and search[1] != var_hei:
                            result.append(root + "\\" + file)
                            continue                

#########################################################################################
                     if operation[0] == "bigger" and operation[1] == "equal":
                        if search[0] > var_wid and search[1] == var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "bigger" and operation[1] == "less":
                        if search[0] > var_wid and search[1] < var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "bigger" and operation[1] == "less or equal":
                        if search[0] > var_wid and search[1] <= var_hei:
                            result.append(root + "\\" + file)
                            continue
                
                     if operation[0] == operation[1] == "bigger":
                        if search[0] > var_wid and search[1] > var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "bigger" and operation[1] == "bigger or equal":
                        if search[0] > var_wid and search[1] >= var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "bigger" and operation[1] == "not":
                        if search[0] > var_wid and search[1] != var_hei:
                            result.append(root + "\\" + file)
                            continue
                    
#########################################################################################
                     if operation[0] == "bigger or equal" and operation[1] == "equal":
                        if search[0] >= var_wid and search[1] == var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "bigger or equal" and operation[1] == "less":
                        if search[0] >= var_wid and search[1] < var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "bigger or equal" and operation[1] == "less or equal":
                        if search[0] >= var_wid and search[1] <= var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "bigger or equal" and operation[1] == "bigger":
                        if search[0] >= var_wid and search[1] > var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == operation[1] == "bigger or equal":
                        if search[0] >= var_wid and search[1] >= var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "bigger or equal" and operation[1] == "not":
                        if search[0] >= var_wid and search[1] != var_hei:
                            result.append(root + "\\" + file)
                            continue
                
#########################################################################################
                     if operation[0] == "not" and operation[1] == "equal":
                        if search[0] != var_wid and search[1] == var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "not" and operation[1] == "less":
                        if search[0] != var_wid and search[1] < var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "not" and operation[1] == "less or equal":
                        if search[0] != var_wid and search[1] <= var_hei:
                            result.append(root + "\\" + file)
                            continue
                
                     if operation[0] == "not" and operation[1] == "bigger":
                        if search[0] != var_wid and search[1] > var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == "not" and operation[1] == "bigger or equal":
                        if search[0] != var_wid and search[1] >= var_hei:
                            result.append(root + "\\" + file)
                            continue                

                     if operation[0] == operation[1] == "not":
                        if search[0] != var_wid and search[1] != var_hei:
                            result.append(root + "\\" + file)
                            continue  

    else:
        if what_to_search == "width":            string = f"width {operation} {var_wid}"            
        if what_to_search == "height":           string = f"height {operation} {var_hei}"
        print(f"\nSearching for {extention} files with {string}:\n")
        
        for root, dirs, files in os.walk(mydir):
            for file in files:
                if file.endswith(f".{extention}".lower()):
                    search = verif(root + "\\" + file)               
                    if what_to_search == "width":
                        param = search[0]; comparison = var_wid
                        
                    if what_to_search == "height":
                        param = search[1]; comparison = var_hei
                        
                    if operation == "equal":
                        if param == comparison:
                            result.append(root + "\\" + file)
                            continue
                        
                    if operation == "less":
                        if param < comparison:
                            result.append(root + "\\" + file)
                            continue
                        
                    if operation == "less or equal":
                        if param <= comparison:
                            result.append(root + "\\" + file)
                            continue
                        
                    if operation == "bigger":
                        if param > comparison:
                            result.append(root + "\\" + file)
                            continue

                    if operation == "bigger or equal":
                        if param >= comparison:
                            result.append(root + "\\" + file)
                            continue
                        
                    if operation == "not":
                        if param != comparison:
                            result.append(root + "\\" + file)
                            continue
    return result

def menu():

    while True:
        print("\nSearch image files using width and/or height, in a specific folder or throught all sub-directories.\n")
        print("Options:\n\n[1] Specific folder\n[2] Recursive\n[3] Exit\n")
        option = answer(3)

        if option == 3:
            break

        if option == 2: ## recursive
            print("\nInsert the root directory - example: c:\\myfiles\n")
            mydir = input(">>> ")
            if not os.path.exists(mydir):
                print("\nDirectory not found, aborting...")
                print("\n" + "-" * 100 + "\n")
                continue

            print("\nInsert the format of image file - example: jpg, png, gif, bmp...\n")
            ext = input(">>> ").lower()
            if not ext:
                print("\nError, aborting...\n")
                print("\n" + "-" * 100 + "\n")
                continue
            print("\nOptions for search using:\n\n[1] Width and height\n[2] Width only\n[3] Height only\n[4] Return to main menu\n")
            option2 = answer(4)

            if option2 == 4:
                continue

            if option2 == 3: ## height only
                print("\nInsert a height value for comparison:\n")
                height = input(">>> ")
                if not height.isdigit():                    
                    print("\nError, aborting...\n")
                    print("\n" + "-" * 100 + "\n")
                    continue
                height = int(height)
                print(f"\nOptions of search:\n\n[1] Equal to {height}\n[2] Less then {height}\n[3] Less or equal to {height}\n[4] Bigger then {height}\n[5] Bigger or equal to {height}\n[6] Not equal to {height}\n[7] Return to main menu\n")
                oper = answer(7)

                if oper == 7:
                    continue

                if oper == 1: operation = "equal"
                if oper == 2: operation = "less"
                if oper == 3: operation = "less or equal"
                if oper == 4: operation = "bigger"
                if oper == 5: operation = "bigger or equal"
                if oper == 6: operation = "not"
                    
                final = recursive(mydir,"height",operation,ext,var_hei = height)

            if option2 == 2: ## width only
                print("\nInsert a width value for comparison:\n")
                width = input(">>> ")
                if not width.isdigit():                    
                    print("\nError, aborting...\n")
                    print("\n" + "-" * 100 + "\n")
                    continue
                width = int(width)
                print(f"\nOptions of search:\n\n[1] Equal to {width}\n[2] Less then {width}\n[3] Less or equal to {width}\n[4] Bigger then {width}\n[5] Bigger or equal to {width}\n[6] Not equal to {width}\n[7] Return to main menu\n")
                oper = answer(7)

                if oper == 7:
                    continue

                if oper == 1: operation = "equal"
                if oper == 2: operation = "less"
                if oper == 3: operation = "less or equal"
                if oper == 4: operation = "bigger"
                if oper == 5: operation = "bigger or equal"
                if oper == 6: operation = "not"
                    
                final = recursive(mydir,"width",operation,ext,var_wid = width)

            if option2 == 1: ## width and height
                print("\nInsert a width value for comparison:\n")
                width = input(">>> ")
                if not width.isdigit():                    
                    print("\nError, aborting...\n")
                    print("\n" + "-" * 100 + "\n")
                    continue
                width = int(width)
                
                print(f"\nOptions of search:\n\n[1] Equal to {width}\n[2] Less then {width}\n[3] Less or equal to {width}\n[4] Bigger then {width}\n[5] Bigger or equal to {width}\n[6] Not equal to {width}\n[7] Return to main menu\n")
                oper = answer(7)

                if oper == 7:
                    continue

                operation = []

                if oper == 1: operation.append("equal")
                if oper == 2: operation.append("less")
                if oper == 3: operation.append("less or equal")
                if oper == 4: operation.append("bigger")
                if oper == 5: operation.append("bigger or equal")
                if oper == 6: operation.append("not")
                
                print("\nInsert a height value for comparison:\n")
                height = input(">>> ")
                if not height.isdigit():                    
                    print("\nError, aborting...\n")
                    print("\n" + "-" * 100 + "\n")
                    continue
                height = int(height)
                
                print(f"\nOptions of search:\n\n[1] Equal to {height}\n[2] Less then {height}\n[3] Less or equal to {height}\n[4] Bigger then {height}\n[5] Bigger or equal to {height}\n[6] Not equal to {height}\n[7] Return to main menu\n")
                oper = answer(7)

                if oper == 7:
                    continue

                if oper == 1: operation.append("equal")
                if oper == 2: operation.append("less")
                if oper == 3: operation.append("less or equal")
                if oper == 4: operation.append("bigger")
                if oper == 5: operation.append("bigger or equal")
                if oper == 6: operation.append("not")
      
                final = recursive(mydir,"width and height",operation,ext,var_wid = width,var_hei = height)

            if not final:
                print("\nZero files founded\n")
            else:
                print(f"\n{len(final)} file(s) founded:\n")
                for x in final: print(x)
            print("\n" + "-" * 100 + "\n")
            continue

        if option == 1: ## specific
            print("\nInsert the specific directory - example: c:\\myfiles\\images\\vacation\n")
            mydir = input(">>> ")
            if not os.path.exists(mydir):
                print("\nDirectory not found, aborting...")
                print("\n" + "-" * 100 + "\n")
                continue
            
            print("\nInsert the format of image file - example: jpg, png, gif, bmp...\n")
            ext = input(">>> ").lower()
            if not ext:
                print("\nError, aborting...\n")
                print("\n" + "-" * 100 + "\n")
                continue
            print("\nOptions for search using:\n\n[1] Width and height\n[2] Width only\n[3] Height only\n[4] Return to main menu\n")
            option2 = answer(4)

            if option2 == 4:
                continue

            if option2 == 3: ## height only
                print("\nInsert a height value for comparison:\n")
                height = input(">>> ")
                if not height.isdigit():                    
                    print("\nError, aborting...\n")
                    print("\n" + "-" * 100 + "\n")
                    continue
                height = int(height)
                print(f"\nOptions of search:\n\n[1] Equal to {height}\n[2] Less then {height}\n[3] Less or equal to {height}\n[4] Bigger then {height}\n[5] Bigger or equal to {height}\n[6] Not equal to {height}\n[7] Return to main menu\n")
                oper = answer(7)

                if oper == 7:
                    continue

                if oper == 1: operation = "equal"
                if oper == 2: operation = "less"
                if oper == 3: operation = "less or equal"
                if oper == 4: operation = "bigger"
                if oper == 5: operation = "bigger or equal"
                if oper == 6: operation = "not"
                    
                final = specific(mydir,"height",operation,ext,var_hei = height)

            if option2 == 2: ## width only
                print("\nInsert a width value for comparison:\n")
                width = input(">>> ")
                if not width.isdigit():                    
                    print("\nError, aborting...\n")
                    print("\n" + "-" * 100 + "\n")
                    continue
                width = int(width)
                print(f"\nOptions of search:\n\n[1] Equal to {width}\n[2] Less then {width}\n[3] Less or equal to {width}\n[4] Bigger then {width}\n[5] Bigger or equal to {width}\n[6] Not equal to {width}\n[7] Return to main menu\n")
                oper = answer(7)

                if oper == 7:
                    continue

                if oper == 1: operation = "equal"
                if oper == 2: operation = "less"
                if oper == 3: operation = "less or equal"
                if oper == 4: operation = "bigger"
                if oper == 5: operation = "bigger or equal"
                if oper == 6: operation = "not"
                    
                final = specific(mydir,"width",operation,ext,var_wid = width)

            if option2 == 1: ## width and height
                print("\nInsert a width value for comparison:\n")
                width = input(">>> ")
                if not width.isdigit():                    
                    print("\nError, aborting...\n")
                    print("\n" + "-" * 100 + "\n")
                    continue
                width = int(width)
                
                print(f"\nOptions of search:\n\n[1] Equal to {width}\n[2] Less then {width}\n[3] Less or equal to {width}\n[4] Bigger then {width}\n[5] Bigger or equal to {width}\n[6] Not equal to {width}\n[7] Return to main menu\n")
                oper = answer(7)

                if oper == 7:
                    continue

                operation = []

                if oper == 1: operation.append("equal")
                if oper == 2: operation.append("less")
                if oper == 3: operation.append("less or equal")
                if oper == 4: operation.append("bigger")
                if oper == 5: operation.append("bigger or equal")
                if oper == 6: operation.append("not")
                
                print("\nInsert a height value for comparison:\n")
                height = input(">>> ")
                if not height.isdigit():                    
                    print("\nError, aborting...\n")
                    print("\n" + "-" * 100 + "\n")
                    continue
                height = int(height)
                
                print(f"\nOptions of search:\n\n[1] Equal to {height}\n[2] Less then {height}\n[3] Less or equal to {height}\n[4] Bigger then {height}\n[5] Bigger or equal to {height}\n[6] Not equal to {height}\n[7] Return to main menu\n")
                oper = answer(7)

                if oper == 7:
                    continue

                if oper == 1: operation.append("equal")
                if oper == 2: operation.append("less")
                if oper == 3: operation.append("less or equal")
                if oper == 4: operation.append("bigger")
                if oper == 5: operation.append("bigger or equal")
                if oper == 6: operation.append("not")
      
                final = specific(mydir,"width and height",operation,ext,var_wid = width,var_hei = height)

            if not final:
                print("\nZero files founded\n")
            else:
                print(f"\n{len(final)} file(s) founded:\n")
                for x in final: print(x)
            print("\n" + "-" * 100 + "\n")
            continue

menu()
