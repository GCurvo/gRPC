# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: auth.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'auth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04\x61uth\"2\n\x0fRegisterRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"?\n\x0c\x41uthResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\t\"!\n\x10ListUsersRequest\x12\r\n\x05token\x18\x01 \x01(\t\"\x15\n\x04User\x12\r\n\x05\x65mail\x18\x01 \x01(\t2\xa8\x01\n\x0b\x41uthService\x12\x35\n\x08Register\x12\x15.auth.RegisterRequest\x1a\x12.auth.AuthResponse\x12/\n\x05Login\x12\x12.auth.LoginRequest\x1a\x12.auth.AuthResponse\x12\x31\n\tListUsers\x12\x16.auth.ListUsersRequest\x1a\n.auth.User0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTERREQUEST']._serialized_start=20
  _globals['_REGISTERREQUEST']._serialized_end=70
  _globals['_LOGINREQUEST']._serialized_start=72
  _globals['_LOGINREQUEST']._serialized_end=119
  _globals['_AUTHRESPONSE']._serialized_start=121
  _globals['_AUTHRESPONSE']._serialized_end=184
  _globals['_LISTUSERSREQUEST']._serialized_start=186
  _globals['_LISTUSERSREQUEST']._serialized_end=219
  _globals['_USER']._serialized_start=221
  _globals['_USER']._serialized_end=242
  _globals['_AUTHSERVICE']._serialized_start=245
  _globals['_AUTHSERVICE']._serialized_end=413
# @@protoc_insertion_point(module_scope)