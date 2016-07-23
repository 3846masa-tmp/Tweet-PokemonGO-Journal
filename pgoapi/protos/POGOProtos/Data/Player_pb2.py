# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Data.Player.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos import Enums_pb2 as POGOProtos_dot_Enums__pb2

from POGOProtos.Enums_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos.Data.Player.proto',
  package='POGOProtos.Data.Player',
  syntax='proto3',
  serialized_pb=_b('\n\x1cPOGOProtos.Data.Player.proto\x12\x16POGOProtos.Data.Player\x1a\x16POGOProtos.Enums.proto\"Q\n\x0f\x43ontactSettings\x12\x1d\n\x15send_marketing_emails\x18\x01 \x01(\x08\x12\x1f\n\x17send_push_notifications\x18\x02 \x01(\x08\"(\n\x08\x43urrency\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\"\xae\x01\n\x0cPlayerAvatar\x12\x0c\n\x04skin\x18\x02 \x01(\x05\x12\x0c\n\x04hair\x18\x03 \x01(\x05\x12\r\n\x05shirt\x18\x04 \x01(\x05\x12\r\n\x05pants\x18\x05 \x01(\x05\x12\x0b\n\x03hat\x18\x06 \x01(\x05\x12\r\n\x05shoes\x18\x07 \x01(\x05\x12(\n\x06gender\x18\x08 \x01(\x0e\x32\x18.POGOProtos.Enums.Gender\x12\x0c\n\x04\x65yes\x18\t \x01(\x05\x12\x10\n\x08\x62\x61\x63kpack\x18\n \x01(\x05\"\x1e\n\x0ePlayerCurrency\x12\x0c\n\x04gems\x18\x01 \x01(\x05\"\xed\x04\n\x0bPlayerStats\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x12\n\nexperience\x18\x02 \x01(\x03\x12\x15\n\rprev_level_xp\x18\x03 \x01(\x03\x12\x15\n\rnext_level_xp\x18\x04 \x01(\x03\x12\x11\n\tkm_walked\x18\x05 \x01(\x02\x12\x1c\n\x14pokemons_encountered\x18\x06 \x01(\x05\x12\x1e\n\x16unique_pokedex_entries\x18\x07 \x01(\x05\x12\x19\n\x11pokemons_captured\x18\x08 \x01(\x05\x12\x12\n\nevolutions\x18\t \x01(\x05\x12\x18\n\x10poke_stop_visits\x18\n \x01(\x05\x12\x18\n\x10pokeballs_thrown\x18\x0b \x01(\x05\x12\x14\n\x0c\x65ggs_hatched\x18\x0c \x01(\x05\x12\x1b\n\x13\x62ig_magikarp_caught\x18\r \x01(\x05\x12\x19\n\x11\x62\x61ttle_attack_won\x18\x0e \x01(\x05\x12\x1b\n\x13\x62\x61ttle_attack_total\x18\x0f \x01(\x05\x12\x1b\n\x13\x62\x61ttle_defended_won\x18\x10 \x01(\x05\x12\x1b\n\x13\x62\x61ttle_training_won\x18\x11 \x01(\x05\x12\x1d\n\x15\x62\x61ttle_training_total\x18\x12 \x01(\x05\x12\x1d\n\x15prestige_raised_total\x18\x13 \x01(\x05\x12\x1e\n\x16prestige_dropped_total\x18\x14 \x01(\x05\x12\x18\n\x10pokemon_deployed\x18\x15 \x01(\x05\x12\x1e\n\x16pokemon_caught_by_type\x18\x16 \x01(\x0c\x12\x1c\n\x14small_rattata_caught\x18\x17 \x01(\x05\"c\n\nDailyBonus\x12#\n\x1bnext_collected_timestamp_ms\x18\x01 \x01(\x03\x12\x30\n(next_defender_bonus_collect_timestamp_ms\x18\x02 \x01(\x03\")\n\x0cPlayerCamera\x12\x19\n\x11is_default_camera\x18\x01 \x01(\x08\"\x7f\n\rEquippedBadge\x12/\n\nbadge_type\x18\x01 \x01(\x0e\x32\x1b.POGOProtos.Enums.BadgeType\x12\r\n\x05level\x18\x02 \x01(\x05\x12.\n&next_equip_change_allowed_timestamp_ms\x18\x03 \x01(\x03\"h\n\x13PlayerPublicProfile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05level\x18\x02 \x01(\x05\x12\x34\n\x06\x61vatar\x18\x03 \x01(\x0b\x32$.POGOProtos.Data.Player.PlayerAvatarP\x00\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONTACTSETTINGS = _descriptor.Descriptor(
  name='ContactSettings',
  full_name='POGOProtos.Data.Player.ContactSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='send_marketing_emails', full_name='POGOProtos.Data.Player.ContactSettings.send_marketing_emails', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_push_notifications', full_name='POGOProtos.Data.Player.ContactSettings.send_push_notifications', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=161,
)


_CURRENCY = _descriptor.Descriptor(
  name='Currency',
  full_name='POGOProtos.Data.Player.Currency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='POGOProtos.Data.Player.Currency.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='POGOProtos.Data.Player.Currency.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=203,
)


_PLAYERAVATAR = _descriptor.Descriptor(
  name='PlayerAvatar',
  full_name='POGOProtos.Data.Player.PlayerAvatar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skin', full_name='POGOProtos.Data.Player.PlayerAvatar.skin', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hair', full_name='POGOProtos.Data.Player.PlayerAvatar.hair', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shirt', full_name='POGOProtos.Data.Player.PlayerAvatar.shirt', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pants', full_name='POGOProtos.Data.Player.PlayerAvatar.pants', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hat', full_name='POGOProtos.Data.Player.PlayerAvatar.hat', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shoes', full_name='POGOProtos.Data.Player.PlayerAvatar.shoes', index=5,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender', full_name='POGOProtos.Data.Player.PlayerAvatar.gender', index=6,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eyes', full_name='POGOProtos.Data.Player.PlayerAvatar.eyes', index=7,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backpack', full_name='POGOProtos.Data.Player.PlayerAvatar.backpack', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=380,
)


_PLAYERCURRENCY = _descriptor.Descriptor(
  name='PlayerCurrency',
  full_name='POGOProtos.Data.Player.PlayerCurrency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gems', full_name='POGOProtos.Data.Player.PlayerCurrency.gems', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=412,
)


_PLAYERSTATS = _descriptor.Descriptor(
  name='PlayerStats',
  full_name='POGOProtos.Data.Player.PlayerStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='POGOProtos.Data.Player.PlayerStats.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experience', full_name='POGOProtos.Data.Player.PlayerStats.experience', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prev_level_xp', full_name='POGOProtos.Data.Player.PlayerStats.prev_level_xp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_level_xp', full_name='POGOProtos.Data.Player.PlayerStats.next_level_xp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='km_walked', full_name='POGOProtos.Data.Player.PlayerStats.km_walked', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemons_encountered', full_name='POGOProtos.Data.Player.PlayerStats.pokemons_encountered', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_pokedex_entries', full_name='POGOProtos.Data.Player.PlayerStats.unique_pokedex_entries', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemons_captured', full_name='POGOProtos.Data.Player.PlayerStats.pokemons_captured', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolutions', full_name='POGOProtos.Data.Player.PlayerStats.evolutions', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poke_stop_visits', full_name='POGOProtos.Data.Player.PlayerStats.poke_stop_visits', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokeballs_thrown', full_name='POGOProtos.Data.Player.PlayerStats.pokeballs_thrown', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eggs_hatched', full_name='POGOProtos.Data.Player.PlayerStats.eggs_hatched', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='big_magikarp_caught', full_name='POGOProtos.Data.Player.PlayerStats.big_magikarp_caught', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_attack_won', full_name='POGOProtos.Data.Player.PlayerStats.battle_attack_won', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_attack_total', full_name='POGOProtos.Data.Player.PlayerStats.battle_attack_total', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_defended_won', full_name='POGOProtos.Data.Player.PlayerStats.battle_defended_won', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_training_won', full_name='POGOProtos.Data.Player.PlayerStats.battle_training_won', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_training_total', full_name='POGOProtos.Data.Player.PlayerStats.battle_training_total', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prestige_raised_total', full_name='POGOProtos.Data.Player.PlayerStats.prestige_raised_total', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prestige_dropped_total', full_name='POGOProtos.Data.Player.PlayerStats.prestige_dropped_total', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_deployed', full_name='POGOProtos.Data.Player.PlayerStats.pokemon_deployed', index=20,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_caught_by_type', full_name='POGOProtos.Data.Player.PlayerStats.pokemon_caught_by_type', index=21,
      number=22, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='small_rattata_caught', full_name='POGOProtos.Data.Player.PlayerStats.small_rattata_caught', index=22,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=415,
  serialized_end=1036,
)


_DAILYBONUS = _descriptor.Descriptor(
  name='DailyBonus',
  full_name='POGOProtos.Data.Player.DailyBonus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_collected_timestamp_ms', full_name='POGOProtos.Data.Player.DailyBonus.next_collected_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_defender_bonus_collect_timestamp_ms', full_name='POGOProtos.Data.Player.DailyBonus.next_defender_bonus_collect_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1038,
  serialized_end=1137,
)


_PLAYERCAMERA = _descriptor.Descriptor(
  name='PlayerCamera',
  full_name='POGOProtos.Data.Player.PlayerCamera',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_default_camera', full_name='POGOProtos.Data.Player.PlayerCamera.is_default_camera', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1139,
  serialized_end=1180,
)


_EQUIPPEDBADGE = _descriptor.Descriptor(
  name='EquippedBadge',
  full_name='POGOProtos.Data.Player.EquippedBadge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='badge_type', full_name='POGOProtos.Data.Player.EquippedBadge.badge_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='POGOProtos.Data.Player.EquippedBadge.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_equip_change_allowed_timestamp_ms', full_name='POGOProtos.Data.Player.EquippedBadge.next_equip_change_allowed_timestamp_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1182,
  serialized_end=1309,
)


_PLAYERPUBLICPROFILE = _descriptor.Descriptor(
  name='PlayerPublicProfile',
  full_name='POGOProtos.Data.Player.PlayerPublicProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='POGOProtos.Data.Player.PlayerPublicProfile.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='POGOProtos.Data.Player.PlayerPublicProfile.level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='POGOProtos.Data.Player.PlayerPublicProfile.avatar', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1311,
  serialized_end=1415,
)

_PLAYERAVATAR.fields_by_name['gender'].enum_type = POGOProtos_dot_Enums__pb2._GENDER
_EQUIPPEDBADGE.fields_by_name['badge_type'].enum_type = POGOProtos_dot_Enums__pb2._BADGETYPE
_PLAYERPUBLICPROFILE.fields_by_name['avatar'].message_type = _PLAYERAVATAR
DESCRIPTOR.message_types_by_name['ContactSettings'] = _CONTACTSETTINGS
DESCRIPTOR.message_types_by_name['Currency'] = _CURRENCY
DESCRIPTOR.message_types_by_name['PlayerAvatar'] = _PLAYERAVATAR
DESCRIPTOR.message_types_by_name['PlayerCurrency'] = _PLAYERCURRENCY
DESCRIPTOR.message_types_by_name['PlayerStats'] = _PLAYERSTATS
DESCRIPTOR.message_types_by_name['DailyBonus'] = _DAILYBONUS
DESCRIPTOR.message_types_by_name['PlayerCamera'] = _PLAYERCAMERA
DESCRIPTOR.message_types_by_name['EquippedBadge'] = _EQUIPPEDBADGE
DESCRIPTOR.message_types_by_name['PlayerPublicProfile'] = _PLAYERPUBLICPROFILE

ContactSettings = _reflection.GeneratedProtocolMessageType('ContactSettings', (_message.Message,), dict(
  DESCRIPTOR = _CONTACTSETTINGS,
  __module__ = 'POGOProtos.Data.Player_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.ContactSettings)
  ))
_sym_db.RegisterMessage(ContactSettings)

Currency = _reflection.GeneratedProtocolMessageType('Currency', (_message.Message,), dict(
  DESCRIPTOR = _CURRENCY,
  __module__ = 'POGOProtos.Data.Player_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.Currency)
  ))
_sym_db.RegisterMessage(Currency)

PlayerAvatar = _reflection.GeneratedProtocolMessageType('PlayerAvatar', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERAVATAR,
  __module__ = 'POGOProtos.Data.Player_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.PlayerAvatar)
  ))
_sym_db.RegisterMessage(PlayerAvatar)

PlayerCurrency = _reflection.GeneratedProtocolMessageType('PlayerCurrency', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERCURRENCY,
  __module__ = 'POGOProtos.Data.Player_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.PlayerCurrency)
  ))
_sym_db.RegisterMessage(PlayerCurrency)

PlayerStats = _reflection.GeneratedProtocolMessageType('PlayerStats', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERSTATS,
  __module__ = 'POGOProtos.Data.Player_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.PlayerStats)
  ))
_sym_db.RegisterMessage(PlayerStats)

DailyBonus = _reflection.GeneratedProtocolMessageType('DailyBonus', (_message.Message,), dict(
  DESCRIPTOR = _DAILYBONUS,
  __module__ = 'POGOProtos.Data.Player_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.DailyBonus)
  ))
_sym_db.RegisterMessage(DailyBonus)

PlayerCamera = _reflection.GeneratedProtocolMessageType('PlayerCamera', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERCAMERA,
  __module__ = 'POGOProtos.Data.Player_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.PlayerCamera)
  ))
_sym_db.RegisterMessage(PlayerCamera)

EquippedBadge = _reflection.GeneratedProtocolMessageType('EquippedBadge', (_message.Message,), dict(
  DESCRIPTOR = _EQUIPPEDBADGE,
  __module__ = 'POGOProtos.Data.Player_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.EquippedBadge)
  ))
_sym_db.RegisterMessage(EquippedBadge)

PlayerPublicProfile = _reflection.GeneratedProtocolMessageType('PlayerPublicProfile', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERPUBLICPROFILE,
  __module__ = 'POGOProtos.Data.Player_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Player.PlayerPublicProfile)
  ))
_sym_db.RegisterMessage(PlayerPublicProfile)


# @@protoc_insertion_point(module_scope)
