# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from novatel_pkg/RANGE.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import novatel_pkg.msg

class RANGE(genpy.Message):
  _md5sum = "ec2ee37b6f94d56550d64b98028bbcfe"
  _type = "novatel_pkg/RANGE"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# RANGE ID: 43
# Put RANGEB for binary when connected with NovAtel Application Suite
# Author: Brandon Medellin
# Date: 2/1/2023

novatel_pkg/CommonLongHeader header

# Total number of observations for the log uniquely identified by the PRN
uint32 num_obs

# ------------------------------------------------------------ 

# Satellite PRN number of range measurement
uint16 prn

# GLONASS Frequency + 7
uint16 glofreq

# Psuedorange measurement (m)
float64 psr

# Psuedorange measurement standard deviation (m)
float32 psr_sig

# Carrier phase, in cycles (accumulated Doppler range)
float64 adr

# Estimated carrier phase standard deviation (cycles)
float32 adr_sig

# Instantaneous carrier Doppler frequency (Hz)
float32 dopp

# Carrier to noise density ratio
float32 c_no

# Number of seconds of continuous tracking (no cycles slipping)
float32 locktime

# Tracking status 
uint32 ch_tr_status

# ------------------------------------------------------------


================================================================================
MSG: novatel_pkg/CommonLongHeader
# Long Binary Header NovAtel
# Author: Brandon Medellin
# Date: 2/1/2023

# Length of the header
uint8 head_length

# Message ID of the log being output
uint16 id

# Measurement source, format, response bit.
uint8 msg_type

# Port address
uint8 port_addr

# Message length not including header (25 bytes) nor CRC (4 bytes)
uint16 length

# Used for multiple related logs. It is a number that counts down from N-1 to 0 where N is the number of related logs ...
uint16 sequence

# Time the processor is idle, calculated once per second - more in documentation
uint8 idle_time

# Indicates the quality of the gps reference time
uint8 time_status

# GNSS week number
uint16 gnss_week

# GNSS Miliseconds from beginning of GNSS week
int32 gnss_mili

# Reserved for internal use
uint16 reserved

# A value (0-65535) representing the receiver software build number
uint16 software_version

"""
  __slots__ = ['header','num_obs','prn','glofreq','psr','psr_sig','adr','adr_sig','dopp','c_no','locktime','ch_tr_status']
  _slot_types = ['novatel_pkg/CommonLongHeader','uint32','uint16','uint16','float64','float32','float64','float32','float32','float32','float32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,num_obs,prn,glofreq,psr,psr_sig,adr,adr_sig,dopp,c_no,locktime,ch_tr_status

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RANGE, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = novatel_pkg.msg.CommonLongHeader()
      if self.num_obs is None:
        self.num_obs = 0
      if self.prn is None:
        self.prn = 0
      if self.glofreq is None:
        self.glofreq = 0
      if self.psr is None:
        self.psr = 0.
      if self.psr_sig is None:
        self.psr_sig = 0.
      if self.adr is None:
        self.adr = 0.
      if self.adr_sig is None:
        self.adr_sig = 0.
      if self.dopp is None:
        self.dopp = 0.
      if self.c_no is None:
        self.c_no = 0.
      if self.locktime is None:
        self.locktime = 0.
      if self.ch_tr_status is None:
        self.ch_tr_status = 0
    else:
      self.header = novatel_pkg.msg.CommonLongHeader()
      self.num_obs = 0
      self.prn = 0
      self.glofreq = 0
      self.psr = 0.
      self.psr_sig = 0.
      self.adr = 0.
      self.adr_sig = 0.
      self.dopp = 0.
      self.c_no = 0.
      self.locktime = 0.
      self.ch_tr_status = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_BH2B2H2BHi2HI2Hdfd4fI().pack(_x.header.head_length, _x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gnss_week, _x.header.gnss_mili, _x.header.reserved, _x.header.software_version, _x.num_obs, _x.prn, _x.glofreq, _x.psr, _x.psr_sig, _x.adr, _x.adr_sig, _x.dopp, _x.c_no, _x.locktime, _x.ch_tr_status))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = novatel_pkg.msg.CommonLongHeader()
      end = 0
      _x = self
      start = end
      end += 69
      (_x.header.head_length, _x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gnss_week, _x.header.gnss_mili, _x.header.reserved, _x.header.software_version, _x.num_obs, _x.prn, _x.glofreq, _x.psr, _x.psr_sig, _x.adr, _x.adr_sig, _x.dopp, _x.c_no, _x.locktime, _x.ch_tr_status,) = _get_struct_BH2B2H2BHi2HI2Hdfd4fI().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_BH2B2H2BHi2HI2Hdfd4fI().pack(_x.header.head_length, _x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gnss_week, _x.header.gnss_mili, _x.header.reserved, _x.header.software_version, _x.num_obs, _x.prn, _x.glofreq, _x.psr, _x.psr_sig, _x.adr, _x.adr_sig, _x.dopp, _x.c_no, _x.locktime, _x.ch_tr_status))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = novatel_pkg.msg.CommonLongHeader()
      end = 0
      _x = self
      start = end
      end += 69
      (_x.header.head_length, _x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gnss_week, _x.header.gnss_mili, _x.header.reserved, _x.header.software_version, _x.num_obs, _x.prn, _x.glofreq, _x.psr, _x.psr_sig, _x.adr, _x.adr_sig, _x.dopp, _x.c_no, _x.locktime, _x.ch_tr_status,) = _get_struct_BH2B2H2BHi2HI2Hdfd4fI().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_BH2B2H2BHi2HI2Hdfd4fI = None
def _get_struct_BH2B2H2BHi2HI2Hdfd4fI():
    global _struct_BH2B2H2BHi2HI2Hdfd4fI
    if _struct_BH2B2H2BHi2HI2Hdfd4fI is None:
        _struct_BH2B2H2BHi2HI2Hdfd4fI = struct.Struct("<BH2B2H2BHi2HI2Hdfd4fI")
    return _struct_BH2B2H2BHi2HI2Hdfd4fI
