'''
The MIT License (MIT)

Copyright (c) 2015 Dan Gunter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

from base64 import b64encode
from json import dumps

def fix_encoding(d,target_encoding='utf-8'):
    '''
    @summary: Fixes the encoding within a dict to make the dict JSON encodable
    @var d: A dictionary to fix encoding within
    @var target_encoding: The encoding to check for
    '''
    out_dict = dict()
    for k, v in d.iteritems():
        if type(v) == dict:
            out_dict[k] = fix_encoding(v)
        else:
            # Check to see if value is unicode
            try:
                str(v).decode(target_encoding)
                out_dict[k] = v
            except UnicodeError:
                # Base64 encode value to avoid json errors
                out_dict[k] = b64encode(v)
            
    return out_dict



def pcap_to_json(pkt,json_indent=4):
    '''
    @summary: Converts a collection of scapy packets to a json encodable object
    @var pkt: The scapy packet collection to encode
    @var json_indent: Controls formatting within the JSON encoded data
    '''
    pkts = list()
    
    for x in pkt:
        pkts.append(packet_to_json(x))
        
    return dumps(pkts,indent=json_indent)

def packet_to_json(pkt):
    '''
    @summary: Converts a collection of scapy packets to a json encodable object
    @var pkt: The scapy packet collection to encode
    @var json_indent: Controls formatting within the JSON encoded data
    '''    
    retpacket = dict()
    layer_iter = 0
    while pkt.getlayer(layer_iter) is not None:
        # Save the layer fields
        layerfields = pkt.getlayer(layer_iter).fields
        # Save the layer name for future identification
        retpacket[pkt.getlayer(layer_iter).name] = fix_encoding(layerfields)
        layer_iter+=1

    return retpacket