"""
Solves Virtual Probe Problems Numerically
@see [US patent 8,170,820 B2](https://patents.google.com/patent/US8170820B2)
@see [US patent 7,660,685 B2](https://patents.google.com/patent/US7660685B2)
"""

# Copyright (c) 2018 Teledyne LeCroy, all rights reserved worldwide.
#
# This file is part of PySI.
#
# PySI is free software: You can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version
# 3 of the License, or any later version.
#
# This program is distrbuted in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>

from numpy import matrix
from numpy import identity

from SignalIntegrity.SystemDescriptions.VirtualProbe import VirtualProbe
from SignalIntegrity.PySIException import PySIExceptionSimulator
from SignalIntegrity.PySIException import PySIExceptionVirtualProbe

class VirtualProbeNumeric(VirtualProbe):
    """class for performing virtual probing numerically.
    @see [US patent 8,170,820 B2](https://patents.google.com/patent/US8170820B2)
    @see [US patent 7,660,685 B2](https://patents.google.com/patent/US7660685B2)
    @note For the purposes of this class, the numerical virtual probe work
    has been performed by returning the transfer matrix.  Transfer matrices
    built over many frequencies are then utilized in the actual waveform
    processing for the virtual probe processing."""
    def __init__(self,sd=None):
        """Constructor
        @param sd (optional) instance of class SystemDescription
        """
        VirtualProbe.__init__(self,sd)
    def TransferMatrix(self):
        """ returns a transfer matrix.
        @return list of list transfer matrix that for O output waveforms
        and I input waveforms is OxI and be considered as multiplied by
        a vector of input waveforms to produce a vector of output waveforms.

        The transfer matrix provided is for a single frequency.
        """
        # pragma: silent exclude
        from numpy.linalg.linalg import LinAlgError
        self.Check()
        # pragma: include
        if self.m_D is None:
            D=matrix(identity(len(self.StimsPrime())))
        else:
            D=self.m_D
        VE_m=matrix(self.VoltageExtractionMatrix(self.m_ml))
        VE_o=matrix(self.VoltageExtractionMatrix(self.m_ol))
        # pragma: silent exclude
        try:
        # pragma: include outdent
            SIPrime=matrix(self.SIPrime())
        # pragma: silent exclude indent
        except PySIExceptionSimulator as e:
            raise PySIExceptionVirtualProbe(e.message)
        # pragma: include
        # pragma: silent exclude
        try:
        # pragma: include outdent
            Result=((VE_o*SIPrime*matrix(D))*(VE_m*SIPrime*matrix(D)).getI()).tolist()
        # pragma: silent exclude indent
        except ValueError:
            raise PySIExceptionVirtualProbe('incorrect matrix alignment')
        except LinAlgError:
            raise PySIExceptionVirtualProbe('numerical error - cannot invert matrix')
        # pragma: include
        return Result