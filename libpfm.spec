%define major 4
%define libname %mklibname pfm
%define devname %mklibname pfm -d
%define staticname %mklibname pfm -d -s

# Broken build system
%undefine _debugsource_packages

Name: libpfm
Version: 4.13.0
Release: 1
Source0: http://sourceforge.net/projects/perfmon2/files/libpfm4/%{name}-%{version}.tar.gz
Patch0: libpfm-4.13.0-clang16.patch
Summary: Library to encode performance events for use by perf
URL: http://perfmon2.sourceforge.net/
License: MIT
Group: System/Libraries
BuildRequires: python
BuildRequires: pkgconfig(python3)
BuildRequires: python%{py_ver}dist(setuptools)
BuildRequires: swig

%description
libpfm is a library to help encode events for use with operating system
kernels performance monitoring interfaces. The current version provides support
for the perf_events interface available in upstream Linux kernels since v2.6.31.

%package -n %{libname}
Summary: Library to encode performance events for use by perf
Group: System/Libraries

%description -n %{libname}
libpfm is a library to help encode events for use with operating system
kernels performance monitoring interfaces. The current version provides support
for the perf_events interface available in upstream Linux kernels since v2.6.31.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

libpfm is a library to help encode events for use with operating system
kernels performance monitoring interfaces. The current version provides support
for the perf_events interface available in upstream Linux kernels since v2.6.31.

%package -n %{staticname}
Summary: Static library files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{staticname}
Static library files for %{name}.

libpfm is a library to help encode events for use with operating system
kernels performance monitoring interfaces. The current version provides support
for the perf_events interface available in upstream Linux kernels since v2.6.31.

%package -n python-%{name}
Summary: Python bindings for the %{name} library
Group: Development/Python
Requires: %{libname} = %{EVRD}

%description -n python-%{name}
Python bindings for the %{name} library

%prep
%autosetup -p1

%build
%make_build \
	CONFIG_PFMLIB_NOPYTHON=n \
	PREFIX=%{_prefix} \
	PYTHON_PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%install
%make_install \
	CONFIG_PFMLIB_NOPYTHON=n \
	PREFIX=%{_prefix} \
	PYTHON_PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	LDCONFIG=%{_bindir}/true

cp -a python/build/lib.linux-*/perfmon/ %{buildroot}%{python_sitearch}/

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so

%files -n %{devname}
%{_includedir}/*
%{_mandir}/man3/*.3*

%files -n %{staticname}
%{_libdir}/*.a

%files -n python-%{name}
%{python_sitearch}/perfmon
%{python_sitearch}/perfmon*.egg
