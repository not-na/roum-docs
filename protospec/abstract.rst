
Abstract
========

The Roum Multiplayer Protocol is designed to let multiple clients share
game state information via a single central server.

The protocol is designed in a way that allows users to easily host their own
servers on any semi-powerful computer. The standalone server does not need any
graphical libraries and can thus run on headless server machines.

Central Server Design
---------------------

A central server design was chosen for security reasons, because only the central
server has to be trusted. This means that all player data is stored on the server.
If any data is to shared with other players, it must first go through the central
server.
One of the disadvantages of this design is however that scaling to very large
(100+) players on a single server becomes difficult without very powerful and
thus expensive server machines.

Security Considerations
-----------------------

The protocol specification is designed to be secure in a way that tampering with
connections or stealing the identity of clients or servers should be nearly
impossible.

Additionally, since the protocol will usually be implemented in Python, common
attacks used on C/C++ based architectures are not possible. This assumes that
Python itself does not have any unknown security vulnerabilities.
