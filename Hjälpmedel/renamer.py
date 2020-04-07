import os 
 
def main(): 
    i = 0
    
    for filename in os.listdir("C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w"):
        dst ="0000" + str(i) + ".jpg"
        src ='C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w/'+ filename
        dst ="C:/Users/amjad/OneDrive/Documents/GitHub/AI-projekt-/an/Images/w/"+ dst 
        os.rename(src, dst)
        i += 1

main()
