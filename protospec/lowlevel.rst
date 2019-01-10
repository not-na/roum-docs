
Low-Level Implementation
========================

Framework
---------

The actual handling of sending and receiving packets is done via :py:mod:`peng3dnet`\ .
This module was developed specifically for use with :py:mod:`peng3d`\ , which is
the graphics framework used for rendering.

The :py:mod:`peng3dnet` module also includes extensions that allow for simple
and (somewhat) secure pinging and location syncing.

On the Wire
-----------

The actual format of packets including headers is described in the :py:mod:`peng3dnet`
documentation.

The payloads sent are encoded using `MessagePack <https://msgpack.org>`_ due to
its various advantages, including low overhead in both speed and serialized data size.

In this documentation, all specifications will only describe the contents of the
payload as if it were encoded as a Python :py:class:`dict`\ .
This is done mainly to simplify the documentation, as all the low-level encoding
is done by :py:mod:`peng3dnet` and not needed for a good understanding of the protocol itself.
