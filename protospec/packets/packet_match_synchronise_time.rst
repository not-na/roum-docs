
``roum:match.synchronise.time`` - Synchronising Game Ticks
==========================================================

.. roum:packet:: roum:match.synchronise.time

This packet is used to synchronise the clientside and serverside :term:`game ticks <game tick>`\ .

+-----------------------+--------------------------------------------+
|Internal Name          |:roum:packet:`roum:match.synchronise.time`  |
+-----------------------+--------------------------------------------+
|Direction              |Clientbound                                 |
+-----------------------+--------------------------------------------+
|Since Version          |v0.1.0dev                                   |
+-----------------------+--------------------------------------------+
|Valid Modes            |``match`` only                              |
+-----------------------+--------------------------------------------+

Purpose
-------

This packet is intended to synchronise the inferior clientside :term:`game ticks <game tick>` to the superior serverside game ticks.
This synchronisation occurs each second (60 game ticks) and is sent to all players.

Structure
---------

Note that all examples shown here contain placeholder data and will have different content in actual packets.::

   {
   "time":8345
   }

The ``time`` is the serverside time in :term:`game ticks <game tick>`\ .
