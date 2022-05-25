# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: asearch.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rasearch.proto\"o\n\x0bRankRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12$\n\x04\x64ocs\x18\x02 \x03(\x0b\x32\x16.RankRequest.DocsEntry\x1a+\n\tDocsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"h\n\x0cRankResponse\x12)\n\x06result\x18\x01 \x03(\x0b\x32\x19.RankResponse.ResultEntry\x1a-\n\x0bResultEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"(\n\nSimRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\x0b\n\x03\x64oc\x18\x02 \x01(\t\" \n\x0bSimResponse\x12\x11\n\tsim_score\x18\x01 \x01(\x01\"\x1d\n\x0c\x45mbedRequest\x12\r\n\x05texts\x18\x01 \x03(\t\"/\n\rEmbedResponse\x12\x1e\n\nembeddings\x18\x01 \x03(\x0b\x32\n.Embedding\"\x1e\n\tEmbedding\x12\x11\n\tembedding\x18\x01 \x03(\x01\x32\x9b\x01\n\x11\x41SearchSimilarity\x12\'\n\x06ReRank\x12\x0c.RankRequest\x1a\r.RankResponse\"\x00\x12,\n\rTextSimilarty\x12\x0b.SimRequest\x1a\x0c.SimResponse\"\x00\x12/\n\x0cGetEmbedding\x12\r.EmbedRequest\x1a\x0e.EmbedResponse\"\x00\x62\x06proto3')



_RANKREQUEST = DESCRIPTOR.message_types_by_name['RankRequest']
_RANKREQUEST_DOCSENTRY = _RANKREQUEST.nested_types_by_name['DocsEntry']
_RANKRESPONSE = DESCRIPTOR.message_types_by_name['RankResponse']
_RANKRESPONSE_RESULTENTRY = _RANKRESPONSE.nested_types_by_name['ResultEntry']
_SIMREQUEST = DESCRIPTOR.message_types_by_name['SimRequest']
_SIMRESPONSE = DESCRIPTOR.message_types_by_name['SimResponse']
_EMBEDREQUEST = DESCRIPTOR.message_types_by_name['EmbedRequest']
_EMBEDRESPONSE = DESCRIPTOR.message_types_by_name['EmbedResponse']
_EMBEDDING = DESCRIPTOR.message_types_by_name['Embedding']
RankRequest = _reflection.GeneratedProtocolMessageType('RankRequest', (_message.Message,), {

  'DocsEntry' : _reflection.GeneratedProtocolMessageType('DocsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RANKREQUEST_DOCSENTRY,
    '__module__' : 'asearch_pb2'
    # @@protoc_insertion_point(class_scope:RankRequest.DocsEntry)
    })
  ,
  'DESCRIPTOR' : _RANKREQUEST,
  '__module__' : 'asearch_pb2'
  # @@protoc_insertion_point(class_scope:RankRequest)
  })
_sym_db.RegisterMessage(RankRequest)
_sym_db.RegisterMessage(RankRequest.DocsEntry)

RankResponse = _reflection.GeneratedProtocolMessageType('RankResponse', (_message.Message,), {

  'ResultEntry' : _reflection.GeneratedProtocolMessageType('ResultEntry', (_message.Message,), {
    'DESCRIPTOR' : _RANKRESPONSE_RESULTENTRY,
    '__module__' : 'asearch_pb2'
    # @@protoc_insertion_point(class_scope:RankResponse.ResultEntry)
    })
  ,
  'DESCRIPTOR' : _RANKRESPONSE,
  '__module__' : 'asearch_pb2'
  # @@protoc_insertion_point(class_scope:RankResponse)
  })
_sym_db.RegisterMessage(RankResponse)
_sym_db.RegisterMessage(RankResponse.ResultEntry)

SimRequest = _reflection.GeneratedProtocolMessageType('SimRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIMREQUEST,
  '__module__' : 'asearch_pb2'
  # @@protoc_insertion_point(class_scope:SimRequest)
  })
_sym_db.RegisterMessage(SimRequest)

SimResponse = _reflection.GeneratedProtocolMessageType('SimResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIMRESPONSE,
  '__module__' : 'asearch_pb2'
  # @@protoc_insertion_point(class_scope:SimResponse)
  })
_sym_db.RegisterMessage(SimResponse)

EmbedRequest = _reflection.GeneratedProtocolMessageType('EmbedRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMBEDREQUEST,
  '__module__' : 'asearch_pb2'
  # @@protoc_insertion_point(class_scope:EmbedRequest)
  })
_sym_db.RegisterMessage(EmbedRequest)

EmbedResponse = _reflection.GeneratedProtocolMessageType('EmbedResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMBEDRESPONSE,
  '__module__' : 'asearch_pb2'
  # @@protoc_insertion_point(class_scope:EmbedResponse)
  })
_sym_db.RegisterMessage(EmbedResponse)

Embedding = _reflection.GeneratedProtocolMessageType('Embedding', (_message.Message,), {
  'DESCRIPTOR' : _EMBEDDING,
  '__module__' : 'asearch_pb2'
  # @@protoc_insertion_point(class_scope:Embedding)
  })
_sym_db.RegisterMessage(Embedding)

_ASEARCHSIMILARITY = DESCRIPTOR.services_by_name['ASearchSimilarity']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RANKREQUEST_DOCSENTRY._options = None
  _RANKREQUEST_DOCSENTRY._serialized_options = b'8\001'
  _RANKRESPONSE_RESULTENTRY._options = None
  _RANKRESPONSE_RESULTENTRY._serialized_options = b'8\001'
  _RANKREQUEST._serialized_start=17
  _RANKREQUEST._serialized_end=128
  _RANKREQUEST_DOCSENTRY._serialized_start=85
  _RANKREQUEST_DOCSENTRY._serialized_end=128
  _RANKRESPONSE._serialized_start=130
  _RANKRESPONSE._serialized_end=234
  _RANKRESPONSE_RESULTENTRY._serialized_start=189
  _RANKRESPONSE_RESULTENTRY._serialized_end=234
  _SIMREQUEST._serialized_start=236
  _SIMREQUEST._serialized_end=276
  _SIMRESPONSE._serialized_start=278
  _SIMRESPONSE._serialized_end=310
  _EMBEDREQUEST._serialized_start=312
  _EMBEDREQUEST._serialized_end=341
  _EMBEDRESPONSE._serialized_start=343
  _EMBEDRESPONSE._serialized_end=390
  _EMBEDDING._serialized_start=392
  _EMBEDDING._serialized_end=422
  _ASEARCHSIMILARITY._serialized_start=425
  _ASEARCHSIMILARITY._serialized_end=580
# @@protoc_insertion_point(module_scope)
