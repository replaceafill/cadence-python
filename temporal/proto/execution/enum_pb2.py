# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/proto/execution/enum.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='temporal/proto/execution/enum.proto',
  package='execution',
  syntax='proto3',
  serialized_options=b'\n\033io.temporal.proto.executionP\001Z\'go.temporal.io/temporal-proto/execution',
  serialized_pb=b'\n#temporal/proto/execution/enum.proto\x12\texecution*\x8e\x01\n\x17WorkflowExecutionStatus\x12\x0b\n\x07Unknown\x10\x00\x12\x0b\n\x07Running\x10\x01\x12\r\n\tCompleted\x10\x02\x12\n\n\x06\x46\x61iled\x10\x03\x12\x0c\n\x08\x43\x61nceled\x10\x04\x12\x0e\n\nTerminated\x10\x05\x12\x12\n\x0e\x43ontinuedAsNew\x10\x06\x12\x0c\n\x08TimedOut\x10\x07*G\n\x14PendingActivityState\x12\r\n\tScheduled\x10\x00\x12\x0b\n\x07Started\x10\x01\x12\x13\n\x0f\x43\x61ncelRequested\x10\x02\x42H\n\x1bio.temporal.proto.executionP\x01Z\'go.temporal.io/temporal-proto/executionb\x06proto3'
)

_WORKFLOWEXECUTIONSTATUS = _descriptor.EnumDescriptor(
  name='WorkflowExecutionStatus',
  full_name='execution.WorkflowExecutionStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Running', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Completed', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Failed', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Canceled', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Terminated', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ContinuedAsNew', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TimedOut', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=51,
  serialized_end=193,
)
_sym_db.RegisterEnumDescriptor(_WORKFLOWEXECUTIONSTATUS)

WorkflowExecutionStatus = enum_type_wrapper.EnumTypeWrapper(_WORKFLOWEXECUTIONSTATUS)
_PENDINGACTIVITYSTATE = _descriptor.EnumDescriptor(
  name='PendingActivityState',
  full_name='execution.PendingActivityState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Scheduled', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Started', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CancelRequested', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=195,
  serialized_end=266,
)
_sym_db.RegisterEnumDescriptor(_PENDINGACTIVITYSTATE)

PendingActivityState = enum_type_wrapper.EnumTypeWrapper(_PENDINGACTIVITYSTATE)
Unknown = 0
Running = 1
Completed = 2
Failed = 3
Canceled = 4
Terminated = 5
ContinuedAsNew = 6
TimedOut = 7
Scheduled = 0
Started = 1
CancelRequested = 2


DESCRIPTOR.enum_types_by_name['WorkflowExecutionStatus'] = _WORKFLOWEXECUTIONSTATUS
DESCRIPTOR.enum_types_by_name['PendingActivityState'] = _PENDINGACTIVITYSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
