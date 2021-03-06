# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MyGame

import flatbuffers

class MonsterExtra(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsMonsterExtra(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MonsterExtra()
        x.Init(buf, n + offset)
        return x

    # MonsterExtra
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MonsterExtra
    def TestfNan(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return float('nan')

    # MonsterExtra
    def TestfPinf(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return float('inf')

    # MonsterExtra
    def TestfNinf(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return float('-inf')

    # MonsterExtra
    def TestdNan(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return float('nan')

    # MonsterExtra
    def TestdPinf(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return float('inf')

    # MonsterExtra
    def TestdNinf(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float64Flags, o + self._tab.Pos)
        return float('-inf')

def MonsterExtraStart(builder): builder.StartObject(6)
def MonsterExtraAddTestfNan(builder, testfNan): builder.PrependFloat32Slot(0, testfNan, float('nan'))
def MonsterExtraAddTestfPinf(builder, testfPinf): builder.PrependFloat32Slot(1, testfPinf, float('inf'))
def MonsterExtraAddTestfNinf(builder, testfNinf): builder.PrependFloat32Slot(2, testfNinf, float('-inf'))
def MonsterExtraAddTestdNan(builder, testdNan): builder.PrependFloat64Slot(3, testdNan, float('nan'))
def MonsterExtraAddTestdPinf(builder, testdPinf): builder.PrependFloat64Slot(4, testdPinf, float('inf'))
def MonsterExtraAddTestdNinf(builder, testdNinf): builder.PrependFloat64Slot(5, testdNinf, float('-inf'))
def MonsterExtraEnd(builder): return builder.EndObject()
