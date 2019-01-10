
``roum:match.entity.update`` - Update Entity
================================================

.. roum:packet:: roum:match.entity.update

This packet is used to update the status of :term:`entities <entity>`\ .

+-----------------------+--------------------------------------------+
|Internal Name          |:roum:packet:`roum:match.entity.update`     |
+-----------------------+--------------------------------------------+
|Direction              |Clientbound                                 |
+-----------------------+--------------------------------------------+
|Since Version          |v0.1.0dev                                   |
+-----------------------+--------------------------------------------+
|Valid Modes            |``match`` only                              |
+-----------------------+--------------------------------------------+

Purpose
-------

This packet is intended to pass the status of an :term:`entity` to all players in the vicinity. It is always emitted
when an attribute of the entity changes. Players to far away to be impacted by the status change will only receive an
update flag that will trigger the necessary updates as soon as they get close enough to the entity.

Structure
---------

Note that all examples shown here contain placeholder data and will have different content in actual packets.

The structure of this packet is similar to :doc:`/format/entity_data` but does not contain all keys

.. todo::
   Specify the attributes of :py:class:`roum.Entity`

