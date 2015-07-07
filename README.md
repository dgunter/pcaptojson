# scapytojson
This library converts scapy packet captures into JSON. Non JSON encodable data is converted to base64 to fix any json encoding issues. The name of the scapy frame is stored in the _layertype key.

Quick Example:
```python
from scapy.all import sniff
from scapy_to_json import scapy_to_json


if __name__ == '__main__':
    # Sniff two packets using scapy
    a = sniff(count=2)
    # Convert the captured packets to json
    json_data = scapy_to_json(a,json_indent=2)
    print(json_data)
```
Output:
```json
[
  [
    {
      "_layertype": "Ethernet", 
      "src": "f8:0b:be:ff:33:cc", 
      "dst": "01:00:5e:cc:bb:aa", 
      "type": 2048
    }, 
    {
      "frag": 0, 
      "src": "192.168.0.23", 
      "proto": 17, 
      "_layertype": "IP", 
      "tos": 64, 
      "dst": "239.255.255.250", 
      "ttl": 1, 
      "len": 487, 
      "id": 29298, 
      "version": 4, 
      "flags": 0, 
      "ihl": 5, 
      "chksum": 37740, 
      "options": []
    }, 
    {
      "dport": 8082, 
      "_layertype": "UDP", 
      "sport": 1050, 
      "len": 467, 
      "chksum": 54681
    }, 
    {
      "load": "AvsRIS4cGYZEt2ZUy2wVPxUABkdmVyPSczJyB2ZXI9JzE1NCcgcGVuZGNhcD0nRmFsc2UnIC8+PHgvPjwvYWN0aXZpdGllcz48L25vZGU+", 
      "_layertype": "Raw"
    }
  ], 
  [
    {
      "_layertype": "Ethernet", 
      "src": "fc:8e:7e:aa:bb:cc", 
      "dst": "01:00:5e:dd:ee:ff", 
      "type": 2048
    }, 
    {
      "frag": 0, 
      "src": "192.168.0.24", 
      "proto": 17, 
      "_layertype": "IP", 
      "tos": 64, 
      "dst": "239.255.255.250", 
      "ttl": 1, 
      "len": 1500, 
      "id": 46510, 
      "version": 4, 
      "flags": 1, 
      "ihl": 5, 
      "chksum": 11326, 
      "options": []
    }, 
    {
      "dport": 8082, 
      "_layertype": "UDP", 
      "sport": 1065, 
      "len": 2150, 
      "chksum": 8860
    }, 
    {
      "load": "AvsRIS4cGYZEt2ZUy2bXA7c32R2cmZzL3YyMCcgc3JjPSd1ZHA6Ly8yMzkuMTkyLjE2Ljc5Ojc1MzQ6NjJjNzA4Nzk=", 
      "_layertype": "Raw"
    }
  ]
]

```
