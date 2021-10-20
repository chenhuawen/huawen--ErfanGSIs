# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apex_manifest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='apex_manifest.proto',
  package='apex.proto',
  syntax='proto3',
  serialized_options=b'\n\020com.android.apexB\006Protos',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x61pex_manifest.proto\x12\napex.proto\"\xac\x03\n\x0c\x41pexManifest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x03\x12\x16\n\x0epreInstallHook\x18\x03 \x01(\t\x12\x1b\n\x0fpostInstallHook\x18\x04 \x01(\tB\x02\x18\x01\x12\x13\n\x0bversionName\x18\x05 \x01(\t\x12\x0e\n\x06noCode\x18\x06 \x01(\x08\x12\x19\n\x11provideNativeLibs\x18\x07 \x03(\t\x12\x19\n\x11requireNativeLibs\x18\x08 \x03(\t\x12\x0f\n\x07jniLibs\x18\t \x03(\t\x12\x1d\n\x15requireSharedApexLibs\x18\n \x03(\t\x12\x1d\n\x15provideSharedApexLibs\x18\x0b \x01(\x08\x12\x46\n\rcapexMetadata\x18\x0c \x01(\x0b\x32/.apex.proto.ApexManifest.CompressedApexMetadata\x12 \n\x18supportsRebootlessUpdate\x18\r \x01(\x08\x1a\x34\n\x16\x43ompressedApexMetadata\x12\x1a\n\x12originalApexDigest\x18\x01 \x01(\tB\x1a\n\x10\x63om.android.apexB\x06Protosb\x06proto3'
)




_APEXMANIFEST_COMPRESSEDAPEXMETADATA = _descriptor.Descriptor(
  name='CompressedApexMetadata',
  full_name='apex.proto.ApexManifest.CompressedApexMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='originalApexDigest', full_name='apex.proto.ApexManifest.CompressedApexMetadata.originalApexDigest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=412,
  serialized_end=464,
)

_APEXMANIFEST = _descriptor.Descriptor(
  name='ApexManifest',
  full_name='apex.proto.ApexManifest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='apex.proto.ApexManifest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='apex.proto.ApexManifest.version', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preInstallHook', full_name='apex.proto.ApexManifest.preInstallHook', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='postInstallHook', full_name='apex.proto.ApexManifest.postInstallHook', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='apex.proto.ApexManifest.versionName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='noCode', full_name='apex.proto.ApexManifest.noCode', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provideNativeLibs', full_name='apex.proto.ApexManifest.provideNativeLibs', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requireNativeLibs', full_name='apex.proto.ApexManifest.requireNativeLibs', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='jniLibs', full_name='apex.proto.ApexManifest.jniLibs', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requireSharedApexLibs', full_name='apex.proto.ApexManifest.requireSharedApexLibs', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provideSharedApexLibs', full_name='apex.proto.ApexManifest.provideSharedApexLibs', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='capexMetadata', full_name='apex.proto.ApexManifest.capexMetadata', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='supportsRebootlessUpdate', full_name='apex.proto.ApexManifest.supportsRebootlessUpdate', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_APEXMANIFEST_COMPRESSEDAPEXMETADATA, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=464,
)

_APEXMANIFEST_COMPRESSEDAPEXMETADATA.containing_type = _APEXMANIFEST
_APEXMANIFEST.fields_by_name['capexMetadata'].message_type = _APEXMANIFEST_COMPRESSEDAPEXMETADATA
DESCRIPTOR.message_types_by_name['ApexManifest'] = _APEXMANIFEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApexManifest = _reflection.GeneratedProtocolMessageType('ApexManifest', (_message.Message,), {

  'CompressedApexMetadata' : _reflection.GeneratedProtocolMessageType('CompressedApexMetadata', (_message.Message,), {
    'DESCRIPTOR' : _APEXMANIFEST_COMPRESSEDAPEXMETADATA,
    '__module__' : 'apex_manifest_pb2'
    # @@protoc_insertion_point(class_scope:apex.proto.ApexManifest.CompressedApexMetadata)
    })
  ,
  'DESCRIPTOR' : _APEXMANIFEST,
  '__module__' : 'apex_manifest_pb2'
  # @@protoc_insertion_point(class_scope:apex.proto.ApexManifest)
  })
_sym_db.RegisterMessage(ApexManifest)
_sym_db.RegisterMessage(ApexManifest.CompressedApexMetadata)


DESCRIPTOR._options = None
_APEXMANIFEST.fields_by_name['postInstallHook']._options = None
# @@protoc_insertion_point(module_scope)
