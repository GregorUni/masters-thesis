# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dc_net.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dc_net.proto',
  package='DCnet',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x64\x63_net.proto\x12\x05\x44\x43net\"$\n\x0b\x41\x63knowlegde\x12\x15\n\rMessageStatus\x18\x01 \x01(\x05\"\x92\x01\n\x06\x44\x43_net\x12\x19\n\x11\x64\x63_net_identifier\x18\x01 \x01(\x05\x12\x19\n\x11\x63lient_identifier\x18\x02 \x01(\x05\x12\x17\n\x0ftransmissionBit\x18\x03 \x01(\x05\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x14\n\x0cnotification\x18\x05 \x01(\x05\x12\x10\n\x08localSum\x18\x06 \x01(\x05\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xb1\x01\n\x07Greeter\x12\x34\n\x08SayHello\x12\x13.DCnet.HelloRequest\x1a\x11.DCnet.HelloReply\"\x00\x12\x39\n\rSayHelloAgain\x12\x13.DCnet.HelloRequest\x1a\x11.DCnet.HelloReply\"\x00\x12\x35\n\x0b\x43lientHello\x12\x11.DCnet.HelloReply\x1a\x11.DCnet.HelloReply\"\x00\x32s\n\x08\x44\x43_round\x12\x33\n\x0cSendLocalSum\x12\r.DCnet.DC_net\x1a\x12.DCnet.Acknowlegde\"\x00\x12\x32\n\x10\x61\x64\x64\x43lientToDCnet\x12\r.DCnet.DC_net\x1a\r.DCnet.DC_net\"\x00'
)




_ACKNOWLEGDE = _descriptor.Descriptor(
  name='Acknowlegde',
  full_name='DCnet.Acknowlegde',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='MessageStatus', full_name='DCnet.Acknowlegde.MessageStatus', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=59,
)


_DC_NET = _descriptor.Descriptor(
  name='DC_net',
  full_name='DCnet.DC_net',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dc_net_identifier', full_name='DCnet.DC_net.dc_net_identifier', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_identifier', full_name='DCnet.DC_net.client_identifier', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transmissionBit', full_name='DCnet.DC_net.transmissionBit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='DCnet.DC_net.timestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification', full_name='DCnet.DC_net.notification', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localSum', full_name='DCnet.DC_net.localSum', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=208,
)


_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='DCnet.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DCnet.HelloRequest.name', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=238,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='DCnet.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='DCnet.HelloReply.message', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=269,
)

DESCRIPTOR.message_types_by_name['Acknowlegde'] = _ACKNOWLEGDE
DESCRIPTOR.message_types_by_name['DC_net'] = _DC_NET
DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Acknowlegde = _reflection.GeneratedProtocolMessageType('Acknowlegde', (_message.Message,), {
  'DESCRIPTOR' : _ACKNOWLEGDE,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnet.Acknowlegde)
  })
_sym_db.RegisterMessage(Acknowlegde)

DC_net = _reflection.GeneratedProtocolMessageType('DC_net', (_message.Message,), {
  'DESCRIPTOR' : _DC_NET,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnet.DC_net)
  })
_sym_db.RegisterMessage(DC_net)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnet.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnet.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='DCnet.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=272,
  serialized_end=449,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='DCnet.Greeter.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloAgain',
    full_name='DCnet.Greeter.SayHelloAgain',
    index=1,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ClientHello',
    full_name='DCnet.Greeter.ClientHello',
    index=2,
    containing_service=None,
    input_type=_HELLOREPLY,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER


_DC_ROUND = _descriptor.ServiceDescriptor(
  name='DC_round',
  full_name='DCnet.DC_round',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=451,
  serialized_end=566,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendLocalSum',
    full_name='DCnet.DC_round.SendLocalSum',
    index=0,
    containing_service=None,
    input_type=_DC_NET,
    output_type=_ACKNOWLEGDE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='addClientToDCnet',
    full_name='DCnet.DC_round.addClientToDCnet',
    index=1,
    containing_service=None,
    input_type=_DC_NET,
    output_type=_DC_NET,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DC_ROUND)

DESCRIPTOR.services_by_name['DC_round'] = _DC_ROUND

# @@protoc_insertion_point(module_scope)