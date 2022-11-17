#Isak Nordström
#Tetek20
#Adventskalender 2021-02
#2022-11-17

def main():

    with open("2021-02.txt", "r", encoding="utf8") as ja:
        lines = ja.readlines()

        #print((lines[10])[-2])

        height = 0
        length = 0

        for i in range(len(lines)):
            
            if (lines[i])[0:2] == "up":
                height-=int((lines[i])[-2])

            elif (lines[i])[0:4] == "down":
                height+=int((lines[i])[-2])

            elif (lines[i])[0:7] == "forward":
                length+=int((lines[i])[-2])
        
        print(f"Length: {length} Height: {height}")
        print(f"Result: {length*height}")

main()