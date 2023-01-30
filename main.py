import requests
import json
from serpapi import GoogleSearch
import time

#Cyllene

# A library/program for getting paraphrased answers from google. 
#usefull for dfintions and what are questions. 

#Works by  connecting with google search api (rapidAPI) and paraphrasing tool. Account are neeed for each. Just use temp email. 

#Grabs from answerbox displayed in google search. 



def paraphrase(input):
    url = 'https://app.plaraphy.com/api/rewriter'

    payload = 'text=' +  input + '.&mode=fluent&lang=es&unique=true'
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'authorization': 'Bearer 24387|8vTSyVeU1ysS8WOkCB9Cu0awirnqGJHAVeEibqL8',
        'cache-control': 'no-cache',
        }
    try: 
        response = requests.post( url, data=payload, headers=headers)

        responseText = response.text

        json_obj = json.loads(responseText)
        print(json_obj, "\n")
        p =  json_obj["rewrited"]
        return p
    except:
        return input


def getDefinition(word):
    params = {
        "engine": "google",
        "q": word,
        "api_key": "9ba9c7ad55c96a85534ed022d151995a28dc650c0246d44b23f8a5e867add0df",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }

    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]

    #organic_results = ""
    #print(type(organic_results))
    #print(organic_results)
    return organic_results[2].get("snippet")
    #return jsonRslt["answer_box"]["snippet"]

inputFilePath = "./words.txt"
outputFilePath = "./output.txt"


#parse csv file
#define and paraphrase each word
#print output to file
def parseFile(filePath):
    inputFile = open(filePath, "r")
    outputFile = open("output.txt", "a")
    

    try:
        # Read and print the entire file line by line
        currWord = inputFile.readline() + " Computer science definition"


        while currWord != '':  # The EOF char is an empty string
            print(currWord, end='')

            definition = getDefinition(currWord)
            definition = getDefinition(currWord)

            definition = definition.replace("...", "")
            definition = definition.strip()

            print("definition: ", definition)

            paraphased = paraphrase(definition)
            time.sleep(2.5)
            outputFile.write(currWord+ "\n"+ definition + "\n")
            currWord = inputFile.readline() + " Computer science definition"
        #for()
    finally:
        inputFile.close()
        outputFile.close()

    
    #definition = getDefinition("Software Portability definition computer science ")
    #paraphrased = paraphrase(definition)

   



parseFile(inputFilePath)
# currWord = "stability"
# definition = getDefinition(currWord)
# paraphased = paraphrase(getDefinition(currWord))
# print(paraphased)