# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pfespace')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pfespace')
    _pfespace = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pfespace', [dirname(__file__)])
        except ImportError:
            import _pfespace
            return _pfespace
        try:
            _mod = imp.load_module('_pfespace', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pfespace = swig_import_helper()
    del swig_import_helper
else:
    import _pfespace
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


MFEM_VERSION = _pfespace.MFEM_VERSION
MFEM_VERSION_STRING = _pfespace.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _pfespace.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _pfespace.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _pfespace.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _pfespace.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _pfespace.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _pfespace.MFEM_VERSION_PATCH
MFEM_SOURCE_DIR = _pfespace.MFEM_SOURCE_DIR
MFEM_INSTALL_DIR = _pfespace.MFEM_INSTALL_DIR
MFEM_TIMER_TYPE = _pfespace.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _pfespace.MFEM_HYPRE_VERSION
import mfem._par.operators
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.array
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.matrix
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.mesh
import mfem._par.ncmesh
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.handle
import mfem._par.hypre
import mfem._par.pmesh
import mfem._par.pncmesh
import mfem._par.communication
import mfem._par.sets
class ParFiniteElementSpace(mfem._par.fespace.FiniteElementSpace):
    """Proxy of C++ mfem::ParFiniteElementSpace class."""

    __swig_setmethods__ = {}
    for _s in [mfem._par.fespace.FiniteElementSpace]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParFiniteElementSpace, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._par.fespace.FiniteElementSpace]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ParFiniteElementSpace, name)
    __repr__ = _swig_repr
    __swig_setmethods__["num_face_nbr_dofs"] = _pfespace.ParFiniteElementSpace_num_face_nbr_dofs_set
    __swig_getmethods__["num_face_nbr_dofs"] = _pfespace.ParFiniteElementSpace_num_face_nbr_dofs_get
    if _newclass:
        num_face_nbr_dofs = _swig_property(_pfespace.ParFiniteElementSpace_num_face_nbr_dofs_get, _pfespace.ParFiniteElementSpace_num_face_nbr_dofs_set)
    __swig_setmethods__["face_nbr_element_dof"] = _pfespace.ParFiniteElementSpace_face_nbr_element_dof_set
    __swig_getmethods__["face_nbr_element_dof"] = _pfespace.ParFiniteElementSpace_face_nbr_element_dof_get
    if _newclass:
        face_nbr_element_dof = _swig_property(_pfespace.ParFiniteElementSpace_face_nbr_element_dof_get, _pfespace.ParFiniteElementSpace_face_nbr_element_dof_set)
    __swig_setmethods__["face_nbr_ldof"] = _pfespace.ParFiniteElementSpace_face_nbr_ldof_set
    __swig_getmethods__["face_nbr_ldof"] = _pfespace.ParFiniteElementSpace_face_nbr_ldof_get
    if _newclass:
        face_nbr_ldof = _swig_property(_pfespace.ParFiniteElementSpace_face_nbr_ldof_get, _pfespace.ParFiniteElementSpace_face_nbr_ldof_set)
    __swig_getmethods__["face_nbr_glob_dof_map"] = _pfespace.ParFiniteElementSpace_face_nbr_glob_dof_map_get
    if _newclass:
        face_nbr_glob_dof_map = _swig_property(_pfespace.ParFiniteElementSpace_face_nbr_glob_dof_map_get)
    __swig_setmethods__["send_face_nbr_ldof"] = _pfespace.ParFiniteElementSpace_send_face_nbr_ldof_set
    __swig_getmethods__["send_face_nbr_ldof"] = _pfespace.ParFiniteElementSpace_send_face_nbr_ldof_get
    if _newclass:
        send_face_nbr_ldof = _swig_property(_pfespace.ParFiniteElementSpace_send_face_nbr_ldof_get, _pfespace.ParFiniteElementSpace_send_face_nbr_ldof_set)

    def __init__(self, *args):
        """
        __init__(mfem::ParFiniteElementSpace self, ParFiniteElementSpace orig, ParMesh pmesh=None, FiniteElementCollection fec=None) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, ParFiniteElementSpace orig, ParMesh pmesh=None) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, ParFiniteElementSpace orig) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, FiniteElementSpace orig, ParMesh pmesh, FiniteElementCollection fec=None) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, FiniteElementSpace orig, ParMesh pmesh) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, ParMesh pm, FiniteElementSpace global_fes, int const * partitioning, FiniteElementCollection f=None) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, ParMesh pm, FiniteElementSpace global_fes, int const * partitioning) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, ParMesh pm, FiniteElementCollection f, int dim=1, int ordering) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, ParMesh pm, FiniteElementCollection f, int dim=1) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, ParMesh pm, FiniteElementCollection f) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, ParMesh pm, mfem::NURBSExtension * ext, FiniteElementCollection f, int dim=1, int ordering) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, ParMesh pm, mfem::NURBSExtension * ext, FiniteElementCollection f, int dim=1) -> ParFiniteElementSpace
        __init__(mfem::ParFiniteElementSpace self, ParMesh pm, mfem::NURBSExtension * ext, FiniteElementCollection f) -> ParFiniteElementSpace
        """
        this = _pfespace.new_ParFiniteElementSpace(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def GetComm(self):
        """GetComm(ParFiniteElementSpace self) -> MPI_Comm"""
        return _pfespace.ParFiniteElementSpace_GetComm(self)


    def GetNRanks(self):
        """GetNRanks(ParFiniteElementSpace self) -> int"""
        return _pfespace.ParFiniteElementSpace_GetNRanks(self)


    def GetMyRank(self):
        """GetMyRank(ParFiniteElementSpace self) -> int"""
        return _pfespace.ParFiniteElementSpace_GetMyRank(self)


    def GetParMesh(self):
        """GetParMesh(ParFiniteElementSpace self) -> ParMesh"""
        return _pfespace.ParFiniteElementSpace_GetParMesh(self)


    def GetDofSign(self, i):
        """GetDofSign(ParFiniteElementSpace self, int i) -> int"""
        return _pfespace.ParFiniteElementSpace_GetDofSign(self, i)


    def GetDofOffsets(self):
        """GetDofOffsets(ParFiniteElementSpace self) -> HYPRE_Int *"""
        return _pfespace.ParFiniteElementSpace_GetDofOffsets(self)


    def GetTrueDofOffsets(self):
        """GetTrueDofOffsets(ParFiniteElementSpace self) -> HYPRE_Int *"""
        return _pfespace.ParFiniteElementSpace_GetTrueDofOffsets(self)


    def GlobalVSize(self):
        """GlobalVSize(ParFiniteElementSpace self) -> HYPRE_Int"""
        return _pfespace.ParFiniteElementSpace_GlobalVSize(self)


    def GlobalTrueVSize(self):
        """GlobalTrueVSize(ParFiniteElementSpace self) -> HYPRE_Int"""
        return _pfespace.ParFiniteElementSpace_GlobalTrueVSize(self)


    def GetTrueVSize(self):
        """GetTrueVSize(ParFiniteElementSpace self) -> int"""
        return _pfespace.ParFiniteElementSpace_GetTrueVSize(self)


    def GetElementDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _pfespace.ParFiniteElementSpace_GetElementDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetBdrElementDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _pfespace.ParFiniteElementSpace_GetBdrElementDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetFaceDofs(self, i):
        from  .array import intArray
        vdofs = intArray()
        _pfespace.ParFiniteElementSpace_GetFaceDofs(self, i, vdofs)
        return vdofs.ToList()



    def GetSharedEdgeDofs(self, group, ei):
      from  .array import intArray
      dofs = intArray()      
      _pfespace.ParFiniteElementSpace_GetSharedEdgeDofs(self, group, ei, dofs)
      return dofs.ToList()      



    def GetSharedTriangleDofs(self, group, fi, dofs):
        """GetSharedTriangleDofs(ParFiniteElementSpace self, int group, int fi, intArray dofs)"""
        return _pfespace.ParFiniteElementSpace_GetSharedTriangleDofs(self, group, fi, dofs)


    def GetSharedQuadrilateralDofs(self, group, fi, dofs):
        """GetSharedQuadrilateralDofs(ParFiniteElementSpace self, int group, int fi, intArray dofs)"""
        return _pfespace.ParFiniteElementSpace_GetSharedQuadrilateralDofs(self, group, fi, dofs)


    def Dof_TrueDof_Matrix(self):
        """Dof_TrueDof_Matrix(ParFiniteElementSpace self) -> HypreParMatrix"""
        return _pfespace.ParFiniteElementSpace_Dof_TrueDof_Matrix(self)


    def GetPartialConformingInterpolation(self):
        """GetPartialConformingInterpolation(ParFiniteElementSpace self) -> HypreParMatrix"""
        return _pfespace.ParFiniteElementSpace_GetPartialConformingInterpolation(self)


    def NewTrueDofVector(self):
        """NewTrueDofVector(ParFiniteElementSpace self) -> HypreParVector"""
        return _pfespace.ParFiniteElementSpace_NewTrueDofVector(self)


    def DivideByGroupSize(self, vec):
        """DivideByGroupSize(ParFiniteElementSpace self, double * vec)"""
        return _pfespace.ParFiniteElementSpace_DivideByGroupSize(self, vec)


    def GroupComm(self, *args):
        """
        GroupComm(ParFiniteElementSpace self) -> GroupCommunicator
        GroupComm(ParFiniteElementSpace self) -> GroupCommunicator
        """
        return _pfespace.ParFiniteElementSpace_GroupComm(self, *args)


    def ScalarGroupComm(self):
        """ScalarGroupComm(ParFiniteElementSpace self) -> GroupCommunicator"""
        return _pfespace.ParFiniteElementSpace_ScalarGroupComm(self)


    def Synchronize(self, ldof_marker):
        """Synchronize(ParFiniteElementSpace self, intArray ldof_marker)"""
        return _pfespace.ParFiniteElementSpace_Synchronize(self, ldof_marker)


    def GetEssentialVDofs(self, bdr_attr_is_ess, ess_dofs, component=-1):
        """
        GetEssentialVDofs(ParFiniteElementSpace self, intArray bdr_attr_is_ess, intArray ess_dofs, int component=-1)
        GetEssentialVDofs(ParFiniteElementSpace self, intArray bdr_attr_is_ess, intArray ess_dofs)
        """
        return _pfespace.ParFiniteElementSpace_GetEssentialVDofs(self, bdr_attr_is_ess, ess_dofs, component)


    def GetEssentialTrueDofs(self, bdr_attr_is_ess, ess_tdof_list, component=-1):
        """
        GetEssentialTrueDofs(ParFiniteElementSpace self, intArray bdr_attr_is_ess, intArray ess_tdof_list, int component=-1)
        GetEssentialTrueDofs(ParFiniteElementSpace self, intArray bdr_attr_is_ess, intArray ess_tdof_list)
        """
        return _pfespace.ParFiniteElementSpace_GetEssentialTrueDofs(self, bdr_attr_is_ess, ess_tdof_list, component)


    def GetLocalTDofNumber(self, ldof):
        """GetLocalTDofNumber(ParFiniteElementSpace self, int ldof) -> int"""
        return _pfespace.ParFiniteElementSpace_GetLocalTDofNumber(self, ldof)


    def GetGlobalTDofNumber(self, ldof):
        """GetGlobalTDofNumber(ParFiniteElementSpace self, int ldof) -> HYPRE_Int"""
        return _pfespace.ParFiniteElementSpace_GetGlobalTDofNumber(self, ldof)


    def GetGlobalScalarTDofNumber(self, sldof):
        """GetGlobalScalarTDofNumber(ParFiniteElementSpace self, int sldof) -> HYPRE_Int"""
        return _pfespace.ParFiniteElementSpace_GetGlobalScalarTDofNumber(self, sldof)


    def GetMyDofOffset(self):
        """GetMyDofOffset(ParFiniteElementSpace self) -> HYPRE_Int"""
        return _pfespace.ParFiniteElementSpace_GetMyDofOffset(self)


    def GetMyTDofOffset(self):
        """GetMyTDofOffset(ParFiniteElementSpace self) -> HYPRE_Int"""
        return _pfespace.ParFiniteElementSpace_GetMyTDofOffset(self)


    def GetProlongationMatrix(self):
        """GetProlongationMatrix(ParFiniteElementSpace self) -> Operator"""
        return _pfespace.ParFiniteElementSpace_GetProlongationMatrix(self)


    def GetRestrictionMatrix(self):
        """GetRestrictionMatrix(ParFiniteElementSpace self) -> SparseMatrix"""
        return _pfespace.ParFiniteElementSpace_GetRestrictionMatrix(self)


    def ExchangeFaceNbrData(self):
        """ExchangeFaceNbrData(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_ExchangeFaceNbrData(self)


    def GetFaceNbrVSize(self):
        """GetFaceNbrVSize(ParFiniteElementSpace self) -> int"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrVSize(self)


    def GetFaceNbrElementVDofs(self, i, vdofs):
        """GetFaceNbrElementVDofs(ParFiniteElementSpace self, int i, intArray vdofs)"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrElementVDofs(self, i, vdofs)


    def GetFaceNbrFaceVDofs(self, i, vdofs):
        """GetFaceNbrFaceVDofs(ParFiniteElementSpace self, int i, intArray vdofs)"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrFaceVDofs(self, i, vdofs)


    def GetFaceNbrFE(self, i):
        """GetFaceNbrFE(ParFiniteElementSpace self, int i) -> FiniteElement"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrFE(self, i)


    def GetFaceNbrFaceFE(self, i):
        """GetFaceNbrFaceFE(ParFiniteElementSpace self, int i) -> FiniteElement"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrFaceFE(self, i)


    def GetFaceNbrGlobalDofMap(self):
        """GetFaceNbrGlobalDofMap(ParFiniteElementSpace self) -> HYPRE_Int const *"""
        return _pfespace.ParFiniteElementSpace_GetFaceNbrGlobalDofMap(self)


    def Lose_Dof_TrueDof_Matrix(self):
        """Lose_Dof_TrueDof_Matrix(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_Lose_Dof_TrueDof_Matrix(self)


    def LoseDofOffsets(self):
        """LoseDofOffsets(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_LoseDofOffsets(self)


    def LoseTrueDofOffsets(self):
        """LoseTrueDofOffsets(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_LoseTrueDofOffsets(self)


    def Conforming(self):
        """Conforming(ParFiniteElementSpace self) -> bool"""
        return _pfespace.ParFiniteElementSpace_Conforming(self)


    def Nonconforming(self):
        """Nonconforming(ParFiniteElementSpace self) -> bool"""
        return _pfespace.ParFiniteElementSpace_Nonconforming(self)


    def GetTrueTransferOperator(self, coarse_fes, T):
        """GetTrueTransferOperator(ParFiniteElementSpace self, FiniteElementSpace coarse_fes, OperatorHandle T)"""
        return _pfespace.ParFiniteElementSpace_GetTrueTransferOperator(self, coarse_fes, T)


    def Update(self, want_transform=True):
        """
        Update(ParFiniteElementSpace self, bool want_transform=True)
        Update(ParFiniteElementSpace self)
        """
        return _pfespace.ParFiniteElementSpace_Update(self, want_transform)


    def UpdatesFinished(self):
        """UpdatesFinished(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_UpdatesFinished(self)

    __swig_destroy__ = _pfespace.delete_ParFiniteElementSpace
    __del__ = lambda self: None

    def PrintPartitionStats(self):
        """PrintPartitionStats(ParFiniteElementSpace self)"""
        return _pfespace.ParFiniteElementSpace_PrintPartitionStats(self)


    def TrueVSize(self):
        """TrueVSize(ParFiniteElementSpace self) -> int"""
        return _pfespace.ParFiniteElementSpace_TrueVSize(self)

ParFiniteElementSpace_swigregister = _pfespace.ParFiniteElementSpace_swigregister
ParFiniteElementSpace_swigregister(ParFiniteElementSpace)

class ConformingProlongationOperator(mfem._par.operators.Operator):
    """Proxy of C++ mfem::ConformingProlongationOperator class."""

    __swig_setmethods__ = {}
    for _s in [mfem._par.operators.Operator]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ConformingProlongationOperator, name, value)
    __swig_getmethods__ = {}
    for _s in [mfem._par.operators.Operator]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ConformingProlongationOperator, name)
    __repr__ = _swig_repr

    def __init__(self, pfes):
        """__init__(mfem::ConformingProlongationOperator self, ParFiniteElementSpace pfes) -> ConformingProlongationOperator"""
        this = _pfespace.new_ConformingProlongationOperator(pfes)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def Mult(self, x, y):
        """Mult(ConformingProlongationOperator self, Vector x, Vector y)"""
        return _pfespace.ConformingProlongationOperator_Mult(self, x, y)


    def MultTranspose(self, x, y):
        """MultTranspose(ConformingProlongationOperator self, Vector x, Vector y)"""
        return _pfespace.ConformingProlongationOperator_MultTranspose(self, x, y)

    __swig_destroy__ = _pfespace.delete_ConformingProlongationOperator
    __del__ = lambda self: None
ConformingProlongationOperator_swigregister = _pfespace.ConformingProlongationOperator_swigregister
ConformingProlongationOperator_swigregister(ConformingProlongationOperator)

# This file is compatible with both classic and new-style classes.


