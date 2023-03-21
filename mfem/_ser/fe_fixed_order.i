%module(package="mfem._ser") fe_fixed_order
%{
#include  "mfem.hpp"
#include "pyoperator.hpp"      
#include "numpy/arrayobject.h"    
%}

%init %{
import_array();
%}
%include "../common/mfem_config.i"
%include "exception.i"
%import "fe.i"
%import "fe_base.i"
%import "element.i"
%include "../common/typemap_macros.i"
%include "../common/exception.i"


%include "fem/fe/fe_fixed_order.hpp"
