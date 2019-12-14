import unittest
import pinocchio as pin
pin.switchToNumpyMatrix()
import numpy as np

class TestFCLTransformConversion(unittest.TestCase):

    def test_from_SE3(self):

        M = pin.SE3.Random()
        #fcl_transform = pin.hppfcl.Transform3f(M)
        #
        #self.assertEqual(M.rotation,fcl_transform.getRotation())
        #self.assertEqual(M.translation,fcl_transform.getTranslation())
    
    def test_to_SE3(self):
        
        fcl_transform = pin.hppfcl.Transform3f()
        M = pin.SE3(fcl_transform)
        self.assertEqual(M.isIdentity())

if __name__ == '__main__':
    if pin.WITH_HPP_FCL_BINDINGS:
        unittest.main()
