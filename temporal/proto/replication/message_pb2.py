# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/proto/replication/message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='temporal/proto/replication/message.proto',
  package='replication',
  syntax='proto3',
  serialized_options=b'\n\035io.temporal.proto.replicationP\001Z)go.temporal.io/temporal-proto/replication',
  serialized_pb=b'\n(temporal/proto/replication/message.proto\x12\x0breplication\"6\n\x1f\x43lusterReplicationConfiguration\x12\x13\n\x0b\x63lusterName\x18\x01 \x01(\t\"~\n!NamespaceReplicationConfiguration\x12\x19\n\x11\x61\x63tiveClusterName\x18\x01 \x01(\t\x12>\n\x08\x63lusters\x18\x02 \x03(\x0b\x32,.replication.ClusterReplicationConfigurationBL\n\x1dio.temporal.proto.replicationP\x01Z)go.temporal.io/temporal-proto/replicationb\x06proto3'
)




_CLUSTERREPLICATIONCONFIGURATION = _descriptor.Descriptor(
  name='ClusterReplicationConfiguration',
  full_name='replication.ClusterReplicationConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clusterName', full_name='replication.ClusterReplicationConfiguration.clusterName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=111,
)


_NAMESPACEREPLICATIONCONFIGURATION = _descriptor.Descriptor(
  name='NamespaceReplicationConfiguration',
  full_name='replication.NamespaceReplicationConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activeClusterName', full_name='replication.NamespaceReplicationConfiguration.activeClusterName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clusters', full_name='replication.NamespaceReplicationConfiguration.clusters', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=239,
)

_NAMESPACEREPLICATIONCONFIGURATION.fields_by_name['clusters'].message_type = _CLUSTERREPLICATIONCONFIGURATION
DESCRIPTOR.message_types_by_name['ClusterReplicationConfiguration'] = _CLUSTERREPLICATIONCONFIGURATION
DESCRIPTOR.message_types_by_name['NamespaceReplicationConfiguration'] = _NAMESPACEREPLICATIONCONFIGURATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClusterReplicationConfiguration = _reflection.GeneratedProtocolMessageType('ClusterReplicationConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERREPLICATIONCONFIGURATION,
  '__module__' : 'temporal.proto.replication.message_pb2'
  # @@protoc_insertion_point(class_scope:replication.ClusterReplicationConfiguration)
  })
_sym_db.RegisterMessage(ClusterReplicationConfiguration)

NamespaceReplicationConfiguration = _reflection.GeneratedProtocolMessageType('NamespaceReplicationConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACEREPLICATIONCONFIGURATION,
  '__module__' : 'temporal.proto.replication.message_pb2'
  # @@protoc_insertion_point(class_scope:replication.NamespaceReplicationConfiguration)
  })
_sym_db.RegisterMessage(NamespaceReplicationConfiguration)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)