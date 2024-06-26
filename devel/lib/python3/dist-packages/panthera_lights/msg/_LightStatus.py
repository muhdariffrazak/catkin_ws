# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from panthera_lights/LightStatus.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class LightStatus(genpy.Message):
  _md5sum = "e88e78a8e709ed3fa5e5e18d48c62d5d"
  _type = "panthera_lights/LightStatus"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 Brake
uint8 HazardLight
uint8 SignalRight
uint8 SignalLeft
uint8 Autonomous
uint8 TeleOp
uint8 Beacon
uint8 Night
uint8 Day
"""
  __slots__ = ['Brake','HazardLight','SignalRight','SignalLeft','Autonomous','TeleOp','Beacon','Night','Day']
  _slot_types = ['uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       Brake,HazardLight,SignalRight,SignalLeft,Autonomous,TeleOp,Beacon,Night,Day

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LightStatus, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.Brake is None:
        self.Brake = 0
      if self.HazardLight is None:
        self.HazardLight = 0
      if self.SignalRight is None:
        self.SignalRight = 0
      if self.SignalLeft is None:
        self.SignalLeft = 0
      if self.Autonomous is None:
        self.Autonomous = 0
      if self.TeleOp is None:
        self.TeleOp = 0
      if self.Beacon is None:
        self.Beacon = 0
      if self.Night is None:
        self.Night = 0
      if self.Day is None:
        self.Day = 0
    else:
      self.Brake = 0
      self.HazardLight = 0
      self.SignalRight = 0
      self.SignalLeft = 0
      self.Autonomous = 0
      self.TeleOp = 0
      self.Beacon = 0
      self.Night = 0
      self.Day = 0

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
      buff.write(_get_struct_9B().pack(_x.Brake, _x.HazardLight, _x.SignalRight, _x.SignalLeft, _x.Autonomous, _x.TeleOp, _x.Beacon, _x.Night, _x.Day))
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
      end = 0
      _x = self
      start = end
      end += 9
      (_x.Brake, _x.HazardLight, _x.SignalRight, _x.SignalLeft, _x.Autonomous, _x.TeleOp, _x.Beacon, _x.Night, _x.Day,) = _get_struct_9B().unpack(str[start:end])
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
      buff.write(_get_struct_9B().pack(_x.Brake, _x.HazardLight, _x.SignalRight, _x.SignalLeft, _x.Autonomous, _x.TeleOp, _x.Beacon, _x.Night, _x.Day))
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
      end = 0
      _x = self
      start = end
      end += 9
      (_x.Brake, _x.HazardLight, _x.SignalRight, _x.SignalLeft, _x.Autonomous, _x.TeleOp, _x.Beacon, _x.Night, _x.Day,) = _get_struct_9B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_9B = None
def _get_struct_9B():
    global _struct_9B
    if _struct_9B is None:
        _struct_9B = struct.Struct("<9B")
    return _struct_9B
