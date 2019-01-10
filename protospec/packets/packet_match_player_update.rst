
``roum:match.player.update`` - Update Player Status
===================================================

.. roum:packet:: roum:match.entity.update.pos

This packet is used to pass the status of a player to each other player.

+-----------------------+--------------------------------------------+
|Internal Name          |:roum:packet:`roum:match.player.update`     |
+-----------------------+--------------------------------------------+
|Direction              |both                                        |
+-----------------------+--------------------------------------------+
|Since Version          |v0.1.0dev                                   |
+-----------------------+--------------------------------------------+
|Valid Modes            |``match`` only                              |
+-----------------------+--------------------------------------------+

Purpose
-------

This packet is intended to update the player status every time it changed. It will be sent to all players concerned
by the change.

Structure
---------

Note that all examples shown here contain placeholder data and will have different content in actual packets.

The structure of this packet is similar to :doc:`/format/player_data` but does not contain all keys

.. todo::
   Specify the attributes of :py:class:`roum.Player`
