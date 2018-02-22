# Teledyne LeCroy Inc. ("COMPANY") CONFIDENTIAL
# Unpublished Copyright (c) 2015-2016 Peter J. Pupalaikis and Teledyne LeCroy,
# All Rights Reserved.
#
# Explicit license in accompanying README.txt file.  If you don't have that file
# or do not agree to the terms in that file, then you are not licensed to use
# this material whatsoever.

def VoltageAmplifier(P,G,Zi,Zo):
    """symbolic 2,3, and 4 port voltage amplifier
    @param P integer number of ports (2,3,4)\n
    if ports are 2, then returns SignalIntegrity.Symbolic.VoltageAmplifier.VoltageAmplifierTwoPort\n
    if ports are 3, then returns SignalIntegrity.Symbolic.VoltageAmplifier.VoltageAmplifierThreePort\n
    if ports are 4, then returns SignalIntegrity.Symbolic.VoltageAmplifier.VoltageAmplifierFourPort
    @param G string voltage gain
    @param Zi string input impedance
    @param Zo string output impedance
    @return list of list of string s-parameter matrix
    containing LaTeX or ASCII strings for each element.
    @note strings can be any valid LaTeX
    """
    if P==2:
        return VoltageAmplifierTwoPort(G,Zi,Zo)
    elif P==3:
        return VoltageAmplifierThreePort(G,Zi,Zo)
    elif P==4:
        return VoltageAmplifierFourPort(G,Zi,Zo)

def VoltageAmplifierFourPort(G,Zi,Zo):
    """symbolic four port current amplifier
    @param G string voltage gain
    @param Zi string input impedance
    @param Zo string output impedance
    @return list of list of string s-parameter matrix
    containing LaTeX or ASCII strings for each element.
    @note strings can be any valid LaTeX
    @note this is the symbolic version of SignalIntegrity.Devices.VoltageAmplifier.VoltageAmplifierFourPort
    """
    return [['\\frac{'+Zi+'}{'+Zi+'+2\\cdot Z0}','\\frac{2\\cdot Z0}{'+Zi+'+2\\cdot Z0}','0','0'],
            ['\\frac{2\\cdot Z0}{'+Zi+'+2\\cdot Z0}','\\frac{'+Zi+'}{'+Zi+'+2\\cdot Z0}','0','0'],
            ['\\frac{2\\cdot '+Zi+'\\cdot Z0\\cdot '+G+'}{\\left('+Zi+'+2\\cdot Z0\\right)\\cdot\left('+Zo+'+2\\cdot Z0\\right)}',
            '-\\frac{2\\cdot '+Zi+'\\cdot Z0\\cdot '+G+'}{\\left('+Zi+'+2\\cdot Z0\\right)\\cdot\\left('+Zo+'+2\\cdot Z0\\right)}',
            '\\frac{'+Zo+'}{'+Zo+'+2\\cdot Z0}','\\frac{2\\cdot Z0}{'+Zo+'+2\\cdot Z0}'],
            ['-\\frac{2\\cdot '+Zi+'\\cdot Z0\\cdot '+G+'}{\\left('+Zi+'+2\\cdot Z0\\right)\\cdot\\left('+Zo+'+2\\cdot Z0\\right)}',
            '\\frac{2\\cdot '+Zi+'\\cdot Z0\\cdot '+G+'}{\\left('+Zi+'+2\\cdot Z0\\right)\\cdot\\left('+Zo+'+2\\cdot Z0\\right)}',
            '\\frac{2\\cdot Z0}{'+Zo+'+2\\cdot Z0}','\\frac{'+Zo+'}{'+Zo+'+2\\cdot Z0}']]

def VoltageAmplifierThreePort(G,Zi,Zo):
    """symbolic three port voltage amplifier
    @param G string voltage gain
    @param Zi string input impedance
    @param Zo string output impedance
    @return list of list of string s-parameter matrix
    containing LaTeX or ASCII strings for each element.
    @note strings can be any valid LaTeX
    @note this is the symbolic version of SignalIntegrity.Devices.VoltageAmplifier.VoltageAmplifierThreePort
    """
    D='-'+Zo+'\\cdot '+Zi+'-2\\cdot '+Zo+'\\cdot Z0-2\\cdot '+Zi+'\\cdot Z0-3\\cdot Z0^2+'+G+'\\cdot '+Zi+'\\cdot Z0'
    S11='\\frac{-'+Zo+'\\cdot '+Zi+'-2\\cdot '+Zi+'\\cdot Z0+Z0^2+'+G+'\\cdot '+Zi+'\\cdot Z0}{'+D+'}'
    S12='\\frac{-2\\cdot Z0^2}{'+D+'}'
    S13='\\frac{-2\\cdot Z0\\cdot\\left('+Zo+' +Z0\\right)}{'+D+'}'
    S21='\\frac{-2\\cdot Z0 \\cdot\\left('+G+'\\cdot '+Zi+' +Z0\\right)}{'+D+'}'
    S22='\\frac{Z0^2-2\\cdot '+Zo+'\\cdot Z0+'+G+'\\cdot '+Zi+'\\cdot Z0-'+Zo+'\\cdot '+Zi+'}{'+D+'}'
    S23='\\frac{2\\cdot Z0\\cdot\\left('+G+'\\cdot '+Zi+'-'+Zi+'-Z0\\right)}{'+D+'}'
    S31='\\frac{2\\cdot Z0\\cdot\\left(-Z0+'+G+'\\cdot '+Zi+'-'+Zo+'\\right)}{'+D+'}'
    S32='\\frac{-2\\cdot Z0\\cdot\\left('+Zi+'+Z0\\right)}{'+D+'}'
    S33='\\frac{-'+Zo+'\\cdot '+Zi+'+Z0^2-'+G+'\\cdot '+Zi+'\\cdot Z0}{'+D+'}'
    return [[S11,S12,S13],
            [S21,S22,S23],
            [S31,S32,S33]]

def VoltageAmplifierTwoPort(G,Zi,Zo):
    """symbolic two port voltage amplifier
    @param G string voltage gain
    @param Zi string input impedance
    @param Zo string output impedance
    @return list of list of string s-parameter matrix
    containing LaTeX or ASCII strings for each element.
    @note strings can be any valid LaTeX
    @note this is the symbolic version of SignalIntegrity.Devices.VoltageAmplifier.VoltageAmplifierTwoPort
    """
    return [['\\frac{'+Zi+' - Z0}{'+Zi+' + Z0}','0'],
            ['\\frac{2\\cdot '+G+' \\cdot '+Zi+' \\cdot Z0}{\\left( '+Zi+' +Z0\\right)\\cdot\\left( '+Zo+' + Z0\\right)}','\\frac{'+Zo+' - Z0}{'+Zo+' + Z0}']]
