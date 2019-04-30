# Third party imports
import numpy as np

# Local imports
from gmprocess.metrics.rotations.rotation import Rotation
from gmprocess.metrics.rotation import rotate


class GMROTD(Rotation):
    """Class for computing the GMROTD rotation."""
    def __init__(self, rotation_data, origin=None):
        """
        Args:
            rotation_data (obspy.core.stream.Stream or numpy.ndarray): Intensity
                    measurement component.
            origin (obspy.core.event.Origin): Defines the focal time and
                    geographical location of an earthquake hypocenter.
                    Default is None.
        """
        super().__init__(rotation_data, origin=None)
        self.result = self.get_gmrotd()

    def get_gmrotd(self):
        """
        Performs GMROTD rotation.

        Returns:
            rotd: numpy.ndarray of the rotated and combined traces.
        """
        horizontals = self._get_horizontals()
        osc1, osc2 = horizontals[0].data, horizontals[1].data
        osc1_rot, osc2_rot = rotate(osc1, osc2, combine=False)
        osc1_max = np.amax(osc1_rot, 1)
        osc2_max = np.amax(osc2_rot, 1)
        rotd = np.sqrt(osc1_max * osc2_max)
        return rotd