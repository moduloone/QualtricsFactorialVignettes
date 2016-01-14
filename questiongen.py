#Code for generating Qualtrics basic TXT formatted vignettes
#Written by Nicholas Proferes (proferes@umd.edu)
#Last revision Jan 13 2016
#Use note: to output to a txt file, type 'python questiongen.py > outputfile.txt' in command prompt
#Written for Python 3 or later

#Definition of factors and choices among factors

factorlist1 = ["factor list 1 item 1", "factor list 1 item 2", "factor list 1 item 3"]
factorlist2 = ["factor list 2 item 1", "factor list 2 item 2", "factor list 2 item 3", "factor list 2 item 4"]
factorlist3 = ["factor list 3 item 1", "factor list 3 item 2"]
factorlist4 = ["factor list 4 item 1", "factor list 4 item 2", "factor list 4 item 3", "factor list 4 item 4", "factor list 4 item 5"]
factorlist5 = ["factor list 5 item 1", "factor list 5 item 2", "factor list 5 item 3"]

#Question number counter
questionnumber = 1

#Print code
#To adjust code for fewer factors (say, 4 instead of 5) remove last variable (in this case m) as well as for loop (for m in factorlist5) 

for i, j, k, l, m in [(i,j,k,l,m) for i in factorlist1 for j in factorlist2 for k in factorlist3 for l in factorlist4 for m in factorlist5]:
	
	#Create a block for each item
	print("[[Block]]")
	
	#Print vignette
	print (questionnumber,".", " You are ", i, ". You see ", j, ". When you, ", k , " reacts ", l, " in order to ", m, ".", sep=''), 
	print ('\r')
	print ("This situation is acceptable to me:")
	print ('\r')
	
	#Measure - 5 Point-Likert. Change to fit your needs.
	print ("Strongly Agree.")
	print ("Agree.")
	print ("Neither Agree nor Disagree.")
	print ("Disagree.")
	print ("Strongly Disagree.")
	
	#Increase count and new line
	questionnumber += 1
	print ('\r')
	
print ("\r")
