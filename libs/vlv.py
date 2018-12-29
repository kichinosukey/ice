class VLV:
    def __init__(self, ivo=None, ivc=None, evo=None, evc=None, 
                ivo_base=360, ivc_base=540, evo_base=180, evc_base=360):
        
        self.ivo = ivo
        self.ivc = ivc
        self.evo = evo
        self.evc = evc

        self.ivo_base = ivo_base
        self.ivc_base = ivc_base
        self.evo_base = evo_base
        self.evc_base = evc_base
    
    def add(self, ivo=None, ivc=None, evo=None, evc=None, cain=None, caex=None):
        """
        - cain and caex are assumed to be retarded
        """
        if ivo is not None:
            self.ivo = self.ivo_base + ivo
        if ivc is not None:
            self.ivc = self.ivc_base + ivc
        if evo is not None:
            self.evo = self.evo_base + evo
        if evo is not None:
            self.evc = self.evc_base + evc
        if cain is not None:
            self.cain = cain
            if ivo is not None:
                self.ivo += self.cain
            if ivc is not None:
                self.ivc -= self.cain
        if caex is not None:
            self.caex = caex
            if evo is not None:
                self.evo -= self.caex
            if evc is not None:
                self.evc += self.caex
        
