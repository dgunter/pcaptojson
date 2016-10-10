# scapytojson
This library converts scapy packet captures into JSON. Non JSON encodable data is converted to base64 to fix any json encoding issues. The name of the scapy frame is stored in the _layertype key.

Quick Example:
```python
from scapy.all import sniff
from pcap_to_json import pcap_to_json

if __name__ == '__main__':
    # Sniff two packets using scapy
    a = sniff(count=2)
    # Convert the captured packets to json
    json_data = pcap_to_json(a,json_indent=2)
    print(json_data)
```
Output:
```json
[
  {
    "Ethernet": {
      "src": "AA:BB:CC:DD:EE:FF", 
      "dst": "AA:BB:CC:DD:EE:FF", 
      "type": 2048
    }, 
    "TCP": {
      "reserved": 0, 
      "seq": 2800302890, 
      "ack": 1696482828, 
      "dataofs": 8, 
      "urgptr": 0, 
      "window": 435, 
      "flags": 16, 
      "chksum": 8764, 
      "dport": 1234, 
      "sport": 2234, 
      "options": [
        [
          "NOP", 
          null
        ], 
        [
          "NOP", 
          null
        ], 
        [
          "Timestamp", 
          [
            3369739968, 
            39714132
          ]
        ]
      ]
    }, 
    "IP": {
      "frag": 0, 
      "src": "1.1.1.1", 
      "proto": 6, 
      "tos": 0, 
      "dst": "2.2.2.2", 
      "chksum": 61630, 
      "len": 52, 
      "options": [], 
      "version": 4, 
      "flags": 0, 
      "ihl": 5, 
      "ttl": 44, 
      "id": 40542
    }
  }, 
  {
    "Raw": {
      "load": "_"
    }, 
    "Ethernet": {
      "src": "AA:BB:CC:DD:EE:FF", 
      "dst": "AA:BB:CC:DD:EE:FF", 
      "type": 2048
    }, 
    "TCP": {
      "reserved": 0, 
      "seq": 1696482828, 
      "ack": 2800302890, 
      "dataofs": 8, 
      "urgptr": 0, 
      "window": 4096, 
      "flags": 24, 
      "chksum": 46274, 
      "dport": 1234, 
      "sport": 2234, 
      "options": [
        [
          "NOP", 
          null
        ], 
        [
          "NOP", 
          null
        ], 
        [
          "Timestamp", 
          [
            39714167, 
            3369739968
          ]
        ]
      ]
    }, 
    "IP": {
      "frag": 0, 
      "src": "1.1.1.1", 
      "proto": 6, 
      "tos": 0, 
      "dst": "2.2.2.2", 
      "chksum": 14126, 
      "len": 53, 
      "options": [], 
      "version": 4, 
      "flags": 2, 
      "ihl": 5, 
      "ttl": 64, 
      "id": 494
    }
  }
]

```
