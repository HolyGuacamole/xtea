import unittest
from cmac import CMAC

class TestXteaCmac(unittest.TestCase):

    def testCmacComputation(self):
        key = [
            0x12, 0x34, 0x56, 0x78,
            0x12, 0x34, 0x56, 0x78,
            0x12, 0x34, 0x56, 0x78,
            0x12, 0x34, 0x56, 0x78
            ]
        cmac = CMAC(key)
        cmac.update([0xde, 0xad, 0xbe, 0xef])
        result = cmac.final()
        expectedResult = bytearray([0xb5, 0xf3, 0xeb, 0x27, 0x15, 0x45, 0xe5, 0x55])
        self.assertEqual(result, expectedResult)
