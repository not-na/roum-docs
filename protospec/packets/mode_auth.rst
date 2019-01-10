
``auth`` Connection Mode
========================

Every connection that is not a :doc:`ping <mode_ping>` connection will start in
this mode. Once this connection mode has been changed away from, it cannot be
reentered, due to security reasons.

Connections in this mode are considered to be not authenticated and not trustworthy.

The main purpose of this connection mode is to exchange credentials to mutually
verify the identity of both server and client.

Handshaking
-----------

These procedures need to be followed to ensure that every connection is secure
and identity theft is prevented.

Note that I am not a security expert, so please point out any security vulnerabilities
privately. Contact information can be found on my GitHub Profile @not-na.

On First Server Start
^^^^^^^^^^^^^^^^^^^^^

On the very first server start, the server registers itself to the :term:`authserver`
calling the :py:meth:`roumauth.ServerSession.createServer()` method after creating
its own instance of :py:class:`roumauth.ServerSession()`\ .

Note that when first creating the server object, only ``serverdata`` needs to be supplied,
as the other values will be automatically generated.

This call populates the ``password`` and ``serverid`` attributes. These values should
be stored securely, as they define the identity of the server.
The ``serverid`` attribute will be shared with clients and is not secret, while
the ``password`` attribute should be kept as secret as a private key.

The ``password`` defaults to a random string of length 32.

On Every Server Start
^^^^^^^^^^^^^^^^^^^^^

This routine should be done on every server start.

First, the credentials generated in the last subsection should be loaded again
and used to create a :py:class:`roumauth.ServerSession()`\ .

If needed, the ``serverdata`` may be updated to reflect changes in the configuration.

The ServerSession should be kept around for as long as the server is running.

On Every New Connection (Server Preparation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Whenever a client requests a new connection, the session validity should be checked
and renewed. This can be done by calling the :py:meth:`roumauth.ServerSession.refreshToken()`
method.

Once this has concluded, the authentication may continue.

.. _auth-protocol:

Further Protocol
^^^^^^^^^^^^^^^^

First, the client uses the API to create a new :py:class:`roumauth.Session()` with the
user-supplied credentials. The E-Mail address used to login should be stored locally
to speed up further login attempts.

Then, the client opens a new :py:mod:`peng3dnet` connection and waits for the :py:mod:`peng3dnet`
handshake to finish before proceeding.

The client then sends a request to the server asking for the server ID and waits for
the answer.

This server ID is used by the client to create a MPSession ID on the :term:`authserver`\ .
The authserver checks the server ID for validity and returns a MPSession ID and secret.

The MPSession ID is then sent to the server for further processing.

The server checks the MPSession ID with the :term:`authserver`\ , also setting a
flag that the server has verified the connection. It also receives the client ID
it did not know before and the secret, which are all sent to the client in order
to prove the identity of the server.

Then, the client sends the MPSession ID and secret to the :term:`authserver` to verify
that the server has set the verification flag. This also sets the client verification
flag.

The client also sends a go-ahead packet to the server to signal that it is ready.

The server then checks with the authserver that the client verification flag has been set.
If the flag has been set, the server indicates to the client that the connection has
been successfully verified.

After this security handshake has concluded, both parties can mutually trust their
supposed identities.

Internally, numbers from 1 to 12 are used to describe the stage of the handshake.

The full table is represented here:

+---+------------------+------------------+------------------------------------------------------------------+
|No.|Direction         | Name             | Description                                                      |
+---+------------------+------------------+------------------------------------------------------------------+
|1-2|---               | Handshake        | Peng3dnet handshake                                              |
+---+------------------+------------------+------------------------------------------------------------------+
|3. |Client->Server    | ServerID #1      | Request for serverID                                             |
+---+------------------+------------------+------------------------------------------------------------------+
|4. |Server->Client    | ServerID #2      | Sends serverID                                                   |
+---+------------------+------------------+------------------------------------------------------------------+
|5. |Client->Auth      | Create MPSession | Creates MPSession with serverID and clientID, receives sessionID |
+---+------------------+------------------+------------------------------------------------------------------+
|6. |Client->Server    | Send MPSession   | Sends MPSession token, shared between parties                    |
+---+------------------+------------------+------------------------------------------------------------------+
|7. |Server->Auth      | Check Session    | Validates Token, sets servercheck, receives secret               |
+---+------------------+------------------+------------------------------------------------------------------+
|8. |Server->Client    | Verify           | Sends secret and clientID to client for verification             |
+---+------------------+------------------+------------------------------------------------------------------+
|9. |Client->Auth      | Check Session    | Checks secret and servercheck, and sets clientcheck              |
+---+------------------+------------------+------------------------------------------------------------------+
|10.|Client->Server    | Ready            | Indicates to server that it is ready                             |
+---+------------------+------------------+------------------------------------------------------------------+
|11.|Server->Auth      | Verify           | Checks clientcheck, receives client information                  |
+---+------------------+------------------+------------------------------------------------------------------+
|12.|Server->Client    | Ready            | Indicates to client that it is ready                             |
+---+------------------+------------------+------------------------------------------------------------------+

.. note::
   After the results of stage 11 have been collected by the authserver, the MPSession is deleted.
   This makes it impossible to verify a connection after it has been established.

:py:mod:`roumauth` Client Library
------------------------------------

The :py:mod:`roumauth` library can be used to easily implement the authentication
interface.

Use the :py:meth:`roumauth.Session.connectToServer()` or :py:meth:`roumauth.ServerSession.connectToClient()`
methods to create a connector object that will handle authentication.

After this object has been created, you will first need to set the callback function
via :py:meth:`roumauth._Connector.setCallback()`\ .

For further information, see the :py:class:`roumauth._Connector()` class documentation.

Packets
-------

.. toctree::
   :maxdepth: 1
   
   packet_auth
