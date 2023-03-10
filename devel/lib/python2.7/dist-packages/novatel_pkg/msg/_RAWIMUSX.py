# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from novatel_pkg/RAWIMUSX.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import novatel_pkg.msg

class RAWIMUSX(genpy.Message):
  _md5sum = "d5a6c96f74c4727c7a4eea6a9a18c400"
  _type = "novatel_pkg/RAWIMUSX"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# INSPVAS Message ID: 508
# Author: Brandon Medellin
# Date: 2/1/2023

novatel_pkg/CommonShortHeader header

# IMU Info Bits 0 -> IMU Error Detected, 1 -> IMU data is encrypted, 2 to 7 -> Reserved
uint8 imu_info

# IMU Tyoe identifier
uint8 imu_type

# GNSS Week
uint16 gnss_week

# Seconds from GNSS week start
float64 gnss_seconds

# Status of the IMU
uint32 imu_status

# Linear Accelerations along Z, Y, X axes
geometry_msgs/Vector3 linear_acceleration

# Angular Velocity around Z, Y, X axes
geometry_msgs/Vector3 angular_velocity

================================================================================
MSG: novatel_pkg/CommonShortHeader
# Short Binary Header NovAtel OEM7
# Author: Brandon Medellin
# Date: 2/1/2023

# Message Length not including header (12 bytes) or CRC (4 byte)
uint8 length

# Message ID of the log being output.
uint16 id

# GNSS week number
uint16 gnss_week

# GNSS Miliseconds from beginning of GNSS week
int32 gnss_mili

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['header','imu_info','imu_type','gnss_week','gnss_seconds','imu_status','linear_acceleration','angular_velocity']
  _slot_types = ['novatel_pkg/CommonShortHeader','uint8','uint8','uint16','float64','uint32','geometry_msgs/Vector3','geometry_msgs/Vector3']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,imu_info,imu_type,gnss_week,gnss_seconds,imu_status,linear_acceleration,angular_velocity

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RAWIMUSX, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = novatel_pkg.msg.CommonShortHeader()
      if self.imu_info is None:
        self.imu_info = 0
      if self.imu_type is None:
        self.imu_type = 0
      if self.gnss_week is None:
        self.gnss_week = 0
      if self.gnss_seconds is None:
        self.gnss_seconds = 0.
      if self.imu_status is None:
        self.imu_status = 0
      if self.linear_acceleration is None:
        self.linear_acceleration = geometry_msgs.msg.Vector3()
      if self.angular_velocity is None:
        self.angular_velocity = geometry_msgs.msg.Vector3()
    else:
      self.header = novatel_pkg.msg.CommonShortHeader()
      self.imu_info = 0
      self.imu_type = 0
      self.gnss_week = 0
      self.gnss_seconds = 0.
      self.imu_status = 0
      self.linear_acceleration = geometry_msgs.msg.Vector3()
      self.angular_velocity = geometry_msgs.msg.Vector3()

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
      buff.write(_get_struct_B2Hi2BHdI6d().pack(_x.header.length, _x.header.id, _x.header.gnss_week, _x.header.gnss_mili, _x.imu_info, _x.imu_type, _x.gnss_week, _x.gnss_seconds, _x.imu_status, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z))
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
        self.header = novatel_pkg.msg.CommonShortHeader()
      if self.linear_acceleration is None:
        self.linear_acceleration = geometry_msgs.msg.Vector3()
      if self.angular_velocity is None:
        self.angular_velocity = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 73
      (_x.header.length, _x.header.id, _x.header.gnss_week, _x.header.gnss_mili, _x.imu_info, _x.imu_type, _x.gnss_week, _x.gnss_seconds, _x.imu_status, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z,) = _get_struct_B2Hi2BHdI6d().unpack(str[start:end])
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
      buff.write(_get_struct_B2Hi2BHdI6d().pack(_x.header.length, _x.header.id, _x.header.gnss_week, _x.header.gnss_mili, _x.imu_info, _x.imu_type, _x.gnss_week, _x.gnss_seconds, _x.imu_status, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z))
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
        self.header = novatel_pkg.msg.CommonShortHeader()
      if self.linear_acceleration is None:
        self.linear_acceleration = geometry_msgs.msg.Vector3()
      if self.angular_velocity is None:
        self.angular_velocity = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 73
      (_x.header.length, _x.header.id, _x.header.gnss_week, _x.header.gnss_mili, _x.imu_info, _x.imu_type, _x.gnss_week, _x.gnss_seconds, _x.imu_status, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z,) = _get_struct_B2Hi2BHdI6d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B2Hi2BHdI6d = None
def _get_struct_B2Hi2BHdI6d():
    global _struct_B2Hi2BHdI6d
    if _struct_B2Hi2BHdI6d is None:
        _struct_B2Hi2BHdI6d = struct.Struct("<B2Hi2BHdI6d")
    return _struct_B2Hi2BHdI6d
