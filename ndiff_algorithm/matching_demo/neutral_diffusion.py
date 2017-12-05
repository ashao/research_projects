import _neutral_diffusion
import f90wrap.runtime
import logging

class Neutral_Diffusion_Driver(f90wrap.runtime.FortranModule):
    """
    Module neutral_diffusion_driver
    
    
    Defined at neutral_diffusion_driver.F90 lines 1-171
    
    """
    class Neutral_Diffusion_Cs(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=neutral_diffusion_cs)
        
        
        Defined at neutral_diffusion_driver.F90 lines 18-31
        
        """
        def __init__(self, handle=None):
            """
            self = Neutral_Diffusion_Cs()
            
            
            Defined at neutral_diffusion_driver.F90 lines 18-31
            
            
            Returns
            -------
            this : Neutral_Diffusion_Cs
            	Object to be constructed
            
            
            Automatically generated constructor for neutral_diffusion_cs
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            self._handle = _neutral_diffusion.f90wrap_neutral_diffusion_cs_initialise()
        
        def __del__(self):
            """
            Destructor for class Neutral_Diffusion_Cs
            
            
            Defined at neutral_diffusion_driver.F90 lines 18-31
            
            Parameters
            ----------
            this : Neutral_Diffusion_Cs
            	Object to be destructed
            
            
            Automatically generated destructor for neutral_diffusion_cs
            """
            if self._alloc:
                _neutral_diffusion.f90wrap_neutral_diffusion_cs_finalise(this=self._handle)
        
        @property
        def ppoly_deg(self):
            """
            Element ppoly_deg ftype=integer  pytype=int
            
            
            Defined at neutral_diffusion_driver.F90 line 19
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__ppoly_deg(self._handle)
        
        @ppoly_deg.setter
        def ppoly_deg(self, ppoly_deg):
            _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__ppoly_deg(self._handle, \
                ppoly_deg)
        
        @property
        def continuous_reconstruction(self):
            """
            Element continuous_reconstruction ftype=logical pytype=bool
            
            
            Defined at neutral_diffusion_driver.F90 line 20
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__continuous_reconstruction(self._handle)
        
        @continuous_reconstruction.setter
        def continuous_reconstruction(self, continuous_reconstruction):
            \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__continuous_reconstruction(self._handle, \
                continuous_reconstruction)
        
        @property
        def boundary_extrap(self):
            """
            Element boundary_extrap ftype=logical pytype=bool
            
            
            Defined at neutral_diffusion_driver.F90 line 21
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__boundary_extrap(self._handle)
        
        @boundary_extrap.setter
        def boundary_extrap(self, boundary_extrap):
            \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__boundary_extrap(self._handle, \
                boundary_extrap)
        
        @property
        def refine_pos(self):
            """
            Element refine_pos ftype=logical pytype=bool
            
            
            Defined at neutral_diffusion_driver.F90 line 22
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__refine_pos(self._handle)
        
        @refine_pos.setter
        def refine_pos(self, refine_pos):
            _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__refine_pos(self._handle, \
                refine_pos)
        
        @property
        def max_iter(self):
            """
            Element max_iter ftype=integer  pytype=int
            
            
            Defined at neutral_diffusion_driver.F90 line 23
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__max_iter(self._handle)
        
        @max_iter.setter
        def max_iter(self, max_iter):
            _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__max_iter(self._handle, \
                max_iter)
        
        @property
        def tolerance(self):
            """
            Element tolerance ftype=double precision pytype=unknown
            
            
            Defined at neutral_diffusion_driver.F90 line 24
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__tolerance(self._handle)
        
        @tolerance.setter
        def tolerance(self, tolerance):
            _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__tolerance(self._handle, \
                tolerance)
        
        @property
        def ref_pres(self):
            """
            Element ref_pres ftype=double precision pytype=unknown
            
            
            Defined at neutral_diffusion_driver.F90 line 25
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__ref_pres(self._handle)
        
        @ref_pres.setter
        def ref_pres(self, ref_pres):
            _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__ref_pres(self._handle, \
                ref_pres)
        
        @property
        def eos_name(self):
            """
            Element eos_name ftype=character(len=80) pytype=str
            
            
            Defined at neutral_diffusion_driver.F90 line 26
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__eos_name(self._handle)
        
        @eos_name.setter
        def eos_name(self, eos_name):
            _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__eos_name(self._handle, \
                eos_name)
        
        @property
        def drho_dt(self):
            """
            Element drho_dt ftype=double precision pytype=unknown
            
            
            Defined at neutral_diffusion_driver.F90 line 27
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__drho_dt(self._handle)
        
        @drho_dt.setter
        def drho_dt(self, drho_dt):
            _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__drho_dt(self._handle, \
                drho_dt)
        
        @property
        def drho_ds(self):
            """
            Element drho_ds ftype=double precision pytype=unknown
            
            
            Defined at neutral_diffusion_driver.F90 line 28
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__drho_ds(self._handle)
        
        @drho_ds.setter
        def drho_ds(self, drho_ds):
            _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__drho_ds(self._handle, \
                drho_ds)
        
        @property
        def remapping_scheme(self):
            """
            Element remapping_scheme ftype=character(len=80) pytype=str
            
            
            Defined at neutral_diffusion_driver.F90 line 30
            
            """
            return \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__get__remapping_scheme(self._handle)
        
        @remapping_scheme.setter
        def remapping_scheme(self, remapping_scheme):
            \
                _neutral_diffusion.f90wrap_neutral_diffusion_cs__set__remapping_scheme(self._handle, \
                remapping_scheme)
        
        def __str__(self):
            ret = ['<neutral_diffusion_cs>{\n']
            ret.append('    ppoly_deg : ')
            ret.append(repr(self.ppoly_deg))
            ret.append(',\n    continuous_reconstruction : ')
            ret.append(repr(self.continuous_reconstruction))
            ret.append(',\n    boundary_extrap : ')
            ret.append(repr(self.boundary_extrap))
            ret.append(',\n    refine_pos : ')
            ret.append(repr(self.refine_pos))
            ret.append(',\n    max_iter : ')
            ret.append(repr(self.max_iter))
            ret.append(',\n    tolerance : ')
            ret.append(repr(self.tolerance))
            ret.append(',\n    ref_pres : ')
            ret.append(repr(self.ref_pres))
            ret.append(',\n    eos_name : ')
            ret.append(repr(self.eos_name))
            ret.append(',\n    drho_dt : ')
            ret.append(repr(self.drho_dt))
            ret.append(',\n    drho_ds : ')
            ret.append(repr(self.drho_ds))
            ret.append(',\n    remapping_scheme : ')
            ret.append(repr(self.remapping_scheme))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    @staticmethod
    def neutral_diffusion_init(ref_pres, remapping_scheme, boundary_extrap, \
        refine_position, tolerance, max_iter, eos_name, drho_dt=None, drho_ds=None):
        """
        cs = neutral_diffusion_init(ref_pres, remapping_scheme, boundary_extrap, \
            refine_position, tolerance, max_iter, eos_name[, drho_dt, drho_ds])
        
        
        Defined at neutral_diffusion_driver.F90 lines 36-62
        
        Parameters
        ----------
        ref_pres : unknown
        remapping_scheme : str
        boundary_extrap : bool
        refine_position : bool
        tolerance : unknown
        max_iter : int
        eos_name : str
        drho_dt : unknown
        drho_ds : unknown
        
        Returns
        -------
        cs : Neutral_Diffusion_Cs
        
        """
        cs = _neutral_diffusion.f90wrap_neutral_diffusion_init(ref_pres=ref_pres, \
            remapping_scheme=remapping_scheme, boundary_extrap=boundary_extrap, \
            refine_position=refine_position, tolerance=tolerance, max_iter=max_iter, \
            eos_name=eos_name, drho_dt=drho_dt, drho_ds=drho_ds)
        cs = neutral_diffusion_driver.Neutral_Diffusion_Cs.from_handle(cs)
        return cs
    
    @staticmethod
    def find_neutral_surfaces(self, nk, tl, sl, hl, tr, sr, hr, pol, por, kol, kor, \
        heff):
        """
        find_neutral_surfaces(self, nk, tl, sl, hl, tr, sr, hr, pol, por, kol, kor, \
            heff)
        
        
        Defined at neutral_diffusion_driver.F90 lines 64-171
        
        Parameters
        ----------
        cs : Neutral_Diffusion_Cs
        nk : int
        tl : unknown array
        sl : unknown array
        hl : unknown array
        tr : unknown array
        sr : unknown array
        hr : unknown array
        pol : unknown array
        por : unknown array
        kol : int array
        kor : int array
        heff : unknown array
        
        """
        _neutral_diffusion.f90wrap_find_neutral_surfaces(cs=self._handle, nk=nk, tl=tl, \
            sl=sl, hl=hl, tr=tr, sr=sr, hr=hr, pol=pol, por=por, kol=kol, kor=kor, \
            heff=heff)
    
    _dt_array_initialisers = []
    

neutral_diffusion_driver = Neutral_Diffusion_Driver()

