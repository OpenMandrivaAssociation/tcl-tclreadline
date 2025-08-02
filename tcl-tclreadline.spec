%global realname tclreadline
%global libname %mklibname tclreadline
%global devname %mklibname tclreadline -d
# libname is `libtclreadline-X.Y.Z.so`, not so-versioned

Name:		tcl-tclreadline
Version:	2.4.1
Release:	1
Source0:	https://github.com/flightaware/tclreadline/archive/refs/tags/v%{version}.tar.gz
Patch0:	tclreadline-2.4.1.patch
Summary:	GNU readline for interactive Tcl shells
URL:		https://github.com/flightaware/tclreadline
License:	BSD-3-Clause
Group:		System/Libraries
BuildRequires:	autoconf automake slibtool
BuildRequires:	tcl-devel tk-devel
BuildRequires:	readline-devel
Requires:	%{libname} = %{EVRD}

%description
The tclreadline package makes GNU readline available
to the scripting language Tcl. The primary purpose of the package
is to facilitate interactive script development by the means
of word and file name completion as well as history expansion
(well known from shells like bash).

This package contains the Tcl binding for %{realname}.

%prep
%autosetup -p1 -n %{realname}-%{version}
NOCONFIGURE=1 sh autogen.sh # regenerate a broken configure script..

%conf
%configure --with-tcl=%{_libdir} --enable-tclshrl --enable-wishrl

%build
%make_build

%install
%make_install
# `package require tclreadline` needs help to find its library
ln -sf ../../libtclreadline-%{version}.so %{buildroot}%{tcl_sitearch}/tclreadline%{version}/libtclreadline.so

%files
%{tcl_sitearch}/tclreadline%{version}/pkgIndex.tcl
%{tcl_sitearch}/tclreadline%{version}/tclreadlineCompleter.tcl
%{tcl_sitearch}/tclreadline%{version}/tclreadlineInit.tcl
%{tcl_sitearch}/tclreadline%{version}/tclreadlineSetup.tcl
%{tcl_sitearch}/tclreadline%{version}/libtclreadline.so
%{_mandir}/mann/tclreadline.n.zst

%package -n %{name}-cli
Summary:	Command-line utilities for %{realname}
Group:		System/Libraries
Requires:	%{name}
Requires:	tk >= %{tcl_version}

%description -n %{name}-cli
The tclreadline package makes GNU readline available
to the scripting language Tcl. The primary purpose of the package
is to facilitate interactive script development by the means
of word and file name completion as well as history expansion
(well known from shells like bash).

This package contains the command-line utilities for %{realname}.

%files -n %{name}-cli
%{_bindir}/tclshrl
%{_bindir}/wishrl

%package -n %{libname}
Summary:	Runtime library for %{realname}
Group:		System/Libraries
Requires:	tcl >= %{tcl_version}

%description -n %{libname}
The tclreadline package makes GNU readline available
to the scripting language Tcl. The primary purpose of the package
is to facilitate interactive script development by the means
of word and file name completion as well as history expansion
(well known from shells like bash).

This package contains the runtime library for %{libname}.

%files -n %{libname}
%{_libdir}/libtclreadline-%{version}.so

%package -n %{devname}
Summary:	Development library and header files for %{realname}
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{realname}-devel = %{EVRD}

%description -n %{devname}
The tclreadline package makes GNU readline available
to the scripting language Tcl. The primary purpose of the package
is to facilitate interactive script development by the means
of word and file name completion as well as history expansion
(well known from shells like bash).

This package contains the header files for %{libname}.

%files -n %{devname}
%{_includedir}/tclreadline.h
%{_libdir}/libtclreadline.so
