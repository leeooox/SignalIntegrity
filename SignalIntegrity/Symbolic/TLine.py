# Teledyne LeCroy Inc. ("COMPANY") CONFIDENTIAL
# Unpublished Copyright (c) 2015-2016 Peter J. Pupalaikis and Teledyne LeCroy,
# All Rights Reserved.
# 
# Explicit license in accompanying README.txt file.  If you don't have that file
# or do not agree to the terms in that file, then you are not licensed to use
# this material whatsoever.

def TLine(P,rho,gamma):
    """symbolic two-port transmission

    symbolic two and four port single-ended transmission line based on rho and gamma

    @param P integer number of ports (2 or 4)\n
    for two ports, returns SignalIntegrity.Symbolic.TLine.TLineTwoPort\n
    for four ports, return SignalIntegrity.Symbolic.TLine.TLineFourPort\n
    @param rho string reflection coefficient
    @param gamma string gamma
    @return list of list of string s-parameter matrix
    containing LaTeX or ASCII strings for each element.
    @note strings can be any valid LaTeX
    @note use SignalIntegrity.Symbolic.TLine.TLineRho if you want to enter the string
    representation of rho based on the characteristic impedance.
    @note use SignalIntegrity.Symbolic.TLine.TLineGamma if you want to enter the string
    representation of gamma based on a time delay
    """
    if P==2:
        return TLineTwoPort(rho,gamma)
    elif P==4:
        return TLineFourPort(rho,gamma)

def TLineRho(Zc,ports=2):
    """string representation of rho from the characteristic impedance
    @param Zc string characteristic impedance
    @param ports (optional) integer number of ports (defaults to two).
    @return string LaTeX representation of rho
    @note that rho is different for a four-port single-ended transmission line.
    """
    if ports == 2:
        return ' \\frac{ '+Zc+'-Z0 }{ '+Zc+' + Z0 }'
    elif ports == 4:
        return ' \\frac{ \\frac{ '+Zc+' }{2} - Z0  }{ \\frac{ '+Zc+' }{2} + Z0 }'

def TLineGamma(Td):
    """string representation of gamma from the propagation time
    @param Td string propagation time
    @return string LaTeX representation of gamma (as a function of frequency)
    """
    return ' -j \\cdot 2 \\pi \\cdot f \\cdot '+Td

def TLineTwoPort(rho,gamma):
    """symbolic single-ended two-port transmission line
    @param rho string reflection coefficient
    @param gamma string gamma
    @return list of list of string s-parameter matrix
    containing LaTeX or ASCII strings for each element.
    @note strings can be any valid LaTeX
    @note use SignalIntegrity.Symbolic.TLine.TLineRho if you want to enter the string
    representation of rho based on the characteristic impedance.
    @note use SignalIntegrity.Symbolic.TLine.TLineGamma if you want to enter the string
    representation of gamma based on a time delay
    @note this is the symbolic version of SignalIntegrity.Devices.TLineTwoPort.TLineTwoPort except that by
    default it's base on rho for symbolic simplicity (Zc complicates the look of things).
    """
    L='e^{'+gamma+'}'
    L2='e^{2 \\cdot '+gamma+' } '
    D='1 - \\left[ '+rho+' \\right]^2 \\cdot '+L2
    S1=' \\frac{ '+rho+' \\cdot \\left( 1 - '+L2+' \\right) }{ '+D+' }'
    S2=' \\frac{ '+L+' \\cdot \\left( 1 - \\left[ '+rho+' \\right] ^2 \\right) }{ '+D+' } '
    return [[S1,S2],[S2,S1]]

def TLineFourPort(rho,gamma):
    """symbolic single-ended four-port transmission line
    @param rho string reflection coefficient
    @param gamma string gamma
    @return list of list of string s-parameter matrix
    containing LaTeX or ASCII strings for each element.
    @note strings can be any valid LaTeX
    @note use SignalIntegrity.Symbolic.TLine.TLineRho if you want to enter the string
    representation of rho based on the characteristic impedance.
    @note use SignalIntegrity.Symbolic.TLine.TLineGamma if you want to enter the string
    representation of gamma based on a time delay
    @note this is the symbolic version of SignalIntegrity.Devices.TLineFourPort.TLineFourPort except that by
    default it's base on rho for symbolic simplicity (Zc complicates the look of things).
    """
    Y='e^{'+gamma+' } '
    Y2='e^{2 \\cdot '+gamma+' } '
    D='2 \\cdot \\left( 1 - '+Y2+' \\cdot \\left[ '+rho+' \\right]^2 \\right)'
    S1= '\\frac{ 1 - '+Y2+' \\cdot \\left[ '+rho+' \\right]^2 + '+rho+' \\cdot \\left( 1 - '+Y2+' \\right) }{ '+D+' } '
    S2= '\\frac{ \\left( 1 - \\left[ '+rho+' \\right]^2 \\right) \\cdot '+Y+' }{ '+D+' } '
    S3= '\\frac{ 1 - '+Y2+' \\cdot \\left[ '+rho+' \\right]^2 - '+rho+' \\cdot \\left( 1 - '+Y2+' \\right)  }{ '+D+' } '
    return [[S1,S2,S3,'-'+S2],
            [S2,S1,'-'+S2,S3],
            [S3,'-'+S2,S1,S2],
            ['-'+S2,S3,S2,S1]]
