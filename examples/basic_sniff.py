from scapy.all import sniff
from scapytojson import scapy_to_json


if __name__ == '__main__':
    # Sniff two packets using scapy
    a = sniff(count=2)
    # Convert the captured packets to json
    json_data = scapy_to_json(a,json_indent=2)
    print(json_data)