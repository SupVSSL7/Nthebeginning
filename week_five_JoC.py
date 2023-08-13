'''FILENAME = "data/years.dat"

dataFile = open(FILENAME, "r")

line =dataFile.readline()

while line != "":
    line = line.rstrip()
    print(line)
    line = dataFile.readline()

# dataFile.close()'''


def simple_therapist(question):
    feels = 1
    
    while feels != 0:
        print(input("How does that make you feel? "))
        return feels
    else:
        feels -= 1
    print("Thank you! Come again!")
    


def main():
    question = print(input("Tell me what is bothering you.  "))
    
    print(simple_therapist(question))

main()