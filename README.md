# retracker-python

A very primitive retracker for local network.
A retracker allows 2 or more computers in one local network communicate via torrent protocol with high speed.

It's don't works with utorrent.
It works with transmission on windows/linux (on windows check firewall to allow local connections for torrent client)

You need bencode package.
Get it there: https://pypi.python.org/pypi/BitTorrent-bencode/5.0.8#downloads
Unpack it into retracker-python/bencode, so bencode.py should be at path retracker-python/bencode/bencode.py

How to use it?
For example you has 2 local computers. 192.168.0.100 and 192.168.0.101
1) Launch retracker on one of local computers. For example, 192.168.0.100
2) At 192.168.0.100 go to transmission, select one of torrents, go to properties, trackers, and add new tracker:
http://ip_from_step_1:8888
3) Repeat step 2 on all your computers.
4) Repeat for all torrents you need.

Another way is set up local DNS so requests to retracker.local will be proceed to computer with retracker. Also, you will need to change retracker port to 80. And this way will work not for all torrents.
