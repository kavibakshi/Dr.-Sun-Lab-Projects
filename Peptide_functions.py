# Function to convert amino acid letters to coefficients
def peptideConverter(peptideInput):
    # Creating Amino Acid List
    amino_list = ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l'
                , 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y']

    # Creating Amino Acid Coefficient list
    Amino_Coeff_205 = [79, 2200, 136, 151, 8600, 54, 5200, 104, 98, 104,
                        1830, 400, 72, 400, 1350, 81, 97, 97, 20400, 6080]
    
    peptide = list(peptideInput.lower()) # Converting Amino Acid input to a list

    peptideLength = -1 
    cysteineCount = 0
    peptideSum = 0
    lowerBound = 0
    upperBound = 0

    for i in peptide: # Looping through amino acid input
        index=0 # Keeps track of the index in the list
        for j in amino_list: # Looping through the amino acid alphabet list
            if i == j: # if amino acid match
                print(i.upper(), " = ", Amino_Coeff_205[index] ) # Print Amino Acid and its Coefficient
                peptideSum += Amino_Coeff_205[index] # Adding the Coefficients together
                peptideLength+=1
                if j == 'c': #counts the number of cysteine's 
                    cysteineCount+=1
            index+=1
            

        if i == ',': # New Peptide
            lowerBound = peptideSum + (2612 * peptideLength)
            upperBound = peptideSum + (2948 * peptideLength) 
            print ("\nThe Molar absorptivity (extinction coefficient) at 205 nm is between ",
            lowerBound, "and ", upperBound, "M-1 cm-1 \n")
            #resetting variables
            peptideSum, cysteineCount, peptideLength, lowerBound, upperBound = 0

    lowerBound = peptideSum + (2612 * peptideLength)
    upperBound = peptideSum + (2948 * peptideLength) 

    return lowerBound, upperBound