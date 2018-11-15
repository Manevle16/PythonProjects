import os

os.chdir("C:/Users/Manev/github/Manevle16/PythonProjects/MachineImageProcessing")

for img in os.listdir("PositiveImages"):
    line = 'positive_images/'+img+' 1 0 0 50 50\n'
    with open('info.dat', 'a') as f:
        f.write(line)
for img in os.listdir("NegativeImages"):
    line = 'negative_images/'+img+'\n'
    with open('bg.txt', 'a') as f:
        f.write(line)
