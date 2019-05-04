# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cubot/cubot_msg.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class cubot_msg(genpy.Message):
  _md5sum = "a1fc69e1ab3f3f95a2a373d704866612"
  _type = "cubot/cubot_msg"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 IMUyaw
int16 wheelspeed0
int16 wheelspeed1
int16 wheelspeed2
int16 wheelspeed3
uint32 stm32clock
int16 gyrox
int16 gyroy
int16 gyroz
int16 accx
int16 accy
int16 accz
float32 qyaw
float32 qpitch
float32 qroll
"""
  __slots__ = ['IMUyaw','wheelspeed0','wheelspeed1','wheelspeed2','wheelspeed3','stm32clock','gyrox','gyroy','gyroz','accx','accy','accz','qyaw','qpitch','qroll']
  _slot_types = ['float32','int16','int16','int16','int16','uint32','int16','int16','int16','int16','int16','int16','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       IMUyaw,wheelspeed0,wheelspeed1,wheelspeed2,wheelspeed3,stm32clock,gyrox,gyroy,gyroz,accx,accy,accz,qyaw,qpitch,qroll

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(cubot_msg, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.IMUyaw is None:
        self.IMUyaw = 0.
      if self.wheelspeed0 is None:
        self.wheelspeed0 = 0
      if self.wheelspeed1 is None:
        self.wheelspeed1 = 0
      if self.wheelspeed2 is None:
        self.wheelspeed2 = 0
      if self.wheelspeed3 is None:
        self.wheelspeed3 = 0
      if self.stm32clock is None:
        self.stm32clock = 0
      if self.gyrox is None:
        self.gyrox = 0
      if self.gyroy is None:
        self.gyroy = 0
      if self.gyroz is None:
        self.gyroz = 0
      if self.accx is None:
        self.accx = 0
      if self.accy is None:
        self.accy = 0
      if self.accz is None:
        self.accz = 0
      if self.qyaw is None:
        self.qyaw = 0.
      if self.qpitch is None:
        self.qpitch = 0.
      if self.qroll is None:
        self.qroll = 0.
    else:
      self.IMUyaw = 0.
      self.wheelspeed0 = 0
      self.wheelspeed1 = 0
      self.wheelspeed2 = 0
      self.wheelspeed3 = 0
      self.stm32clock = 0
      self.gyrox = 0
      self.gyroy = 0
      self.gyroz = 0
      self.accx = 0
      self.accy = 0
      self.accz = 0
      self.qyaw = 0.
      self.qpitch = 0.
      self.qroll = 0.

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
      buff.write(_get_struct_f4hI6h3f().pack(_x.IMUyaw, _x.wheelspeed0, _x.wheelspeed1, _x.wheelspeed2, _x.wheelspeed3, _x.stm32clock, _x.gyrox, _x.gyroy, _x.gyroz, _x.accx, _x.accy, _x.accz, _x.qyaw, _x.qpitch, _x.qroll))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 40
      (_x.IMUyaw, _x.wheelspeed0, _x.wheelspeed1, _x.wheelspeed2, _x.wheelspeed3, _x.stm32clock, _x.gyrox, _x.gyroy, _x.gyroz, _x.accx, _x.accy, _x.accz, _x.qyaw, _x.qpitch, _x.qroll,) = _get_struct_f4hI6h3f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_f4hI6h3f().pack(_x.IMUyaw, _x.wheelspeed0, _x.wheelspeed1, _x.wheelspeed2, _x.wheelspeed3, _x.stm32clock, _x.gyrox, _x.gyroy, _x.gyroz, _x.accx, _x.accy, _x.accz, _x.qyaw, _x.qpitch, _x.qroll))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 40
      (_x.IMUyaw, _x.wheelspeed0, _x.wheelspeed1, _x.wheelspeed2, _x.wheelspeed3, _x.stm32clock, _x.gyrox, _x.gyroy, _x.gyroz, _x.accx, _x.accy, _x.accz, _x.qyaw, _x.qpitch, _x.qroll,) = _get_struct_f4hI6h3f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_f4hI6h3f = None
def _get_struct_f4hI6h3f():
    global _struct_f4hI6h3f
    if _struct_f4hI6h3f is None:
        _struct_f4hI6h3f = struct.Struct("<f4hI6h3f")
    return _struct_f4hI6h3f