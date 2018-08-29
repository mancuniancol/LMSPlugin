# LMSPlugin
Fauxmo plugin for Logitech Media Server (Squeezebox Server).
https://github.com/n8henrie/fauxmo

The devices have 5 properties:

<b>server_ip</b>: Squeezebox server IP address (optional). If it is omitted, it will use localhost as server_ip. However, this implies that FAUXMO is running in the same machine that Squeezebox server.

<b>player_id</b>: Unique player identifier (optional). It could be obtening by typing `http://[server_ip]:9000/status.html`. It will use the current player in the server.

<b>playlist</b>:  Song path, playlist path, directory or url (optional).  The device will be treated as player or server if this property is omitted.

<b>name</b>: Name of the device. Mandatory.

<b>port</b>: Port that this device will run on. Mandatory.


For example:

Squeezebox server [LMS] has 3 players  [Kitchen player], [Living Room player] and [Balcony player]

There are 3 playlist.  Playlist1, Playlist2 and Playlist3. 

It is possible to configure le playlist1 to play current player.  Then, only playlist, name and port properties will be added. Or attached to determinate player, then all the properties should added.

