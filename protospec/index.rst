
Roum Multiplayer Protocol Specification
=======================================

This section of the documentation describes the protocol used to communicate
between the client and server.

The protocol is based on a single TCP Connection per client. This allows for
great compatibility and connection security, due to TCPs automatic packet validation
and re-sending.


Protocol Specification Index
----------------------------

.. toctree::
   :maxdepth: 2
   
   abstract
   lowlevel
   
   packets/mode_ping
   packets/mode_auth
   packets/mode_lobby
   packets/mode_match
   packets/mode_chat

Packets
^^^^^^^

``auth`` Connection Mode
""""""""""""""""""""""""

.. toctree::
   :maxdepth: 1

   packets/packet_auth

``lobby`` Connection Mode
"""""""""""""""""""""""""

.. toctree::
   :maxdepth: 1

   packets/packet_info_server
   packets/packet_info_otherplayers

   packets/packet_clientsettings
   packets/packet_clientstatus
   packets/packet_player_features

   packets/packet_lobby

``match`` Connection Mode
"""""""""""""""""""""""""

.. toctree::
   :maxdepth: 1

   packets/packet_match_entity_create
   packets/packet_match_entity_remove
   packets/packet_match_entity_takedamage
   packets/packet_match_entity_update
   packets/packet_match_entity_update_pos

   packets/packet_match_player_takedamage
   packets/packet_match_player_update
   packets/packet_match_player_update_pos

   packets/packet_match_sfx_play

   packets/packet_match_status_update
   packets/packet_match_synchronise_time

   packets/packet_match_vfx_effect
   packets/packet_match_vfx_particle

``chat`` Connection Mode
""""""""""""""""""""""""

.. toctree::
   :maxdepth: 1

   packets/packet_chat_channel_subscribe
   packets/packet_chat_channel_unsubscribe
   packets/packet_chat_message
