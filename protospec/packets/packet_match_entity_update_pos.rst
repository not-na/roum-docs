
``roum:match.entity.update.pos`` - Update Entity Position
=========================================================

.. roum:packet:: roum:match.entity.update.pos

This packet is used to pass the position of an :term:`entity` to each other player.

+-----------------------+--------------------------------------------+
|Internal Name          |:roum:packet:`roum:match.entity.update.pos` |
+-----------------------+--------------------------------------------+
|Direction              |Clientbound                                 |
+-----------------------+--------------------------------------------+
|Since Version          |v0.1.0dev                                   |
+-----------------------+--------------------------------------------+
|Valid Modes            |``match`` only                              |
+-----------------------+--------------------------------------------+

Purpose
-------

This packet is intended to be sent to all players in the vicinity of the emitting :term:`entity` each :term:`game tick`\ .
If the recipient is further away, he will receive this packet less frequent.

Structure
---------

Note that all examples shown here contain placeholder data and will have different content in actual packets.::

   {
   "time":13465

   "entity":"1ba7070a-22a7-4a0f-9f3b-df91f4ea7b65"
   "position":(331.29, 971.01, 566.98)
   }

The ``time`` is the timestamp in :term:`game ticks <game tick>`, at which the ``entity`` was at the specified ``position``\ .
Here, the ``time`` is the serverside game time.
