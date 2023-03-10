# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from novatel_pkg/BESTPOS.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import novatel_pkg.msg

class BESTPOS(genpy.Message):
  _md5sum = "9f8dc9710a4cb96033fd5b5ef2cdb331"
  _type = "novatel_pkg/BESTPOS"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# INSPVAS Message ID: 508
# Author: Brandon Medellin
# Date: 2/10/2023

novatel_pkg/CommonLongHeader header

# Solution Status 
uint32 sol_stat

# Position type
uint32 pos_type

# Latitude 
float64 lat

# Longitude
float64 lon

# Height above mean sea level (metres)
float64 hgt

# undulation
float32 undulation

# Datum ID Number 
uint32 datum_id

# Latitude statdard dev
float32 lat_std

# Longitude standard dev
float32 long_std

# Height standard dev 
float32 hgt_std

# Base station ID 
string stn_id

# Differential age in seconds
float32 diff_age

# Solution age in seconds
float32 sol_age

# Number of Satellites tracked 
uint8 num_sats

# Number of satellites used in solution 
uint8 num_sol_sats

# Number of satellites  with L1/E1/B1 signals used in solution
uint8 num_sol_l1_sats

# Number of satellites with multi-frequency signals used in solution
uint8 num_sol_multi_sats

# Reserved


# ext sol stat 


# Galileo and BeiDou sig mask 


# GPS and GLONASS sig mask

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
  __slots__ = ['header','sol_stat','pos_type','lat','lon','hgt','undulation','datum_id','lat_std','long_std','hgt_std','stn_id','diff_age','sol_age','num_sats','num_sol_sats','num_sol_l1_sats','num_sol_multi_sats']
  _slot_types = ['novatel_pkg/CommonLongHeader','uint32','uint32','float64','float64','float64','float32','uint32','float32','float32','float32','string','float32','float32','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,sol_stat,pos_type,lat,lon,hgt,undulation,datum_id,lat_std,long_std,hgt_std,stn_id,diff_age,sol_age,num_sats,num_sol_sats,num_sol_l1_sats,num_sol_multi_sats

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BESTPOS, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = novatel_pkg.msg.CommonLongHeader()
      if self.sol_stat is None:
        self.sol_stat = 0
      if self.pos_type is None:
        self.pos_type = 0
      if self.lat is None:
        self.lat = 0.
      if self.lon is None:
        self.lon = 0.
      if self.hgt is None:
        self.hgt = 0.
      if self.undulation is None:
        self.undulation = 0.
      if self.datum_id is None:
        self.datum_id = 0
      if self.lat_std is None:
        self.lat_std = 0.
      if self.long_std is None:
        self.long_std = 0.
      if self.hgt_std is None:
        self.hgt_std = 0.
      if self.stn_id is None:
        self.stn_id = ''
      if self.diff_age is None:
        self.diff_age = 0.
      if self.sol_age is None:
        self.sol_age = 0.
      if self.num_sats is None:
        self.num_sats = 0
      if self.num_sol_sats is None:
        self.num_sol_sats = 0
      if self.num_sol_l1_sats is None:
        self.num_sol_l1_sats = 0
      if self.num_sol_multi_sats is None:
        self.num_sol_multi_sats = 0
    else:
      self.header = novatel_pkg.msg.CommonLongHeader()
      self.sol_stat = 0
      self.pos_type = 0
      self.lat = 0.
      self.lon = 0.
      self.hgt = 0.
      self.undulation = 0.
      self.datum_id = 0
      self.lat_std = 0.
      self.long_std = 0.
      self.hgt_std = 0.
      self.stn_id = ''
      self.diff_age = 0.
      self.sol_age = 0.
      self.num_sats = 0
      self.num_sol_sats = 0
      self.num_sol_l1_sats = 0
      self.num_sol_multi_sats = 0

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
      buff.write(_get_struct_BH2B2H2BHi2H2I3dfI3f().pack(_x.header.head_length, _x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gnss_week, _x.header.gnss_mili, _x.header.reserved, _x.header.software_version, _x.sol_stat, _x.pos_type, _x.lat, _x.lon, _x.hgt, _x.undulation, _x.datum_id, _x.lat_std, _x.long_std, _x.hgt_std))
      _x = self.stn_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2f4B().pack(_x.diff_age, _x.sol_age, _x.num_sats, _x.num_sol_sats, _x.num_sol_l1_sats, _x.num_sol_multi_sats))
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
      end += 73
      (_x.header.head_length, _x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gnss_week, _x.header.gnss_mili, _x.header.reserved, _x.header.software_version, _x.sol_stat, _x.pos_type, _x.lat, _x.lon, _x.hgt, _x.undulation, _x.datum_id, _x.lat_std, _x.long_std, _x.hgt_std,) = _get_struct_BH2B2H2BHi2H2I3dfI3f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.stn_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.stn_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.diff_age, _x.sol_age, _x.num_sats, _x.num_sol_sats, _x.num_sol_l1_sats, _x.num_sol_multi_sats,) = _get_struct_2f4B().unpack(str[start:end])
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
      buff.write(_get_struct_BH2B2H2BHi2H2I3dfI3f().pack(_x.header.head_length, _x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gnss_week, _x.header.gnss_mili, _x.header.reserved, _x.header.software_version, _x.sol_stat, _x.pos_type, _x.lat, _x.lon, _x.hgt, _x.undulation, _x.datum_id, _x.lat_std, _x.long_std, _x.hgt_std))
      _x = self.stn_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2f4B().pack(_x.diff_age, _x.sol_age, _x.num_sats, _x.num_sol_sats, _x.num_sol_l1_sats, _x.num_sol_multi_sats))
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
      end += 73
      (_x.header.head_length, _x.header.id, _x.header.msg_type, _x.header.port_addr, _x.header.length, _x.header.sequence, _x.header.idle_time, _x.header.time_status, _x.header.gnss_week, _x.header.gnss_mili, _x.header.reserved, _x.header.software_version, _x.sol_stat, _x.pos_type, _x.lat, _x.lon, _x.hgt, _x.undulation, _x.datum_id, _x.lat_std, _x.long_std, _x.hgt_std,) = _get_struct_BH2B2H2BHi2H2I3dfI3f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.stn_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.stn_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.diff_age, _x.sol_age, _x.num_sats, _x.num_sol_sats, _x.num_sol_l1_sats, _x.num_sol_multi_sats,) = _get_struct_2f4B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2f4B = None
def _get_struct_2f4B():
    global _struct_2f4B
    if _struct_2f4B is None:
        _struct_2f4B = struct.Struct("<2f4B")
    return _struct_2f4B
_struct_BH2B2H2BHi2H2I3dfI3f = None
def _get_struct_BH2B2H2BHi2H2I3dfI3f():
    global _struct_BH2B2H2BHi2H2I3dfI3f
    if _struct_BH2B2H2BHi2H2I3dfI3f is None:
        _struct_BH2B2H2BHi2H2I3dfI3f = struct.Struct("<BH2B2H2BHi2H2I3dfI3f")
    return _struct_BH2B2H2BHi2H2I3dfI3f
