# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/proto/workflowservice/service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporal.proto.workflowservice import request_response_pb2 as temporal_dot_proto_dot_workflowservice_dot_request__response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='temporal/proto/workflowservice/service.proto',
  package='workflowservice',
  syntax='proto3',
  serialized_options=b'\n!io.temporal.proto.workflowserviceP\001Z-go.temporal.io/temporal-proto/workflowservice',
  serialized_pb=b'\n,temporal/proto/workflowservice/service.proto\x12\x0fworkflowservice\x1a\x35temporal/proto/workflowservice/request_response.proto2\xce&\n\x0fWorkflowService\x12l\n\x11RegisterNamespace\x12).workflowservice.RegisterNamespaceRequest\x1a*.workflowservice.RegisterNamespaceResponse\"\x00\x12l\n\x11\x44\x65scribeNamespace\x12).workflowservice.DescribeNamespaceRequest\x1a*.workflowservice.DescribeNamespaceResponse\"\x00\x12\x63\n\x0eListNamespaces\x12&.workflowservice.ListNamespacesRequest\x1a\'.workflowservice.ListNamespacesResponse\"\x00\x12\x66\n\x0fUpdateNamespace\x12\'.workflowservice.UpdateNamespaceRequest\x1a(.workflowservice.UpdateNamespaceResponse\"\x00\x12o\n\x12\x44\x65precateNamespace\x12*.workflowservice.DeprecateNamespaceRequest\x1a+.workflowservice.DeprecateNamespaceResponse\"\x00\x12{\n\x16StartWorkflowExecution\x12..workflowservice.StartWorkflowExecutionRequest\x1a/.workflowservice.StartWorkflowExecutionResponse\"\x00\x12\x8a\x01\n\x1bGetWorkflowExecutionHistory\x12\x33.workflowservice.GetWorkflowExecutionHistoryRequest\x1a\x34.workflowservice.GetWorkflowExecutionHistoryResponse\"\x00\x12r\n\x13PollForDecisionTask\x12+.workflowservice.PollForDecisionTaskRequest\x1a,.workflowservice.PollForDecisionTaskResponse\"\x00\x12\x8d\x01\n\x1cRespondDecisionTaskCompleted\x12\x34.workflowservice.RespondDecisionTaskCompletedRequest\x1a\x35.workflowservice.RespondDecisionTaskCompletedResponse\"\x00\x12\x84\x01\n\x19RespondDecisionTaskFailed\x12\x31.workflowservice.RespondDecisionTaskFailedRequest\x1a\x32.workflowservice.RespondDecisionTaskFailedResponse\"\x00\x12r\n\x13PollForActivityTask\x12+.workflowservice.PollForActivityTaskRequest\x1a,.workflowservice.PollForActivityTaskResponse\"\x00\x12\x8a\x01\n\x1bRecordActivityTaskHeartbeat\x12\x33.workflowservice.RecordActivityTaskHeartbeatRequest\x1a\x34.workflowservice.RecordActivityTaskHeartbeatResponse\"\x00\x12\x96\x01\n\x1fRecordActivityTaskHeartbeatById\x12\x37.workflowservice.RecordActivityTaskHeartbeatByIdRequest\x1a\x38.workflowservice.RecordActivityTaskHeartbeatByIdResponse\"\x00\x12\x8d\x01\n\x1cRespondActivityTaskCompleted\x12\x34.workflowservice.RespondActivityTaskCompletedRequest\x1a\x35.workflowservice.RespondActivityTaskCompletedResponse\"\x00\x12\x99\x01\n RespondActivityTaskCompletedById\x12\x38.workflowservice.RespondActivityTaskCompletedByIdRequest\x1a\x39.workflowservice.RespondActivityTaskCompletedByIdResponse\"\x00\x12\x84\x01\n\x19RespondActivityTaskFailed\x12\x31.workflowservice.RespondActivityTaskFailedRequest\x1a\x32.workflowservice.RespondActivityTaskFailedResponse\"\x00\x12\x90\x01\n\x1dRespondActivityTaskFailedById\x12\x35.workflowservice.RespondActivityTaskFailedByIdRequest\x1a\x36.workflowservice.RespondActivityTaskFailedByIdResponse\"\x00\x12\x8a\x01\n\x1bRespondActivityTaskCanceled\x12\x33.workflowservice.RespondActivityTaskCanceledRequest\x1a\x34.workflowservice.RespondActivityTaskCanceledResponse\"\x00\x12\x96\x01\n\x1fRespondActivityTaskCanceledById\x12\x37.workflowservice.RespondActivityTaskCanceledByIdRequest\x1a\x38.workflowservice.RespondActivityTaskCanceledByIdResponse\"\x00\x12\x93\x01\n\x1eRequestCancelWorkflowExecution\x12\x36.workflowservice.RequestCancelWorkflowExecutionRequest\x1a\x37.workflowservice.RequestCancelWorkflowExecutionResponse\"\x00\x12~\n\x17SignalWorkflowExecution\x12/.workflowservice.SignalWorkflowExecutionRequest\x1a\x30.workflowservice.SignalWorkflowExecutionResponse\"\x00\x12\x99\x01\n SignalWithStartWorkflowExecution\x12\x38.workflowservice.SignalWithStartWorkflowExecutionRequest\x1a\x39.workflowservice.SignalWithStartWorkflowExecutionResponse\"\x00\x12{\n\x16ResetWorkflowExecution\x12..workflowservice.ResetWorkflowExecutionRequest\x1a/.workflowservice.ResetWorkflowExecutionResponse\"\x00\x12\x87\x01\n\x1aTerminateWorkflowExecution\x12\x32.workflowservice.TerminateWorkflowExecutionRequest\x1a\x33.workflowservice.TerminateWorkflowExecutionResponse\"\x00\x12\x87\x01\n\x1aListOpenWorkflowExecutions\x12\x32.workflowservice.ListOpenWorkflowExecutionsRequest\x1a\x33.workflowservice.ListOpenWorkflowExecutionsResponse\"\x00\x12\x8d\x01\n\x1cListClosedWorkflowExecutions\x12\x34.workflowservice.ListClosedWorkflowExecutionsRequest\x1a\x35.workflowservice.ListClosedWorkflowExecutionsResponse\"\x00\x12{\n\x16ListWorkflowExecutions\x12..workflowservice.ListWorkflowExecutionsRequest\x1a/.workflowservice.ListWorkflowExecutionsResponse\"\x00\x12\x93\x01\n\x1eListArchivedWorkflowExecutions\x12\x36.workflowservice.ListArchivedWorkflowExecutionsRequest\x1a\x37.workflowservice.ListArchivedWorkflowExecutionsResponse\"\x00\x12{\n\x16ScanWorkflowExecutions\x12..workflowservice.ScanWorkflowExecutionsRequest\x1a/.workflowservice.ScanWorkflowExecutionsResponse\"\x00\x12~\n\x17\x43ountWorkflowExecutions\x12/.workflowservice.CountWorkflowExecutionsRequest\x1a\x30.workflowservice.CountWorkflowExecutionsResponse\"\x00\x12r\n\x13GetSearchAttributes\x12+.workflowservice.GetSearchAttributesRequest\x1a,.workflowservice.GetSearchAttributesResponse\"\x00\x12\x84\x01\n\x19RespondQueryTaskCompleted\x12\x31.workflowservice.RespondQueryTaskCompletedRequest\x1a\x32.workflowservice.RespondQueryTaskCompletedResponse\"\x00\x12r\n\x13ResetStickyTaskList\x12+.workflowservice.ResetStickyTaskListRequest\x1a,.workflowservice.ResetStickyTaskListResponse\"\x00\x12`\n\rQueryWorkflow\x12%.workflowservice.QueryWorkflowRequest\x1a&.workflowservice.QueryWorkflowResponse\"\x00\x12\x84\x01\n\x19\x44\x65scribeWorkflowExecution\x12\x31.workflowservice.DescribeWorkflowExecutionRequest\x1a\x32.workflowservice.DescribeWorkflowExecutionResponse\"\x00\x12i\n\x10\x44\x65scribeTaskList\x12(.workflowservice.DescribeTaskListRequest\x1a).workflowservice.DescribeTaskListResponse\"\x00\x12\x63\n\x0eGetClusterInfo\x12&.workflowservice.GetClusterInfoRequest\x1a\'.workflowservice.GetClusterInfoResponse\"\x00\x12{\n\x16ListTaskListPartitions\x12..workflowservice.ListTaskListPartitionsRequest\x1a/.workflowservice.ListTaskListPartitionsResponse\"\x00\x42T\n!io.temporal.proto.workflowserviceP\x01Z-go.temporal.io/temporal-proto/workflowserviceb\x06proto3'
  ,
  dependencies=[temporal_dot_proto_dot_workflowservice_dot_request__response__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_WORKFLOWSERVICE = _descriptor.ServiceDescriptor(
  name='WorkflowService',
  full_name='workflowservice.WorkflowService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=121,
  serialized_end=5063,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterNamespace',
    full_name='workflowservice.WorkflowService.RegisterNamespace',
    index=0,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._REGISTERNAMESPACEREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._REGISTERNAMESPACERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeNamespace',
    full_name='workflowservice.WorkflowService.DescribeNamespace',
    index=1,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._DESCRIBENAMESPACEREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._DESCRIBENAMESPACERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListNamespaces',
    full_name='workflowservice.WorkflowService.ListNamespaces',
    index=2,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTNAMESPACESREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTNAMESPACESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateNamespace',
    full_name='workflowservice.WorkflowService.UpdateNamespace',
    index=3,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._UPDATENAMESPACEREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._UPDATENAMESPACERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeprecateNamespace',
    full_name='workflowservice.WorkflowService.DeprecateNamespace',
    index=4,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._DEPRECATENAMESPACEREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._DEPRECATENAMESPACERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='StartWorkflowExecution',
    full_name='workflowservice.WorkflowService.StartWorkflowExecution',
    index=5,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._STARTWORKFLOWEXECUTIONREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._STARTWORKFLOWEXECUTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetWorkflowExecutionHistory',
    full_name='workflowservice.WorkflowService.GetWorkflowExecutionHistory',
    index=6,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._GETWORKFLOWEXECUTIONHISTORYREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._GETWORKFLOWEXECUTIONHISTORYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PollForDecisionTask',
    full_name='workflowservice.WorkflowService.PollForDecisionTask',
    index=7,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._POLLFORDECISIONTASKREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._POLLFORDECISIONTASKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RespondDecisionTaskCompleted',
    full_name='workflowservice.WorkflowService.RespondDecisionTaskCompleted',
    index=8,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDDECISIONTASKCOMPLETEDREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDDECISIONTASKCOMPLETEDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RespondDecisionTaskFailed',
    full_name='workflowservice.WorkflowService.RespondDecisionTaskFailed',
    index=9,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDDECISIONTASKFAILEDREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDDECISIONTASKFAILEDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PollForActivityTask',
    full_name='workflowservice.WorkflowService.PollForActivityTask',
    index=10,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._POLLFORACTIVITYTASKREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._POLLFORACTIVITYTASKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RecordActivityTaskHeartbeat',
    full_name='workflowservice.WorkflowService.RecordActivityTaskHeartbeat',
    index=11,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RECORDACTIVITYTASKHEARTBEATREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RECORDACTIVITYTASKHEARTBEATRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RecordActivityTaskHeartbeatById',
    full_name='workflowservice.WorkflowService.RecordActivityTaskHeartbeatById',
    index=12,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RECORDACTIVITYTASKHEARTBEATBYIDREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RECORDACTIVITYTASKHEARTBEATBYIDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RespondActivityTaskCompleted',
    full_name='workflowservice.WorkflowService.RespondActivityTaskCompleted',
    index=13,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKCOMPLETEDREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKCOMPLETEDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RespondActivityTaskCompletedById',
    full_name='workflowservice.WorkflowService.RespondActivityTaskCompletedById',
    index=14,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKCOMPLETEDBYIDREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKCOMPLETEDBYIDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RespondActivityTaskFailed',
    full_name='workflowservice.WorkflowService.RespondActivityTaskFailed',
    index=15,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKFAILEDREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKFAILEDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RespondActivityTaskFailedById',
    full_name='workflowservice.WorkflowService.RespondActivityTaskFailedById',
    index=16,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKFAILEDBYIDREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKFAILEDBYIDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RespondActivityTaskCanceled',
    full_name='workflowservice.WorkflowService.RespondActivityTaskCanceled',
    index=17,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKCANCELEDREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKCANCELEDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RespondActivityTaskCanceledById',
    full_name='workflowservice.WorkflowService.RespondActivityTaskCanceledById',
    index=18,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKCANCELEDBYIDREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDACTIVITYTASKCANCELEDBYIDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RequestCancelWorkflowExecution',
    full_name='workflowservice.WorkflowService.RequestCancelWorkflowExecution',
    index=19,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._REQUESTCANCELWORKFLOWEXECUTIONREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._REQUESTCANCELWORKFLOWEXECUTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SignalWorkflowExecution',
    full_name='workflowservice.WorkflowService.SignalWorkflowExecution',
    index=20,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._SIGNALWORKFLOWEXECUTIONREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._SIGNALWORKFLOWEXECUTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SignalWithStartWorkflowExecution',
    full_name='workflowservice.WorkflowService.SignalWithStartWorkflowExecution',
    index=21,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._SIGNALWITHSTARTWORKFLOWEXECUTIONREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._SIGNALWITHSTARTWORKFLOWEXECUTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ResetWorkflowExecution',
    full_name='workflowservice.WorkflowService.ResetWorkflowExecution',
    index=22,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESETWORKFLOWEXECUTIONREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESETWORKFLOWEXECUTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TerminateWorkflowExecution',
    full_name='workflowservice.WorkflowService.TerminateWorkflowExecution',
    index=23,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._TERMINATEWORKFLOWEXECUTIONREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._TERMINATEWORKFLOWEXECUTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListOpenWorkflowExecutions',
    full_name='workflowservice.WorkflowService.ListOpenWorkflowExecutions',
    index=24,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTOPENWORKFLOWEXECUTIONSREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTOPENWORKFLOWEXECUTIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListClosedWorkflowExecutions',
    full_name='workflowservice.WorkflowService.ListClosedWorkflowExecutions',
    index=25,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTCLOSEDWORKFLOWEXECUTIONSREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTCLOSEDWORKFLOWEXECUTIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListWorkflowExecutions',
    full_name='workflowservice.WorkflowService.ListWorkflowExecutions',
    index=26,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTWORKFLOWEXECUTIONSREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTWORKFLOWEXECUTIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListArchivedWorkflowExecutions',
    full_name='workflowservice.WorkflowService.ListArchivedWorkflowExecutions',
    index=27,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTARCHIVEDWORKFLOWEXECUTIONSREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTARCHIVEDWORKFLOWEXECUTIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ScanWorkflowExecutions',
    full_name='workflowservice.WorkflowService.ScanWorkflowExecutions',
    index=28,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._SCANWORKFLOWEXECUTIONSREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._SCANWORKFLOWEXECUTIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CountWorkflowExecutions',
    full_name='workflowservice.WorkflowService.CountWorkflowExecutions',
    index=29,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._COUNTWORKFLOWEXECUTIONSREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._COUNTWORKFLOWEXECUTIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSearchAttributes',
    full_name='workflowservice.WorkflowService.GetSearchAttributes',
    index=30,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._GETSEARCHATTRIBUTESREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._GETSEARCHATTRIBUTESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RespondQueryTaskCompleted',
    full_name='workflowservice.WorkflowService.RespondQueryTaskCompleted',
    index=31,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDQUERYTASKCOMPLETEDREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESPONDQUERYTASKCOMPLETEDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ResetStickyTaskList',
    full_name='workflowservice.WorkflowService.ResetStickyTaskList',
    index=32,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESETSTICKYTASKLISTREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._RESETSTICKYTASKLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='QueryWorkflow',
    full_name='workflowservice.WorkflowService.QueryWorkflow',
    index=33,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._QUERYWORKFLOWREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._QUERYWORKFLOWRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeWorkflowExecution',
    full_name='workflowservice.WorkflowService.DescribeWorkflowExecution',
    index=34,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._DESCRIBEWORKFLOWEXECUTIONREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._DESCRIBEWORKFLOWEXECUTIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DescribeTaskList',
    full_name='workflowservice.WorkflowService.DescribeTaskList',
    index=35,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._DESCRIBETASKLISTREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._DESCRIBETASKLISTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetClusterInfo',
    full_name='workflowservice.WorkflowService.GetClusterInfo',
    index=36,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._GETCLUSTERINFOREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._GETCLUSTERINFORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListTaskListPartitions',
    full_name='workflowservice.WorkflowService.ListTaskListPartitions',
    index=37,
    containing_service=None,
    input_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTTASKLISTPARTITIONSREQUEST,
    output_type=temporal_dot_proto_dot_workflowservice_dot_request__response__pb2._LISTTASKLISTPARTITIONSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKFLOWSERVICE)

DESCRIPTOR.services_by_name['WorkflowService'] = _WORKFLOWSERVICE

# @@protoc_insertion_point(module_scope)
