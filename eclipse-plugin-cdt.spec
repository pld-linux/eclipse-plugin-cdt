#
# Conditional build:
%bcond_without	incall	# don't include all tarballs in .src.rpm
#
%define		need_x86	0
%define		need_ppc	0
%define		need_ia64	0
%define		need_x8664	0

%if %{with incall}
%define		need_x86	1
%define		need_ppc	1
%define		need_ia64	1
%define		need_x8664	1
%else
%ifarch %{ix86}
%define		need_x86	1
%endif
%ifarch ppc
%define		need_ppc	1
%endif
%ifarch ia64
%define		need_ia64	1
%endif
%ifarch %{x8664}
%define		need_x8664	1
%endif
%endif

Summary:	CDT - a set of plugins for Eclipse that implement a C/C++ IDE
Summary(pl):	CDT - zestaw wtyczek do ¶rodowiska Eclipse implementuj±cy IDE C/C++
Name:		eclipse-plugin-cdt
%define		_ver_major	3.0
%define		_ver_minor	2
Version:	%{_ver_major}.%{_ver_minor}
Release:	2
License:	CPL v1.0
Group:		Development/Languages
%if %{need_x86}
Source0:	http://download.eclipse.org/tools/cdt/releases/eclipse3.1/dist/%{version}/org.eclipse.cdt-%{version}-linux.x86.tar.gz
# Source0-md5:	815b072169285c4fc2b7ed04951df28c
%endif
%if %{need_ppc}
Source1:	http://download.eclipse.org/tools/cdt/releases/eclipse3.1/dist/%{version}/org.eclipse.cdt-%{version}-linux.ppc.tar.gz
# Source1-md5:	8ec4a4dfe2e6a53f27934dacc1e457ee
%endif
%if %{need_ia64}
Source2:	http://download.eclipse.org/tools/cdt/releases/eclipse3.1/dist/%{version}/org.eclipse.cdt-%{version}-linux.ia64.tar.gz
# Source2-md5:	5cf7cc9acdbe357ba7f4b2ed979b4b0e
%endif
%if %{need_x8664}
Source3:	http://download.eclipse.org/tools/cdt/releases/eclipse3.1/dist/%{version}/org.eclipse.cdt-%{version}-linux.x86_64.tar.gz
# Source3-md5:	38ed3260a22f493934465cf1fdfb394e
%endif
URL:		http://www.eclipse.org/cdt/
BuildRequires:	unzip
Requires:	eclipse >= 3.0
ExclusiveArch:	%{ix86} %{x8664} ia64 ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipse_arch	%(echo %{_target_cpu} | sed 's/i.86/x86/;s/athlon/x86/;s/pentium./x86/')
%define		_eclipsedir  	%{_libdir}/eclipse

%description
The CDT project adds a C/C++ Perspective to the Eclipse Workbench that
supports C/C++ development with a number of views, wizards, a powerful
editor, and a debugger.

%description -l pl
Projekt CDT rozszerza zintegrowane ¶rodowisko programistyczne Eclipse
o nowe elementy wspomagaj±ce tworzenie aplikacji w jêzykach C i C++.

%prep
%ifarch %{ix86}
%setup -q -c -T -b0
%endif
%ifarch ppc
%setup -q -c -T -b1
%endif
%ifarch ia64
%setup -q -c -T -b2
%endif
%ifarch %{x8664}
%setup -q -c -T -b3
%endif

%build
%ifnarch %{ix86}
rm -rf eclipse/plugins/org.eclipse.cdt.core.linux_%{_ver_major}.%{_ver_minor}/os/linux/x86
%endif
%ifnarch ppc
rm -rf eclipse/plugins/org.eclipse.cdt.core.linux_%{_ver_major}.%{_ver_minor}/os/linux/ppc
%endif
%ifnarch ia64
rm -rf eclipse/plugins/org.eclipse.cdt.core.linux_%{_ver_major}.%{_ver_minor}/os/linux/ia64
%endif
%ifnarch %{x8664}
rm -rf eclipse/plugins/org.eclipse.cdt.core.linux_%{_ver_major}.%{_ver_minor}/os/linux/x86_64
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r * $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/*
%dir %{_eclipsedir}/plugins
%{_eclipsedir}/plugins/org.eclipse.cdt_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.core_*.*.*

%dir %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux.%{_eclipse_arch}_*.*.*
%dir %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux.%{_eclipse_arch}_*.*.*/os
%dir %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux.%{_eclipse_arch}_*.*.*/os/linux
%dir %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux.%{_eclipse_arch}_*.*.*/os/linux/%{_eclipse_arch}
%attr(755,root,root) %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux.%{_eclipse_arch}_*.*.*/os/linux/%{_eclipse_arch}/*.so
%dir %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*/*.jar
%{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*/*.xml
%{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*/*.html
%{_eclipsedir}/plugins/org.eclipse.cdt.core.linux.%{_eclipse_arch}_*.*.*/*.xml
%{_eclipsedir}/plugins/org.eclipse.cdt.core.linux.%{_eclipse_arch}_*.*.*/*.html

%{_eclipsedir}/plugins/org.eclipse.cdt.debug.core_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.debug.mi.core_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.debug.mi.ui_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.debug.ui_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.doc.user_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.launch_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.make.core_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.make.ui_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.managedbuilder.core_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.managedbuilder.gnu.ui_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.managedbuilder.ui_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.refactoring_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.ui_*.*.*
