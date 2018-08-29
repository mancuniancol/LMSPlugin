# LMSPlugin
Fauxmo plugin for Logitech Media Server (Squeezebox Server).
https://github.com/n8henrie/fauxmo

The devices have 5 properties:

**server_ip**: Squeezebox server IP address (optional). If it is omitted, it will use localhost as server_ip. However, this implies that FAUXMO is running in the same machine that Squeezebox server.

**player_id**: Unique player identifier (optional). It could be obtening by typing `http://[server_ip]:9000/status.html`. It will use the current player in the server.

**playlist**:  Song path, playlist path, directory or url (optional).  The device will be treated as player or server if this property is omitted.

**name**: Name of the device. Mandatory.

**port**: Port that this device will run on. Mandatory.


For example:

Squeezebox server `LMS` has 3 players  `Kitchen player`, `Living Room player` and `Balcony player`

There are 3 playlist.  `101.5 Radio`,` CISM Radio` and `BBC1 Radio`. 

####Option 1. Just the playlists
    {
      "FAUXMO": {
        "ip_address": "auto"
      },
      "PLUGINS": {
        "LMSPlugin": {
          "DEVICES": [
            {
              "port": 12346,
              "name": "101.5 Radio",
              "playlist": "http://stream02.ustream.ca:8000/cibl128.mp3"
            },
            {
              "port": 12347,
              "name": "CISM Radio",
              "playlist": "http://opml.radiotime.com/Tune.ashx?id=s24807"
            },
            {
              "port": 12348,
              "name": "BBC1 Radio",
              "playlist": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p"
            }
          ]
        }
      }
    }

It will use the current player and the Squeebox server should be installed in the same machine than FAUXMO

####Option 2. Just the playlists detailed
    {
      "FAUXMO": {
        "ip_address": "auto"
      },
      "PLUGINS": {
        "LMSPlugin": {
          "DEVICES": [
            {
              "port": 12346,
              "name": "101.5 Radio",
              "server_ip": "192.168.0.124",
              "player_id": "5a:8c:23:5c:f0:bc"
              "playlist": "http://stream02.ustream.ca:8000/cibl128.mp3"
            },
            {
              "port": 12347,
              "name": "CISM Radio",
              "server_ip": "192.168.0.124",
              "player_id": "cc:8c:23:cc:f0:bc"
              "playlist": "http://opml.radiotime.com/Tune.ashx?id=s24807"
            },
            {
              "port": 12348,
              "name": "BBC1 Radio",
              "server_ip": "192.168.0.124",
              "player_id": "12:8c:aa:5c:f0:bc",
              "playlist": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p"
            }
          ]
        }
      }
    }
    
The player can be the same or not, same for the server.

####Option 3. Controlling only the players
    {
      "FAUXMO": {
        "ip_address": "auto"
      },
      "PLUGINS": {
        "LMSPlugin": {
          "DEVICES": [
            {
              "port": 12341,
              "name": "Kitchen player",
              "server_ip": "192.168.0.124",
              "player_id": "5a:8c:23:5c:f0:bc"
            },
            {
              "port": 12342,
              "name": "Living Room player",
              "server_ip": "192.168.0.124",
              "player_id": "cc:8c:23:cc:f0:bc"
            },
            {
              "port": 12343,
              "name": "Balcony player",
              "server_ip": "192.168.0.124",
              "player_id": "12:8c:aa:5c:f0:bc"
            }
          ]
        }
      }
    }

####Option 4. Controlling the server only
    {
      "FAUXMO": {
        "ip_address": "auto"
      },
      "PLUGINS": {
        "LMSPlugin": {
          "DEVICES": [
            {
              "port": 12340,
              "name": "Squeezebox Server",
              "server_ip": "192.168.0.124"
            }
          ]
        }
      }
    }
    
 ####Option 5. Controlling all
 
     {
      "FAUXMO": {
        "ip_address": "auto"
      },
      "PLUGINS": {
        "LMSPlugin": {
          "DEVICES": [
            {
              "port": 12340,
              "name": "Squeezebox Server",
              "server_ip": "192.168.0.124"
            },
            {
              "port": 12341,
              "name": "Kitchen player",
              "server_ip": "192.168.0.124",
              "player_id": "5a:8c:23:5c:f0:bc"
            },
            {
              "port": 12342,
              "name": "Living Room player",
              "server_ip": "192.168.0.124",
              "player_id": "cc:8c:23:cc:f0:bc"
            },
            {
              "port": 12343,
              "name": "Balcony player",
              "server_ip": "192.168.0.124",
              "player_id": "12:8c:aa:5c:f0:bc"
            },
            {
              "port": 12346,
              "name": "101.5 Radio",
              "playlist": "http://stream02.ustream.ca:8000/cibl128.mp3"
            },
            {
              "port": 12347,
              "name": "CISM Radio",
              "playlist": "http://opml.radiotime.com/Tune.ashx?id=s24807"
            },
            {
              "port": 12348,
              "name": "BBC1 Radio",
              "playlist": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p"
            }
          ]
        }
      }
    }