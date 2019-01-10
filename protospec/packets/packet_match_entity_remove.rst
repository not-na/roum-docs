
``roum:match.entity.remove`` - Removes an Entity
================================================

.. roum:packet:: roum:match.entity.remove

This packet is used to remove an :term:`entity`\ .

+-----------------------+--------------------------------------------+
|Internal Name          |:roum:packet:`roum:match.entity.remove`     |
+-----------------------+--------------------------------------------+
|Direction              |Clientbound                                 |
+-----------------------+--------------------------------------------+
|Since Version          |v0.1.0dev                                   |
+-----------------------+--------------------------------------------+
|Valid Modes            |``match`` only                              |
+-----------------------+--------------------------------------------+

Purpose
-------

This packet is used to inform players of the removal of an :term:`entity`\ . Such a case might occur when a
:term:`weapon factory` is destroyed or when a projectile impacts another entity.

Structure
---------

Note that all examples shown here contain placeholder data and will have different content in actual packets.::

   {
   "time":3780

   "entity":"76874380-20f7-42e3-aefb-46a8dca98d03"
   }


The ``time`` is the timestamp in :term:`game ticks <game tick>`, at which the ``entity`` was removed.
Here, the ``time`` is the serverside game time.