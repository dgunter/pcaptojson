from pcap_to_json import load_pcap_to_mongodb
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient()
    load_pcap_to_mongodb(client,"SkypeIRC.pcap")