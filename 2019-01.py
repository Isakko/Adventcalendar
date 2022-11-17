#Isak Nordström
#Tetek20
#Adventskalender 2019-01
#2022-11-16

def main():

    sum = 0

    with open("2019-01.txt", "r", encoding="utf8") as ja:
        lines = ja.readlines()

        for i in range(len(lines)):
            sum+=((int(lines[i])/3)//1)-2
        
        print(sum)

main()  