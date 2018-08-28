"""lmsplugin.py :: Fauxmo plugin for Logitech Media Server (Squeezebox Server).

Fauxmo plugin that makes simple HTTP requests in its `on` and `off` methods.
"""
import http.client
import urllib.error
import urllib.parse
import urllib.request

from fauxmo.plugins import FauxmoPlugin

__author__ = 'mancuniancol'


class LMSPlugin(FauxmoPlugin):
    def __init__(
        self,
        *,
        server_ip: str = "localhost",
        player_id: str = "",
        playlist: str = None,
        name: str,
        port: int
    ) -> None:
        """ Initialize a LMSPlugin instance.

        Keyword Args:
            server_ip: Squeezebox server IP address
            player_id: Unique player identifier
            playlist:  Song path, playlist path, directory or url
            name: Name of the device
            port: Port that this device will run on
        """
        self.server_ip = server_ip
        self.player_id = player_id
        self.playlist = playlist
        self.item = None
        super().__init__(name=name, port=port)

    @staticmethod
    def open(url):
        result = "unknown"
        try:
            req = urllib.request.Request(url=url)
            with urllib.request.urlopen(req) as resp:
                if isinstance(resp, http.client.HTTPResponse
                              ) and resp.status in (200, 201):
                    result = resp.read().decode('utf8')

        except urllib.error.URLError:
            pass

        return result

    def on(self) -> bool:
        """ Turn device on.

        Returns:
            True if the request seems to have been sent successfully
        """
        url = "http://%s:9000/status.html?p0=" % self.server_ip
        if self.playlist is None:
            url += "play"
        else:
            url += "playlist&p1=play&p2=%s" % self.playlist

        url += "&player=%s" % self.player_id
        resp = self.open(url)
        if resp != "unknown" and self.playlist is not None:
            self.item = resp[resp.find("item=") + 5: resp.find("&amp;")]

        return resp != "unknown"

    def off(self) -> bool:
        """ Turn device off.

        Returns:
            True if the request seems to have been sent successfully
        """
        url = "http://%s:9000/status.html?p0=stop" % self.server_ip
        url += "&player=%s" % self.player_id
        resp = self.open(url)
        self.item = None
        return resp != "unknown"

    def get_state(self) -> str:
        """ Get device state.

        Returns:
            "on", "off", or "unknown"
        """
        url = "http://%s:9000/status.html" % self.server_ip
        url += "?player=%s" % self.player_id

        resp = self.open(url)
        if resp == "unknown":
            return "unknown"

        is_stopped = not resp.find("<b>Play</b>") > -1
        if is_stopped:
            return "off"

        if self.playlist is None:
            return "on"

        # if we get here, there is a playlist
        # which is playing and it requires to call the songinfo
        if self.item is None:
            item = resp[resp.find("item=") + 5: resp.find("&amp;")]
            url = "http://%s:9000/songinfo.html?item=%s&player=%s" % (
                self.server_ip, item, self.player_id)
            song_info = self.open(url)
            if self.playlist in song_info:
                self.item = item

        return "on" if self.item is not None and self.item in resp else "off"
