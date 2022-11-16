#Isak Nordström
#Tetek20
#Adventskalender 2021-01
#2022-11-16

def main():

    quantity_increased = 0
    quantity_decreased = 0

    with open("julkalender_2021_01.txt", "r", encoding="utf8") as ja:
        lines = ja.readlines()
        

        for i in range(len(lines)):
            
            if i == len(lines)-1:
                break
            elif lines[i+1] > lines[i]:
                
                print(f"{lines[i+1]} increased")
                quantity_increased+=1

            elif lines[i+1] < lines[i]:
                
                print(f"{lines[i+1]} decreased")
                quantity_decreased+=1
            
           
        print(f"Quantity increased: {quantity_increased}, quantity decreased: {quantity_decreased}")    



main()