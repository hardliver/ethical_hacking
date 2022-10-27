# Complete Python 3 Ethical Hacking: Beginner To Advanced!

## Port Scanner

- 獲取ip位置<br/>
    `$ nslookup <網頁HOST>`


## SSH Bruteforcer

- Metasploitable 2
    - [image](https://sourceforge.net/projects/metasploitable/)
    - [docker](https://hub.docker.com/r/tleemcjr/metasploitable2)

    > SSH: msfadmin / msfadmin


## Man in the middle - Arpspoofer

- scapy
    ```python
    $ scapy

    >>> ls(ARP)
    hwtype     : XShortField                         = ('1')
    ptype      : XShortEnumField                     = ('2048')
    hwlen      : FieldLenField                       = ('None')
    plen       : FieldLenField                       = ('None')
    op         : ShortEnumField                      = ('1')
    hwsrc      : MultipleTypeField (SourceMACField, StrFixedLenField) = ('None')
    psrc       : MultipleTypeField (SourceIPField, SourceIP6Field, StrFixedLenField) = ('None')
    hwdst      : MultipleTypeField (MACField, StrFixedLenField) = ('None')
    pdst       : MultipleTypeField (IPField, IP6Field, StrFixedLenField) = ('None')
    >>> packet = ARP(pdst='192.168.0.13')
    >>> packet.show()
    ###[ ARP ]### 
    hwtype    = 0x1
    ptype     = IPv4
    hwlen     = None
    plen      = None
    op        = who-has
    hwsrc     = 52:54:00:94:b6:27
    psrc      = 192.168.0.31
    hwdst     = 00:00:00:00:00:00
    pdst      = 192.168.0.13
    >>> packet.op = 2
    >>> packet.show()
    ###[ ARP ]### 
    hwtype    = 0x1
    ptype     = IPv4
    hwlen     = None
    plen      = None
    op        = is-at
    hwsrc     = 52:54:00:94:b6:27
    psrc      = 192.168.0.31
    hwdst     = 00:00:00:00:00:00
    pdst      = 192.168.0.13
    ```
