
``roum:match.status.update`` - Update the Game Status
=========================================================

.. roum:packet:: roum:match.status.update

This packet is used to update the game status.

+-----------------------+--------------------------------------------+
|Internal Name          |:roum:packet:`roum:match.status.update`     |
+-----------------------+--------------------------------------------+
|Direction              |Cliendbound                                 |
+-----------------------+--------------------------------------------+
|Since Version          |v0.1.0dev                                   |
+-----------------------+--------------------------------------------+
|Valid Modes            |``match`` only                              |
+-----------------------+--------------------------------------------+

Purpose
-------

This packet is intended to update major information concerning the game status, like the begin and the end of an match.

Structure
---------

Note that all examples shown here contain placeholder data and will have different content in actual packets.::

   {
   "time":0

   "status":{...}
   }

The ``time`` is the timestamp in :term:`game ticks <game tick>`\ , at which the ``status`` was updated.
Here, the ``time`` is the serverside time.

``status`` Structure
^^^^^^^^^^^^^^^^^^^^

Note that all examples shown here contain placeholder data and will have different content in actual packets.

.. todo::
   Specify the attributes of :py:class:`roum.Match`
