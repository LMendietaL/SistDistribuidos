# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: counter.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcounter.proto\x12\rlettercounter\"\x17\n\x04Text\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"\x16\n\x05\x43ount\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x32J\n\rLetterCounter\x12\x39\n\x0c\x43ountLetters\x12\x13.lettercounter.Text\x1a\x14.lettercounter.Countb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'counter_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TEXT']._serialized_start=32
  _globals['_TEXT']._serialized_end=55
  _globals['_COUNT']._serialized_start=57
  _globals['_COUNT']._serialized_end=79
  _globals['_LETTERCOUNTER']._serialized_start=81
  _globals['_LETTERCOUNTER']._serialized_end=155
# @@protoc_insertion_point(module_scope)
