%global	debug_package	%{nil}

Name:		accel-config
Version:	3.5.1
Release:	1
Summary:	Configure accelerator subsystem devices
Group:		Development/Tools
# The entire source code is under GPLv2 except for accel-config
# library which is mostly LGPLv2.1, ccan/list which is BSD-MIT and
# the rest of ccan which is CC0.
License:	GPLv2 and LGPLv2+ and MIT and CC0
URL:		https://github.com/intel/idxd-config
Source0:	%{name}-v%{version}.tar.gz

Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires:	autoconf
BuildRequires:	asciidoc
BuildRequires:	xmlto
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	systemd

# accel-config is for configuring Intel DSA (Data-Streaming
# Accelerator) subsystem in the Linux kernel. It supports x86_64 only.
ExclusiveArch:	%{ix86} x86_64

%description
Utility library for configuring the accelerator subsystem.

%package devel
Summary:	Development files for libaccfg
License:	LGPLv2+
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package libs
Summary:	Configuration library for accelerator subsystem devices
# All source code of configuration library is LGPLv2.1, except
# ccan/list which is BSD-MIT and the rest of ccan/ which is CC0.
License:	LGPLv2+ and MIT and CC0
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description libs
Libraries for %{name}.

%package test
Summary:	Tests for accel-config
License:	GPLv2
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description test
Tests for accel-config command.

%prep
%setup -q -n %{name}-v%{version}

%build
echo %{version} > version
./autogen.sh
%configure --disable-static --disable-silent-rules --enable-test
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%check
make check

%files
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/accel-config-licenses LICENSE_GPL_2_0
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*
%{_sysconfdir}/%{name}/contrib/configs/*

%files libs
%doc README.md
%license Documentation/COPYING licenses/BSD-MIT licenses/CC0
%license licenses/accel-config-licenses accfg/lib/LICENSE_LGPL_2_1
%{_libdir}/lib%{name}.so.*

%files devel
%license Documentation/COPYING
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%files test
%license Documentation/COPYING LICENSE_GPL_2_0
%doc test/README.md
%global	lib_path lib
%{_prefix}/%{lib_path}/accel-config/test/*

%changelog
* Fri Nov 25 2022 Aichun Shi <aichun.shi@intel.com> - 3.5.1-1
- Initial Packaging
