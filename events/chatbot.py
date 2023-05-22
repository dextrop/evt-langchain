from langchain.llms import OpenAI

# The function statement
STATEMENT = "Start using chatbot"

welcomeMsg = '''\nWelcome, The event uses OpenAI with langchain to answer all your query.
To start the chatbot you need to enter Open AI Key.
To Obtain an Open AI key, go to https://platform.openai.com/account/api-keys
Signup if you dont have an account, else login.\n 
'''

startedMsg = '''\nChatbot is initialization, you can not start asking any query
To end simply type `exit` instead of query 
\n'''

endMsg = '''\nThe project is created for fun purpose, Read more about the project at
\thttps://github.com/dextrop/eventlangchain\n
If you have any feedback you can mail us on saurabh@ask-jennie.com
\n'''

def execute(args):
    # Continue with the function to download the file to the output location.
    print (welcomeMsg)
    key = input("Enter you open ai key >> ")

    llm = OpenAI(openai_api_key=key)
    doContinue = True
    while(doContinue):
        query = input("Ask Query >> ")
        checkForExit = query.replace(" ", "").lower()
        resp = llm(query)
        if checkForExit == "exit" or checkForExit == "exit()":
            doContinue = False
        print (resp)

    print (endMsg)
    return True
