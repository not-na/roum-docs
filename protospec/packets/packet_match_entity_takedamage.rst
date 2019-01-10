
``roum:match.entity.takedamage`` - Signalise an entity took damage
==================================================================

.. roum:packet:: roum:match.entity.takedamage

This packet is used to tell a player that an entity took damage.

+-----------------------+--------------------------------------------+
|Internal Name          |:roum:packet:`roum:match.entity.takedamage` |
+-----------------------+--------------------------------------------+
|Direction              |Clientbound                                 |
+-----------------------+--------------------------------------------+
|Since Version          |v0.1.0dev                                   |
+-----------------------+--------------------------------------------+
|Valid Modes            |``match`` only                              |
+-----------------------+--------------------------------------------+

Purpose
-------

This packet is intended to signalise to a player that a certain entity took damage. This can be beneficial to inform the
player that for example one of his :term:`drones <drone>` or an allied :term:`weapon factory` is being attacked.

Structure
---------

Note that all examples shown here contain placeholder data and will have different content in actual packets.::

   {
   "time":8374

   "entity":"94e28628-b83d-498a-8dce-8e2cbc8aff3f"
   "origin":"0dd967e3-d418-4815-b347-feecb1d1eb6d"
   "components":{...}
   }

The ``time`` is the timestamp in :term:`game ticks <game tick>`\ , at which the ``entity`` took damage.
The ``origin`` is the source which damaged the ``entity``\ . If the source was another player or one of his projectiles,
the player's uuid will be transmitted. If the player was damaged by an :term:`passive object`\ , the objects uuid will
be transmitted. Here, the ``time`` is the serverside time.

``components`` Structure
^^^^^^^^^^^^^^^^^^^^^^^^

``components`` is a mapping of all the :term:`entities components <entity component>` damaged.

Structure of ``component`` values:::

   {
   "warhead":{"amount":24.13, "type":"ion"},
   "body":{"amount":96.67, "type":"ion"},
   ...
   }

.. todo::
Add list for components (And how do they even work?)

``amount`` indicates the amount of damage the specified component took. ``type`` indicates the
:term:`type <damage type>` of the damage.
