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
  package='DCnetPackage',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x64\x63_net.proto\x12\x0c\x44\x43netPackage\"$\n\x0b\x41\x63knowlegde\x12\x15\n\rMessageStatus\x18\x01 \x01(\x05\"\x92\x01\n\x06\x44\x43_net\x12\x19\n\x11\x64\x63_net_identifier\x18\x01 \x01(\x05\x12\x19\n\x11\x63lient_identifier\x18\x02 \x01(\x05\x12\x17\n\x0ftransmissionBit\x18\x03 \x01(\x05\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x14\n\x0cnotification\x18\x05 \x01(\x05\x12\x10\n\x08localSum\x18\x06 \x01(\x05\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"F\n\x06Secret\x12\x19\n\x11\x63lient_identifier\x18\x01 \x01(\x05\x12\x0e\n\x06secret\x18\x02 \x01(\x05\x12\x11\n\tneighboor\x18\x03 \x01(\x05\"$\n\x0c\x44iffieHelman\x12\t\n\x01p\x18\x01 \x01(\x05\x12\t\n\x01g\x18\x02 \x01(\x05\"F\n\x04Seed\x12\x10\n\x08PRNGSeed\x18\x01 \x01(\x05\x12\x19\n\x11\x63lient_identifier\x18\x02 \x01(\x05\x12\x11\n\tneighboor\x18\x03 \x01(\x05\"\x07\n\x05\x45mpty2\xdb\x01\n\x07Greeter\x12\x42\n\x08SayHello\x12\x1a.DCnetPackage.HelloRequest\x1a\x18.DCnetPackage.HelloReply\"\x00\x12G\n\rSayHelloAgain\x12\x1a.DCnetPackage.HelloRequest\x1a\x18.DCnetPackage.HelloReply\"\x00\x12\x43\n\x0b\x43lientHello\x12\x18.DCnetPackage.HelloReply\x1a\x18.DCnetPackage.HelloReply\"\x00\x32\x9b\x03\n\x08\x44\x43_round\x12\x41\n\x0cSendLocalSum\x12\x14.DCnetPackage.DC_net\x1a\x19.DCnetPackage.Acknowlegde\"\x00\x12@\n\x10\x61\x64\x64\x43lientToDCnet\x12\x14.DCnetPackage.DC_net\x1a\x14.DCnetPackage.DC_net\"\x00\x12@\n\x10\x63onnectDCClients\x12\x14.DCnetPackage.DC_net\x1a\x14.DCnetPackage.DC_net\"\x00\x12\x43\n\x13\x45xchangeSecretForDH\x12\x14.DCnetPackage.Secret\x1a\x14.DCnetPackage.Secret\"\x00\x12\x45\n\x10getDiffieHellman\x12\x13.DCnetPackage.Empty\x1a\x1a.DCnetPackage.DiffieHelman\"\x00\x12<\n\x10\x45xchangePRNGSeed\x12\x12.DCnetPackage.Seed\x1a\x12.DCnetPackage.Seed\"\x00'
)




_ACKNOWLEGDE = _descriptor.Descriptor(
  name='Acknowlegde',
  full_name='DCnetPackage.Acknowlegde',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='MessageStatus', full_name='DCnetPackage.Acknowlegde.MessageStatus', index=0,
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
  serialized_start=30,
  serialized_end=66,
)


_DC_NET = _descriptor.Descriptor(
  name='DC_net',
  full_name='DCnetPackage.DC_net',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dc_net_identifier', full_name='DCnetPackage.DC_net.dc_net_identifier', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_identifier', full_name='DCnetPackage.DC_net.client_identifier', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transmissionBit', full_name='DCnetPackage.DC_net.transmissionBit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='DCnetPackage.DC_net.timestamp', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification', full_name='DCnetPackage.DC_net.notification', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localSum', full_name='DCnetPackage.DC_net.localSum', index=5,
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
  serialized_start=69,
  serialized_end=215,
)


_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='DCnetPackage.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='DCnetPackage.HelloRequest.name', index=0,
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
  serialized_start=217,
  serialized_end=245,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='DCnetPackage.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='DCnetPackage.HelloReply.message', index=0,
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
  serialized_start=247,
  serialized_end=276,
)


_SECRET = _descriptor.Descriptor(
  name='Secret',
  full_name='DCnetPackage.Secret',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_identifier', full_name='DCnetPackage.Secret.client_identifier', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret', full_name='DCnetPackage.Secret.secret', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='neighboor', full_name='DCnetPackage.Secret.neighboor', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=278,
  serialized_end=348,
)


_DIFFIEHELMAN = _descriptor.Descriptor(
  name='DiffieHelman',
  full_name='DCnetPackage.DiffieHelman',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='p', full_name='DCnetPackage.DiffieHelman.p', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='g', full_name='DCnetPackage.DiffieHelman.g', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=350,
  serialized_end=386,
)


_SEED = _descriptor.Descriptor(
  name='Seed',
  full_name='DCnetPackage.Seed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='PRNGSeed', full_name='DCnetPackage.Seed.PRNGSeed', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_identifier', full_name='DCnetPackage.Seed.client_identifier', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='neighboor', full_name='DCnetPackage.Seed.neighboor', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=388,
  serialized_end=458,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='DCnetPackage.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=460,
  serialized_end=467,
)

DESCRIPTOR.message_types_by_name['Acknowlegde'] = _ACKNOWLEGDE
DESCRIPTOR.message_types_by_name['DC_net'] = _DC_NET
DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['Secret'] = _SECRET
DESCRIPTOR.message_types_by_name['DiffieHelman'] = _DIFFIEHELMAN
DESCRIPTOR.message_types_by_name['Seed'] = _SEED
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Acknowlegde = _reflection.GeneratedProtocolMessageType('Acknowlegde', (_message.Message,), {
  'DESCRIPTOR' : _ACKNOWLEGDE,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnetPackage.Acknowlegde)
  })
_sym_db.RegisterMessage(Acknowlegde)

DC_net = _reflection.GeneratedProtocolMessageType('DC_net', (_message.Message,), {
  'DESCRIPTOR' : _DC_NET,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnetPackage.DC_net)
  })
_sym_db.RegisterMessage(DC_net)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnetPackage.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnetPackage.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

Secret = _reflection.GeneratedProtocolMessageType('Secret', (_message.Message,), {
  'DESCRIPTOR' : _SECRET,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnetPackage.Secret)
  })
_sym_db.RegisterMessage(Secret)

DiffieHelman = _reflection.GeneratedProtocolMessageType('DiffieHelman', (_message.Message,), {
  'DESCRIPTOR' : _DIFFIEHELMAN,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnetPackage.DiffieHelman)
  })
_sym_db.RegisterMessage(DiffieHelman)

Seed = _reflection.GeneratedProtocolMessageType('Seed', (_message.Message,), {
  'DESCRIPTOR' : _SEED,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnetPackage.Seed)
  })
_sym_db.RegisterMessage(Seed)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'dc_net_pb2'
  # @@protoc_insertion_point(class_scope:DCnetPackage.Empty)
  })
_sym_db.RegisterMessage(Empty)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='DCnetPackage.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=470,
  serialized_end=689,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='DCnetPackage.Greeter.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SayHelloAgain',
    full_name='DCnetPackage.Greeter.SayHelloAgain',
    index=1,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ClientHello',
    full_name='DCnetPackage.Greeter.ClientHello',
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
  full_name='DCnetPackage.DC_round',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=692,
  serialized_end=1103,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendLocalSum',
    full_name='DCnetPackage.DC_round.SendLocalSum',
    index=0,
    containing_service=None,
    input_type=_DC_NET,
    output_type=_ACKNOWLEGDE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='addClientToDCnet',
    full_name='DCnetPackage.DC_round.addClientToDCnet',
    index=1,
    containing_service=None,
    input_type=_DC_NET,
    output_type=_DC_NET,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='connectDCClients',
    full_name='DCnetPackage.DC_round.connectDCClients',
    index=2,
    containing_service=None,
    input_type=_DC_NET,
    output_type=_DC_NET,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExchangeSecretForDH',
    full_name='DCnetPackage.DC_round.ExchangeSecretForDH',
    index=3,
    containing_service=None,
    input_type=_SECRET,
    output_type=_SECRET,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getDiffieHellman',
    full_name='DCnetPackage.DC_round.getDiffieHellman',
    index=4,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_DIFFIEHELMAN,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExchangePRNGSeed',
    full_name='DCnetPackage.DC_round.ExchangePRNGSeed',
    index=5,
    containing_service=None,
    input_type=_SEED,
    output_type=_SEED,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DC_ROUND)

DESCRIPTOR.services_by_name['DC_round'] = _DC_ROUND

# @@protoc_insertion_point(module_scope)
