#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will read student names and GPA's from a 
# text file. The program will perform different analytical tasks. It will 
# output a different file called output.txt with the results
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

def main():
    try:
        fileInput = open('input.txt', 'r')
        fileOutput = open('output.txt', 'w')

        # Creating the Names list and Scores list               
        Names = []
        Scores = []
            
        # Loop to capitalize first and last name of each line in the input file
        for line in fileInput:
            # Strip removes empty space 
            # Split the line into seperate words 
            temp = line.strip().split()
            # Get the first name and capitalize it
            firstName = temp[0].title()
            # Get the last name and capitalize it
            lastName = temp[1].title()
            # Concatenate the first and last name and add to Names list
            Names.append(firstName + " " + lastName)
            # Adding the score of the student and turn it into a float
            Scores.append(float(temp[2]))
        
        print("Printing every content in the file...\n", Names)
        print(Scores)
        
        # Finding the max score in Scores
        maxScore = max(Scores)
        
        # Creating the maxScoreStudents list
        maxScoreStudents = []
        # Loop to find students who had the max score and adding them to maxScoreStudents
        for i, score in enumerate(Scores):
            if score == maxScore:
                maxScoreStudents.append(Names[i])
        
        # Writing in the output file what the the max score is 
        # and which students had the max score
        fileOutput.write(f"\nMaximum score is: {maxScore}\n")
        for student in maxScoreStudents:
            fileOutput.write(f"{student} {maxScore} \n")
        
        # Assignment says to add but is not in the desired outputs
        # print("Scores have been updated...")
        
        fileOutput.write("\nUpdated score(s) with letter grade:\n")
        for i in range(len(Scores)):
            # If the students has a score lower than a 4.0  
            # then they will have .1 added to their grade
            if Scores[i] < 4.0:
                Scores[i] += 0.1
            # Second part of the loop to add the grade to the student
            if Scores[i] >= 3.7:
                grade = 'A'
            elif Scores[i] >= 3.5:
                grade = 'B'
            elif Scores[i] >= 3.0:
                grade = 'C'
            elif Scores[i] >= 2.5:
                grade = 'D'
            else:
                grade = 'F'
            # Formatting for the names, scores and grade in the output.txt
            fileOutput.write("{} {:.2f}, {}\n".format(Names[i], Scores[i], grade))
        
        fileInput.close()
        fileOutput.close()

    # Throw an error code instead of ending the program            
    except FileNotFoundError:
        print("The program failed to open the file. Make sure of the followings:")
        print("\t\tThe file to read is located in the same folder where this program is!")
        print("\t\tThe file's name is splled correctly!")
    
main()