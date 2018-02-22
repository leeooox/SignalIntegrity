# Teledyne LeCroy Inc. ("COMPANY") CONFIDENTIAL
# Unpublished Copyright (c) 2015-2016 Peter J. Pupalaikis and Teledyne LeCroy,
# All Rights Reserved.
# 
# Explicit license in accompanying README.txt file.  If you don't have that file
# or do not agree to the terms in that file, then you are not licensed to use
# this material whatsoever.

from SignalIntegrity.Devices import TeeThreePortSafe

class Numeric(object):
    def InstallSafeTees(self,Z=0.00001):
        for d in range(len(self)):
            if '#' in self[d].Name:
                self[d].AssignSParameters(TeeThreePortSafe(0.000000001))
