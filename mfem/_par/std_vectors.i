%module(package="mfem._par") std_vectors
//
//  std_vectors :
//     this modules gather all std::vector based object
//     the reason why we have this module is %include "std_vector.i"
//     can not be imported. Otherwise, SWIGPY_SLICE_ARG is not decleared
//     in a module which imports i file where std_vector.i is imported.
%{
#include <vector>
#include "mfem.hpp"  
#include "numpy/arrayobject.h"
#include "pyoperator.hpp"
#include "../common/pycoefficient.hpp"
#include "../common/io_stream.hpp"
%}


%init %{
import_array();
%}

%include "exception.i"

%import "array.i"
//%import "mesh.i"
//%import "pfespace.i"
//%import "pmesh.i"

%include "std_vector.i"
%template(vector_int) std::vector<int>;
%template(vector_Vector) std::vector<mfem::Vector>;
%template(vector_intArray) std::vector<mfem::Array<int>>;
%template(vector_ParFiniteElementSpace) std::vector<mfem::ParFiniteElementSpace *>;
%template(vector_ParMesh) std::vector<mfem::ParMesh *>;
%template(vector_HypreParMatrix) std::vector<mfem::HypreParMatrix *>;


  
