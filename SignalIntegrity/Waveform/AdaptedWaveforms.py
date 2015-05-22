class AdaptedWaveforms(object):
    def __init__(self,wfl):
        from TimeDescriptor import TimeDescriptor
        from SignalIntegrity.Filters.WaveformTrimmer import WaveformTrimmer
        from SignalIntegrity.Filters.FilterDescriptor import FilterDescriptor
        from SignalIntegrity.Filters.UpsamplerLinear import Upsampler
        from SignalIntegrity.Filters.UpsamplerLinear import FractionalDelayFilter
        from SignalIntegrity.Waveform.Waveform import Waveform
        #upsample all of the waveforms first
        wful=[wf*Upsampler(int(round(wfl[0].TimeDescriptor().Fs/wf.TimeDescriptor().Fs))) for wf in wfl]
        wfcdl=[wf.TimeDescriptor()*WaveformTrimmer(0,0)*
        FractionalDelayFilter(0,True).FilterDescriptor()
            for wf in wful]
        overlapping=wfcdl[0]
        for wfcd in wfcdl[1:]:
            overlapping=overlapping.Intersection(wfcd)
        # overlapping now contains the overlapping waveform
        adl=[overlapping/wf.TimeDescriptor() for wf in wful]
        fdl=[FractionalDelayFilter(ad.D-int(ad.D),True) for ad in adl]
        adl=[FilterDescriptor(ad.U,int(ad.D),ad.S) for ad in adl]
        trl=[WaveformTrimmer(int(round(ad.TrimLeft())),int(round(ad.TrimRight()))) for ad in adl]
        self.awfl=[wf*tr*fd for (wf,tr,fd) in zip(wful,trl,fdl)]
        self.awfl=[Waveform(self.awfl[0].TimeDescriptor(),awf.Values()) for awf in self.awfl]
    def __getitem__(self,item):
        return self.awfl[item]
    def __len__(self):
        return len(self.awfl)