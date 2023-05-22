# Langchain Events

The Langchain Events project aims to provide automation using the Langchain library and [nlp2fn](https://pypi.org/project/nlp2fn/0.0.1/).

**About Langchain and [nlp2fn](https://pypi.org/project/nlp2fn/0.0.1/)**

- Langchain is a powerful Python library designed for blockchain-based language translation. It utilizes advanced machine learning and natural language processing techniques to facilitate multi-language translations. By leveraging blockchain technology, Langchain ensures translation accuracy and reliability, fostering trust and maintaining high quality. Additionally, it provides a decentralized framework for translators to contribute and earn rewards for their efforts.
- nlp2fn is a seamless and intuitive software tool for Python automation. It allows you to load and execute Python functions from any specified location. Whether your functions reside in local directories or remote servers, nlp2fn simplifies the process of fetching, loading, and preparing them for execution.

## Setup

- **Clone the Repository**
```shell
git clone git@github.com:dextrop/evt-langchain.git
```
This command clones the `git@github.com:dextrop/evt-langchain.git` repository to your local system, creating a directory named `evt-langchain`.

- **Install Dependencies**
```shell
cd evt-langchain
pip install -r requirements.txt
```
Navigate to the `evt-langchain` directory and run the above command to install the project's dependencies.

- **Set the Source**
```shell
nlp2fn set source events 
```
Before running the above command, ensure that you are inside the `evt-langchain` directory. This command sets the source directory as "events" within the `evt-langchain` clone.

## Getting Started

Now that we have set up the source directory as "events" within the `evt-langchain` project, we can start using the different events provided. Here is a list of available events:

#### 1. Chatbot 

To run the chatbot, execute the following command:

```shell
nlp2fn exec -m "Start using chatbot"
```

**Output:**

```
Statement: Start using chatbot
Executing: Start using chatbot

Welcome! This event utilizes OpenAI with Langchain to answer all your queries. To start the chatbot, you need to provide your OpenAI key.

To obtain an OpenAI key, visit https://platform.openai.com/account/api-keys. If you don't have an account, sign up; otherwise, log in.

Enter your OpenAI key >> sk0p0eGJ70czimpYsCTywvtT1BlbZFJKOblL2Pa5aSU72tV1ItM
Ask a query >> What is the sum of all numbers between 0 and 100?

The sum of all numbers between 0 and 100 is 5050.
Ask a query >> Can you smile for me?

Yes, I can! :)
Ask a query >>
```

#### 2. Analyse CSV
The event help use to take any CSV as input and can analyse data based on the information.
To run type

```nlp2fn exec -m "Analyse data from /Users/jennie/Downloads/SoundAuthUsers-Sheet1.csv"```

**output**
```shell
Statement: Analyse data from /Users/jennie/Downloads/SoundAuthUsers-Sheet1.csv
Executing: Analyse data from {csv_file_path}

Welcome, The event uses OpenAI with langchain to answer all your query.
To start you need to enter Open AI Key.
To Obtain an Open AI key, go to https://platform.openai.com/account/api-keys
Signup if you dont have an account, else login.
 

Enter you open ai key >> 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
Ask Query >> list all columns    


> Entering new AgentExecutor chain...
Thought: I need to find out what columns are in the dataframe
Action: python_repl_ast
Action Input: df.columns
Observation: Index(['Type', 'Email', 'Timestamp'], dtype='object')
Thought: I now know the final answer
Final Answer: Type, Email, Timestamp

> Finished chain.
Type, Email, Timestamp
Ask Query >> exit

The project is created for fun purpose, Read more about the project at
        https://github.com/dextrop/eventlangchain

If you have any feedback you can mail us on saurabh@ask-jennie.com
```

## Join the Development

We welcome contributions from the community! Feel free to submit pull requests and create issues on our [GitHub page](https://github.com/dextrop/nlp2fn/issues).

## Contact

For questions, suggestions, or any kind of discussion, feel free to open an issue on our GitHub page.

Embrace the simplification of Python automation with `nlp2fn`.



