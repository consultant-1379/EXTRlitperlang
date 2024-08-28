%define debug_package %{nil}
%global _missing_build_ids_terminate_build 0
%global realversion 17.5
%global realname erlang
%global rpmversion <rpm.version>
%global packager <ericsson.rstate>

#
# spec file for package erlang
#
# Copyright (c) 1997-2014 Ericsson AB. All Rights Reserved.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#


Name:           EXTRlitperlang_CXP9031333
Version:        %{rpmversion}
Release:        0
Summary:        General-purpose programming language and runtime environment
License:        ErlPL-1.1
Group:          Development/Languages/Other
Packager:       %{packager}
Url:            http://www.erlang.org
Source:        http://www.erlang.org/download/erlang-%{realversion}.tar.gz
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{realname}-%{realversion}-build
Provides: %{realname} = %{realversion}
Provides: %{realname}(x86-64) = %{realversion}


%if 0%{?suse_version} >=1230
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%define have_systemd 1 
%endif

%define epmd_home %{_var}/lib/epmd

%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.

%package debugger
Summary:        A debugger for debugging and testing of Erlang programs
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}

%description debugger
A debugger for debugging and testing of Erlang programs.

%package dialyzer
Summary:        A DIscrepany AnaLYZer for ERlang programs
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}
Requires:       graphviz

%description dialyzer
A DIscrepany AnaLYZer for ERlang programs.

%package doc
Summary:        Erlang documentation
Group:          Development/Languages/Other

%description doc
Documentation for Erlang.

%package epmd
Summary:        Erlang Port Mapper daemon
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description epmd
The Erlang Port Mapper daemon acts as a name server on all hosts involved in distributed Erlang computations.

%package et
Summary:        An event tracer for Erlang programs
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}

%description et
An event tracer for Erlang programs.

%package jinterface
Summary:        Erlang Java Interface
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}
Requires:       java >= 1.5.0

%description jinterface
JInterface module for accessing erlang from Java

%package gs
Summary:        A library for Tcl/Tk support in Erlang
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       tk

%description gs
A Graphics System used to write platform independent user interfaces.

%package reltool
Summary:        A release management tool
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}

%description reltool
Reltool is a release management tool. It analyses a given
Erlang/OTP installation and determines various dependencies
between applications. The graphical frontend depicts the
dependencies and enables interactive customization of a
target system. The backend provides a batch interface
for generation of customized target systems.

%package observer
Summary:        A GUI tool for observing an erlang system
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description observer
The observer is gui frontend containing various tools to inspect a system.
It displays system information, application structures, process information,
ets or mnesia tables and a frontend for tracing with ttb. 

%package src
Summary:        Erlang/OTP applications sources
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description src
Erlang sources for all the applications in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package debugger-src
Summary:        Erlang/OTP debugger application sources
Group:          Development/Languages/Other
Requires:       %{name}-debugger = %{version}

%description debugger-src
Erlang sources for the debugger application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package dialyzer-src
Summary:        Erlang/OTP dialyzer application sources
Group:          Development/Languages/Other
Requires:       %{name}-dialyzer = %{version}

%description dialyzer-src
Erlang sources for the dialyzer application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package et-src
Summary:        Erlang/OTP et application sources
Group:          Development/Languages/Other
Requires:       %{name}-et = %{version}

%description et-src
Erlang sources for the et application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package gs-src
Summary:        Erlang/OTP gs application sources
Group:          Development/Languages/Other
Requires:       %{name}-gs = %{version}

%description gs-src
Erlang sources for the gs application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package jinterface-src
Summary:        Erlang/OTP jinterface application sources
Group:          Development/Languages/Other
Requires:       %{name}-jinterface = %{version}

%description jinterface-src
Erlang sources for the jinterface application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package reltool-src
Summary:        Erlang/OTP reltool application sources
Group:          Development/Languages/Other
Requires:       %{name}-reltool = %{version}

%description reltool-src
Erlang sources for the reltool application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package observer-src
Summary:        Erlang/OTP observer application sources
Group:          Development/Languages/Other
Requires:       %{name}-observer = %{version}

%description observer-src
Erlang sources for the observer application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating

embedded systems.
%package toolbar-src
Summary:        Erlang/OTP toolbar application sources
Group:          Development/Languages/Other
Requires:       %{name}-toolbar = %{version}

%description toolbar-src
Erlang sources for the toolbar application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package tv-src
Summary:        Erlang/OTP tv application sources
Group:          Development/Languages/Other
Requires:       %{name}-tv = %{version}

%description tv-src
Erlang sources for the tv application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package toolbar
Summary:        A tool bar simplifying access to the Erlang tools
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}

%description toolbar
A tool bar simplifying access to the Erlang tools.

%package tv
Summary:        An ETS and MNESIA graphical table visualizer
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-gs = %{version}

%description tv
An ETS and MNESIA graphical table visualizer.

%prep
%setup -q -n  otp_src_%{realversion}


./otp_build autoconf
%build
%debug_package
%if 0%{?suse_version} == 1100 || 0%{?fedora_version} == 9
export CFLAGS="-fno-strict-aliasing"
%else
export CFLAGS="%{optflags} -fno-strict-aliasing"
%endif
export CXXFLAGS=$CFLAGS
#    --with-ssl=%{_prefix} \
%configure \
    --without-javac \
    --without-java \
    --without-jinterface \
    --without-ic \
    --without-orber \
    --without-odbc \
    --without-diameter \
    --without-wx \
    --without-cosTransactions \
    --without-cosEventDomain \
    --without-cosEvent \
    --without-cosFile \
    --without-cosTime \
    --without-cosProperty \
    --without-cosNotifications \
    --without-rpath \
    --enable-threads \
    --enable-smp-support \
    --enable-kernel-poll \
    --enable-hipe \
    --enable-buildin-zlib \
    --enable-dynamic-ssl-lib \
    --disable-javac \
    --disable-wx \
    --disable-gs \
    --disable-rpath

# clean stalled files before rebuild them
make %{?_smp_mflags} clean

touch ./lib/ose/SKIP
touch ./lib/cosTransactions/SKIP
touch ./lib/cosEventDomain/SKIP
touch ./lib/cosEvent/SKIP
touch ./lib/cosFileTransfer/SKIP
touch ./lib/cosTime/SKIP
touch ./lib/cosProperty/SKIP
touch ./lib/cosNotification/SKIP

make

%install
%if 0%{?sles_version} >= 10
    make DESTDIR=%{buildroot} install
%else
    %make_install
%endif

export TOOLS_VERSION=`ls %{buildroot}%{_libdir}/erlang/lib/ |grep ^tools- | sed "s|tools-||"`

# clean up
find %{buildroot}%{_libdir}/erlang -perm 0775 | xargs chmod -v 0755
find %{buildroot}%{_libdir}/erlang -name Makefile | xargs chmod -v 0644
find %{buildroot}%{_libdir}/erlang -name \*.bat | xargs rm -fv
find %{buildroot}%{_libdir}/erlang -name index.txt.old | xargs rm -fv
rm %{buildroot}%{_libdir}/erlang/lib/tools-$TOOLS_VERSION/emacs/test.erl.orig
mv %{buildroot}%{_libdir}/erlang/lib/tools-$TOOLS_VERSION/emacs/test.erl.indented %{buildroot}%{_libdir}/erlang/lib/tools-$TOOLS_VERSION/emacs/test.erl

# doc
mkdir -p erlang_doc

# The man-pages for binaries are safe to move to %{_mandir}, others may conflict with other packages

mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
cat > %{buildroot}%{_datadir}/emacs/site-lisp/erlang.el << EOF
(setq load-path (cons "%{_libdir}/erlang/lib/tools-$TOOLS_VERSION/emacs" load-path))
(add-to-list 'load-path "%{_datadir}/emacs/site-lisp/ess")
(load-library "erlang-start")
EOF

%if 0%{?suse_version} > 1020
# hardlink duplicates:
find . -name "start_erl*" | xargs chmod 755
%fdupes %{buildroot}/%{_libdir}/erlang
# %%doc macro copies the files to the package doc dir, hardlinks thus don't work
%endif

install -d -m 0750        %{buildroot}%{epmd_home}
install -d -m 0755        %{buildroot}%{_sbindir}

%files
%defattr(-,root,root)
%{_bindir}/*
%exclude %{_bindir}/dialyzer
%exclude %{_bindir}/epmd
%dir %{_libdir}/erlang
%dir %{_libdir}/erlang/lib/
%exclude %{_libdir}/erlang/lib/*/src
%exclude %{_libdir}/erlang/lib/*/c_src
%{_libdir}/erlang/bin/
%exclude %{_libdir}/erlang/bin/dialyzer
%{_libdir}/erlang/bin/epmd
%{_libdir}/erlang/erts-*/
%exclude %{_libdir}/erlang/erts-*/bin/dialyzer
%{_libdir}/erlang/erts-*/bin/epmd
%{_libdir}/erlang/lib/asn1-*/
%{_libdir}/erlang/lib/common_test-*/
%{_libdir}/erlang/lib/compiler-*/
%{_libdir}/erlang/lib/crypto-*/
%{_libdir}/erlang/lib/edoc-*/
%{_libdir}/erlang/lib/erl_docgen-*/
%{_libdir}/erlang/lib/erl_interface-*/
%{_libdir}/erlang/lib/erts-*/
%{_libdir}/erlang/lib/eunit-*/
%{_libdir}/erlang/lib/hipe-*/
%{_libdir}/erlang/lib/inets-*/
%{_libdir}/erlang/lib/kernel-*/
%{_libdir}/erlang/lib/megaco-*/
%{_libdir}/erlang/lib/mnesia-*/
%{_libdir}/erlang/lib/os_mon-*/
%{_libdir}/erlang/lib/otp_mibs-*/
%{_libdir}/erlang/lib/parsetools-*/
%{_libdir}/erlang/lib/percept-*/
%{_libdir}/erlang/lib/public_key-*/
%{_libdir}/erlang/lib/runtime_tools-*/
%{_libdir}/erlang/lib/sasl-*/
%{_libdir}/erlang/lib/snmp-*/
%{_libdir}/erlang/lib/ssh-*/
%{_libdir}/erlang/lib/ssl-*/
%{_libdir}/erlang/lib/stdlib-*/
%{_libdir}/erlang/lib/syntax_tools-*/
%{_libdir}/erlang/lib/test_server-*/
%{_libdir}/erlang/lib/tools-*/
%{_libdir}/erlang/lib/typer-*/
%{_libdir}/erlang/lib/webtool-*/
%{_libdir}/erlang/lib/xmerl-*/
%{_libdir}/erlang/lib/eldap-*/
#%exclude %{_libdir}/erlang/lib/ose-*/
%{_libdir}/erlang/releases/
%{_libdir}/erlang/usr/
%{_libdir}/erlang/Install
%{_libdir}/erlang/misc/
%{_datadir}/emacs/site-lisp/erlang.el
%{_bindir}/epmd
%{_libdir}/erlang/bin/epmd
%{_libdir}/erlang/erts-*/bin/epmd

%files debugger
%defattr(-,root,root)
%{_libdir}/erlang/lib/debugger-*/
%exclude %{_libdir}/erlang/lib/debugger-*/src

%files dialyzer
%defattr(-,root,root)
%{_libdir}/erlang/lib/dialyzer-*/
%exclude %{_libdir}/erlang/lib/dialyzer-*/src
%{_bindir}/dialyzer
%{_libdir}/erlang/bin/dialyzer
%{_libdir}/erlang/erts-*/bin/dialyzer


%files et
%defattr(-,root,root)
%{_libdir}/erlang/lib/et-*/
%exclude %{_libdir}/erlang/lib/et-*/src

%files gs
%defattr(-,root,root)
%{_libdir}/erlang/lib/gs-*/
%exclude %{_libdir}/erlang/lib/gs-*/src


%files reltool
%defattr(-,root,root)
%{_libdir}/erlang/lib/reltool-*/
%exclude %{_libdir}/erlang/lib/reltool-*/src

%files observer
%defattr(-,root,root)
%{_libdir}/erlang/lib/observer-*/
%exclude %{_libdir}/erlang/lib/observer-*/src


%defattr(-,root,root)
