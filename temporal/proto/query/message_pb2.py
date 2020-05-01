# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/proto/query/message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporal.proto.common import message_pb2 as temporal_dot_proto_dot_common_dot_message__pb2
from temporal.proto.query import enum_pb2 as temporal_dot_proto_dot_query_dot_enum__pb2
from temporal.proto.execution import enum_pb2 as temporal_dot_proto_dot_execution_dot_enum__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='temporal/proto/query/message.proto',
  package='query',
  syntax='proto3',
  serialized_options=b'\n\027io.temporal.proto.queryP\001Z#go.temporal.io/temporal-proto/query',
  serialized_pb=b'\n\"temporal/proto/query/message.proto\x12\x05query\x1a#temporal/proto/common/message.proto\x1a\x1ftemporal/proto/query/enum.proto\x1a#temporal/proto/execution/enum.proto\"G\n\rWorkflowQuery\x12\x11\n\tqueryType\x18\x01 \x01(\t\x12#\n\tqueryArgs\x18\x02 \x01(\x0b\x32\x10.common.Payloads\"y\n\x13WorkflowQueryResult\x12*\n\nresultType\x18\x01 \x01(\x0e\x32\x16.query.QueryResultType\x12 \n\x06\x61nswer\x18\x02 \x01(\x0b\x32\x10.common.Payloads\x12\x14\n\x0c\x65rrorMessage\x18\x03 \x01(\t\"C\n\rQueryRejected\x12\x32\n\x06status\x18\x01 \x01(\x0e\x32\".execution.WorkflowExecutionStatusB@\n\x17io.temporal.proto.queryP\x01Z#go.temporal.io/temporal-proto/queryb\x06proto3'
  ,
  dependencies=[temporal_dot_proto_dot_common_dot_message__pb2.DESCRIPTOR,temporal_dot_proto_dot_query_dot_enum__pb2.DESCRIPTOR,temporal_dot_proto_dot_execution_dot_enum__pb2.DESCRIPTOR,])




_WORKFLOWQUERY = _descriptor.Descriptor(
  name='WorkflowQuery',
  full_name='query.WorkflowQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='queryType', full_name='query.WorkflowQuery.queryType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryArgs', full_name='query.WorkflowQuery.queryArgs', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=152,
  serialized_end=223,
)


_WORKFLOWQUERYRESULT = _descriptor.Descriptor(
  name='WorkflowQueryResult',
  full_name='query.WorkflowQueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resultType', full_name='query.WorkflowQueryResult.resultType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='answer', full_name='query.WorkflowQueryResult.answer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorMessage', full_name='query.WorkflowQueryResult.errorMessage', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=225,
  serialized_end=346,
)


_QUERYREJECTED = _descriptor.Descriptor(
  name='QueryRejected',
  full_name='query.QueryRejected',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='query.QueryRejected.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=348,
  serialized_end=415,
)

_WORKFLOWQUERY.fields_by_name['queryArgs'].message_type = temporal_dot_proto_dot_common_dot_message__pb2._PAYLOADS
_WORKFLOWQUERYRESULT.fields_by_name['resultType'].enum_type = temporal_dot_proto_dot_query_dot_enum__pb2._QUERYRESULTTYPE
_WORKFLOWQUERYRESULT.fields_by_name['answer'].message_type = temporal_dot_proto_dot_common_dot_message__pb2._PAYLOADS
_QUERYREJECTED.fields_by_name['status'].enum_type = temporal_dot_proto_dot_execution_dot_enum__pb2._WORKFLOWEXECUTIONSTATUS
DESCRIPTOR.message_types_by_name['WorkflowQuery'] = _WORKFLOWQUERY
DESCRIPTOR.message_types_by_name['WorkflowQueryResult'] = _WORKFLOWQUERYRESULT
DESCRIPTOR.message_types_by_name['QueryRejected'] = _QUERYREJECTED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkflowQuery = _reflection.GeneratedProtocolMessageType('WorkflowQuery', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWQUERY,
  '__module__' : 'temporal.proto.query.message_pb2'
  # @@protoc_insertion_point(class_scope:query.WorkflowQuery)
  })
_sym_db.RegisterMessage(WorkflowQuery)

WorkflowQueryResult = _reflection.GeneratedProtocolMessageType('WorkflowQueryResult', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWQUERYRESULT,
  '__module__' : 'temporal.proto.query.message_pb2'
  # @@protoc_insertion_point(class_scope:query.WorkflowQueryResult)
  })
_sym_db.RegisterMessage(WorkflowQueryResult)

QueryRejected = _reflection.GeneratedProtocolMessageType('QueryRejected', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREJECTED,
  '__module__' : 'temporal.proto.query.message_pb2'
  # @@protoc_insertion_point(class_scope:query.QueryRejected)
  })
_sym_db.RegisterMessage(QueryRejected)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
