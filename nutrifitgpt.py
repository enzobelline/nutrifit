import csv
import openai
#gptmodel definition
gpt35turbo=0.002

GPTapiModel = gpt35turbo

# Provide the paths to your CSV file
inputFilePath = "googleforms.csv"
outputFilePath = "promptGeneration.txt"

def count_tokens(input_string):
    tokens = input_string.split()
    return len(tokens)

def promptGenerator(inputFilePath, outputFilePath):
    concatenated_string = ""

    with open(inputFilePath, "r") as csvfile, open(outputFilePath, 'w', newline='') as outputtxt:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row

        for row in reader: #for loop that generates the prompt for each newline in the txt
          # column content index
          # c0= timestamp,   c1 = name, c2 - email, c3 gender, c4 weight,
          # c5 = metabolism, c6 = goals, c7 = exercises interested in, 
          # c8 = hr in a week, c9 = intensity, c10= experience, c11 = diet restrict
          # c12 = health conditions, c13 = payment
          prompt = "This profile is for user, " + row[1] + \
          " . They are a " + row[3] + \
          " who weighs " + row[4] + \
          " lbs. if 1 is a Fast metabolism and Narrow frame and a 5 is a slow metabolism and wider frame, they are a " + row[5] + \
          ". Their goals in fitness are " + row[6] + \
          ". The types of exercises that they want to include in their plan are " + row[7] + \
          ". They have " + row[8] + " in a week to spend towards their fitness plan. " + \
          " On a scale, 1 is easy and 5 is intense, they want the intensity of their fitness plan to be " + row[9]  + \
          ". Their current fitness level on a scale from 1 to 10 with 1 being beginner is " + row[10]  + \
          " Dietary Restrictions:" + row[11]  +\
          " Health conditions to consider in fitness: " + row[12] + "\n"
          outputtxt.write(prompt)
          currToken=count_tokens(prompt)
          cost= currToken*GPTapiModel

          print( row[1] + ": ",currToken," tokens or $",cost)

# Call the function to actually create outputfile
result = promptGenerator(inputFilePath,outputFilePath)
