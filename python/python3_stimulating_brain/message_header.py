from message import ISerializable
import struct


class Header(ISerializable):
    def __init__(self, buffer):
        # 3 unsigned int, 2 byte, 1 unsigned short
        self.struct_fmt = '=3I2BH'
        self.struct_len = struct.calcsize(self.struct_fmt)

        if buffer != None:
            unpacked = struct.unpack(self.struct_fmt, buffer)

            self.MSGID, self.MSGTYPE, self.BODYLEN, self.FRAGMENTED, self.LASTMSG, self.SEQ = unpacked

    def GetBytes(self):
        # *(), *[]은 해당 튜플, 리스트를 언패킹함.
        return struct.pack(self.struct_fmt, *(
                self.MSGID, self.MSGTYPE, self.BODYLEN, self.FRAGMENTED, self.LASTMSG, self.SEQ
        ))

    def GetSize(self):
        return self.struct_len