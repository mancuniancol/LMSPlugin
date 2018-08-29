# LMSPlugin
Fauxmo plugin for Logitech Media Server (Squeezebox Server).
https://github.com/n8henrie/fauxmo

The devices have 5 properties:

server_ip: Squeezebox server IP address (optional). If it is omitted, it will use localhost as server_ip
player_id: Unique player identifier (optional). It could be obtening by typing `http://[server_ip]:9000/status.html`. It will use the current player in the server.
playlist:  Song path, playlist path, directory or url (optional).  The device will be treated as player or server.
name: Name of the device.
port: Port that this device will run on.


For example:

Squeezebox server [LMS] has 3 players  [Kitchen player], [Living Room player] and [Balcony player]

There are 3 playlist.  Playlist1, Playlist2 and Playlist3. 

The configuration 
