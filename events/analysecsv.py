import os.path

from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

# The function statement
STATEMENT = "Analyse data from {csv_file_path}"

welcomeMsg = '''\nWelcome, The event uses OpenAI with langchain to answer all your query.
To start you need to enter Open AI Key.
To Obtain an Open AI key, go to https://platform.openai.com/account/api-keys
Signup if you dont have an account, else login.\n 
'''

startedMsg = '''\nAnalyseCSV is initialization, you can not start asking any query
The query shall be answered based on the csv provided.
To end simply type `exit` instead of query.
\n'''

endMsg = '''\nThe project is created for fun purpose, Read more about the project at
\thttps://github.com/dextrop/eventlangchain\n
If you have any feedback you can mail us on saurabh@ask-jennie.com
\n'''

def execute(args):
    # Continue with the function to download the file to the output location.
    print (welcomeMsg)
    key = input("Enter you open ai key >> ")
    doContinue = True

    if not os.path.exists(args[0]):
        raise ValueError("Invalid CSV File")

    agent = create_csv_agent(OpenAI(temperature=0, openai_api_key=key),
                             args[0],
                             verbose=True)
    while(doContinue):
        query = input("Ask Query >> ")
        checkForExit = query.replace(" ", "").lower()
        if checkForExit == "exit" or checkForExit == "exit()":
            doContinue = False
        else:
            resp = agent.run(query)
            print ("Answer : ", resp)

    print (endMsg)
    return True
