from Peptide_functions import peptideConverter

print("\nWelcome! This program converts Protein Peptide(s) input to their Molar absorptivities \n")

while True:
    #  Asking user's choice
    choice = int(input('Enter 1 to input Peptide(s) manually (seperating different Peptides using commas)\n'
                'Enter 2 to import Peptide(s) using a text (.txt) file (seperating different Peptides using commas)\n'
                'Enter 3 to exit : \n'))
    
    match choice:

        case 1:
            # Taking input from user
            peptideInput = input("\nPlease input the peptide code using single letter Amino Acids: \n")
            print("\nPeptide composition: \n")
            lowerBound, upperBound = peptideConverter(peptideInput) # Calling the Peptide converter function to get lowerbound and upperbound range
            print ("\nThe Molar absorptivity (extinction coefficient) at 205 nm is between ",
            lowerBound, "and ", upperBound, "M-1 cm-1 \n")

        case 2: # Using text file as input
            fileInput = input("\nPlease input a file name (same directory as program) \n")
            with open(fileInput) as peptideFile: # Reading the text file inputted by the user
                contents = peptideFile.read()
                print("\nAmino acid composition: \n")
                lowerBound, upperBound = peptideConverter(contents) # Calling the Peptide converter function to get lowerbound and upperbound range
                print ("\nThe Molar absorptivity (extinction coefficient) at 205 nm is between ",
                lowerBound, "and ", upperBound, "M-1 cm-1 \n")

        case 3:
            break

        case _: # Default case
            print("ERROR! Please enter 1, 2 or 3.")