import random

#Open both the README and Jokes files.
readme_file = open("README.md","r+",encoding = "utf-8")
jokes_file = open("Jokes.txt","r",encoding = "utf-8")

#Read contents of these files and store them in a list.
readme_lines = readme_file.readlines() 
jokes = jokes_file.readlines()

#First two lines of jokes.txt can be skipped as it contains attributions to the jokes sources.
jokes = jokes[2:]

#Generate a random interger between 0 and len(jokes) and check if it is the starting line of a new joke.
a = random.randint(0,len(jokes))
while (a)%3 != 0:  #every new joke starts at line number 3n
    a = random.randint(0,len(jokes))

#Find Index of the line where the edit is to be made.   
line = readme_lines.index("Here's a Joke for you -\n")

#Replace the old joke line with the new joke line.
readme_lines[line+1] = jokes[a-1]
readme_lines[line+2] = jokes[a]

readme_file.close()
#Reopen README file in write mode and write the new content. 
readme_file = open("README.md","w+",encoding = "utf-8")
readme_file.writelines(readme_lines)

#close both the files.
readme_file.close()
jokes_file.close()
