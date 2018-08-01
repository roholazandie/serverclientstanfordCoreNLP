from pycorenlp import StanfordCoreNLP
from server import StanfordCoreNLPServer
import logging

logging.basicConfig(
            filename="serverclientstanfordCoreNLP.log",
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(message)s")


class Client():

    def __init__(self, corenlp_dir):
        '''
        As you make an instace of the client the server starts to run
        '''
        corenlp_server = StanfordCoreNLPServer(corenlp_dir=corenlp_dir )
        corenlp_server.run()
        self._ip = 'http://localhost:9000'


    def get_sentence_sentiment(self, sentence):
        try:
            nlp = StanfordCoreNLP(self._ip)
            result = nlp.annotate(sentence,
                                  properties={
                                   'annotators': 'sentiment',
                                   'outputFormat': 'json',
                                   'timeout': 5000,
                               })
        except:
            logging.exception("Server didn't respond")
            return None


        return result["sentences"][0]["sentiment"], result["sentences"][0]["sentimentValue"]




if __name__ == "__main__":
    client = Client("./stanford-corenlp-full-2018-02-27/*")
    sentiment, sentiment_value = client.get_sentence_sentiment("I love you.")
    print("sentiment ", sentiment)
    print("sentiment value ", sentiment_value)


