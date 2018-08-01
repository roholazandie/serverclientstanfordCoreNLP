# Description
This project can run the standfordcorenlp in python using threading and client server architecture.
The client.py starts the server as a daemon thread in the background and if it is already started use it.
You can instantiate client in your code without being worry about anything else.

# How to use?
1. Install the requirements.txt
```
pip install -r requirements.txt
```
1. Download the [standfordcorenlp](https://stanfordnlp.github.io/CoreNLP/) and extract it.
2. Give the correct path of the folder to client
3. Run the client.py

# Requirements
This code works with standfordcorenlp 2018-02-27 and Python3.5.