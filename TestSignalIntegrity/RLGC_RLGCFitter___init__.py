class RLGCFitter(LevMar):
    def __init__(self,sp,guess,callback=None):
        self.m_sp=sp
        self.f=self.m_sp.m_f
        self.Z0=self.m_sp.m_Z0
        v=self.VectorizeSp(sp)
        LevMar.__init__(self,callback)
        LevMar.Initialize(self, [[g] for g in guess], v)
        self.ones=[1 for _ in self.f]
        self.dZdR=self.ones
        self.dZdRse=[math.sqrt(f) for f in self.f]
        self.p2f=[2.*math.pi*f for f in self.f]
        self.dZdL=[1j*p2f for p2f in self.p2f]
        self.zeros=[0 for _ in self.f]
        self.dZdG=self.zeros
        self.dZdC=self.zeros
        self.dZddf=self.zeros
        self.dYdR=self.zeros
        self.dYdRse=self.zeros
        self.dYdL=self.zeros
        self.dYdG=self.ones
    def fF(self,x):
        (R,L,G,C,Rse,df)=(x[0][0],x[1][0],x[2][0],x[3][0],x[4][0],x[5][0])
        self.Z=[R+Rse*math.sqrt(f)+1j*2.*math.pi*f*L for f in self.f]
        self.Y=[G+2.*math.pi*f*C*(1j+df) for f in self.f]
        self.gamma=[cmath.sqrt(z*y) for (z,y) in zip(self.Z,self.Y)]
        self.Zc=[cmath.sqrt(z/y) for (z,y) in zip(self.Z,self.Y)]
        self.rho=[(zc-self.Z0)/(zc+self.Z0) for zc in self.Zc]
        self.rho2=[r*r for r in self.rho]
        self.eg=[cmath.exp(-g) for g in self.gamma]
        self.e2g=[egx*egx for egx in self.eg]
        self.S11=[r*(1-e2)/(1-r2*e2) for (r,e2,r2) in zip(self.rho,self.e2g,self.rho2)]
        self.S12=[(1-r2)*e/(1-r2*e2) for (r2,e,e2) in zip(self.rho2,self.eg,self.e2g)]
        S=[[[s11,s12],[s12,s11]] for (s11,s12) in zip(self.S11,self.S12)]
        vS=self.VectorizeSp(S)
        return vS
...
