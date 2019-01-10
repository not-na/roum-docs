
``roum:match.player.update.pos`` - Update Player Position
=========================================================

.. roum:packet:: roum:match.player.update.pos

This packet is used to pass the position of a player to each other player.

+-----------------------+--------------------------------------------+
|Internal Name          |:roum:packet:`roum:match.player.update.pos` |
+-----------------------+--------------------------------------------+
|Direction              |both                                        |
+-----------------------+--------------------------------------------+
|Since Version          |v0.1.0dev                                   |
+-----------------------+--------------------------------------------+
|Valid Modes            |``match`` only                              |
+-----------------------+--------------------------------------------+

Purpose
-------

This packet is intended to be sent to all players in the vicinity of the emitting player each :term:`game tick`\ .
If the recipient is further away, he will receive this packet less frequent.

Structure
---------

Note that all examples shown here contain placeholder data and will have different content in actual packets.::

   {
   "time":9162

   "player":"1a0ab7f4-3225-42ea-9d62-052c874e25e7"
   "position":(531.25, 133.39, 927.78)
   }

The ``time`` is the timestamp in :term:`game ticks`\ , at which the ``player`` was at the specified ``position``\ .
Here, the ``time`` is the clientside time of the ``player``\ , not the serverside game time.
