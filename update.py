import random

readme_file = open("README.md","r+")
jokes_file = open("jokes.txt","r")

readme_lines = readme_file.readlines()
jokes = jokes_file.readlines()


a = random.randint(0,len(jokes))
while (a-1)%3 != 0:  #every new joke starts at line number 3n - 1
    a = random.randint(0,len(jokes))

line = readme_lines.index("Here's a Joke for you -\n")

readme_lines[line+1] = jokes[a-1]
readme_lines[line+2] = jokes[a]

readme_file.close()
readme_file = open("README.md","w+")
readme_file.writelines(readme_lines)

readme_file.close()
jokes_file.close()