
``roum:match.player.takedamage`` - Signalise the player that he took damage
===========================================================================

.. roum:packet:: roum:match.player.takedamage

This packet is used to tell a player that he took damage.

+-----------------------+--------------------------------------------+
|Internal Name          |:roum:packet:`roum:match.player.takedamage` |
+-----------------------+--------------------------------------------+
|Direction              |Clientbound                                 |
+-----------------------+--------------------------------------------+
|Since Version          |v0.1.0dev                                   |
+-----------------------+--------------------------------------------+
|Valid Modes            |``match`` only                              |
+-----------------------+--------------------------------------------+

Purpose
-------

This packet is intended to inform a player that he took damage. It will be sent each time he takes damage.

Structure
---------

Note that all examples shown here contain placeholder data and will have different content in actual packets.::

   {
   "time":8376

   "player":"1a0ab7f4-3225-42ea-9d62-052c874e25e7"
   "origin":"7082a2f1-f09a-4a4f-a264-281628db179a"
   "components":{...}
   }

The ``time`` is the timestamp in :term:`game ticks <game tick>`\ , at which the ``player`` took damage.
The ``origin`` is the source which damaged the ``player``\ . If the source was another player or one of his projectiles,
the player's uuid will be transmitted. If the player was damaged by an :term:`passive object`\ , the objects uuid will
be transmitted. Here, the ``time`` is the serverside time.

``components`` Structure
^^^^^^^^^^^^^^^^^^^^^^^^

``components`` is a mapping of all the :term:`ships components <ship component>` damaged.

Structure of ``component`` values:::

   {
   "shield":{"amount":203.15, "type":"laser"},
   "thruster_1":{"amount":15.93, "type":"laser"},
   ...
   }

.. todo::
Add list for components (And how do they even work?)

``amount`` indicates the amount of damage the specified component took. ``type`` indicates the
:term:`type <damage type>` of the damage.
