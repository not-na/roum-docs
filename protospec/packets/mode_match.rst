
``match`` Connection Mode
=========================

Purpose
-------

After leaving the :doc:`lobby <mode_lobby>`, all data transmissions concerning the game itself (all
non-:doc:`chat<mode_chat>` data) will use this mode.

Packets
-------

.. toctree::
   :maxdepth: 1

   packet_match_init

   packet_match_status_update
   packet_match_synchronise_time

   packet_match_player_update_pos
   packet_match_entity_update_pos

   packet_match_player_update
   packet_match_player_takedamage

   packet_match_entity_create
   packet_match_entity_update
   packet_match_entity_takedamage
   packet_match_entity_remove

   packet_match_sfx_play
   packet_match_vfx_particle
   packet_match_vfx_effect
