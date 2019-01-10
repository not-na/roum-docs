
``ping`` Connection Mode
========================

The pinging mechanism is handled by the :py:mod:`peng3dnet.ext.ping` module.

This mode is also different in that it actually is a different :py:mod:`peng3dnet`
connection type called :py:mod:`peng3dnet.ext.ping.PingConnectionType`\ , whereas
all other connection modes use the same connection type and can be switched between
at any time.

Purpose
-------

A ping is intended to be used to query publicly available information from the server.
This information may include the number of players on the server, the name of the
server and many other pieces of information.

A ping is usually sent by the game client, but it may also be sent by other applications
to gather information about a server, e.g. in a website presenting a list of servers.

As a side-effect, the roundtrip time from client to server and back is also measured.
This ping time automatically includes packet encoding, network lag, packet decoding/re-encoding
by the server and handling by the client. The roundtrip time is thus an accurate
representation of the delays to be expected when querying information from the server
during other modes.

Client Side
-----------

Pinging is done by the multiplayer server list found when clicking the :guilabel:`Select Server`
button in the main menu.

The multiplayer server list uses the :py:meth:`opendig.client.Client.asyncPingServer()`
wrapper to ensure that the returned server data has been normalized

.. todo::
   How does this work for Roum

.. seealso::
   See the :doc:`/format/serverlist` documentation for how the server list is stored.

Server Side
-----------

Since ping requests are automatically handled, only a callback that can add server
statistics is used for customization.

The callback that is used is :py:meth:`opendig.server.dedicated.ODServer.getPingData()`\ .

.. todo::
   How does this work for Roum

Transmitted Data
----------------

.. todo::
   Add this subsection
