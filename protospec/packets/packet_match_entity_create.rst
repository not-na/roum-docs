
``roum:match.entity.create`` - Create new Entity
================================================

.. roum:packet:: roum:match.entity.create

This packet is used to create a new :term:`entity`\ .

+-----------------------+--------------------------------------------+
|Internal Name          |:roum:packet:`roum:match.entity.create`     |
+-----------------------+--------------------------------------------+
|Direction              |Clientbound                                 |
+-----------------------+--------------------------------------------+
|Since Version          |v0.1.0dev                                   |
+-----------------------+--------------------------------------------+
|Valid Modes            |``match`` only                              |
+-----------------------+--------------------------------------------+

Purpose
-------

This packet is intended to signal the new creation of a new :term:`entity`\ . This might either be a new launched
:term:`drone` or as well an object like an asteroid splitting in half or many ship wreckage debris after an explosion.
Differently to the :roum:packet:`roum:match.entity.update`\ , this packet is sent to all players and not only to those
in the vicinity.

Structure
---------

Note that all examples shown here contain placeholder data and will have different content in actual packets.

The structure of this packet is similar to :doc:`/format/entity_data` but does not contain all keys

.. todo::
   Specify the attributes of :py:class:`roum.Entity`

