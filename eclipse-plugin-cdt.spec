Summary:	CDT - a set of plugins for Eclipse that implement a C/C++ IDE
Summary(pl):	CDT - zestaw wtyczek do ¶rodowiska Eclipse implementuj±cy IDE C/C++
Name:		eclipse-plugin-cdt
%define		_ver_major	2.1
%define		_ver_minor	0
Version:	%{_ver_major}.%{_ver_minor}
Release:	1
License:	CPL v1.0
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/cdt/releases/new/zips/%{version}/org.eclipse.cdt-%{version}-linux.x86.zip
# Source0-md5:	1542dee90e6c4451d51a8135f2860f41
Source1:	http://download.eclipse.org/tools/cdt/releases/new/zips/%{version}/org.eclipse.cdt-%{version}-linux.ppc.zip
# Source1-md5:	d7f15a696ba60dd3460c06117b4c2989
Source2:	http://download.eclipse.org/tools/cdt/releases/new/zips/%{version}/org.eclipse.cdt-%{version}-linux.ia64.zip
# Source2-md5:	04ee41cbe5bbcdf47d2199ede1ed7edc
URL:		http://www.eclipse.org/cdt/
BuildRequires:	unzip
Requires:	eclipse >= 3.0
ExclusiveArch:	%{ix86} ppc ia64
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

%build
%ifnarch %{ix86}
rm -r eclipse/plugins/org.eclipse.cdt.core.linux_%{_ver_major}.%{_ver_minor}/os/linux/x86
%endif
%ifnarch ppc
rm -r eclipse/plugins/org.eclipse.cdt.core.linux_%{_ver_major}.%{_ver_minor}/os/linux/ppc
%endif
%ifnarch ia64
rm -r eclipse/plugins/org.eclipse.cdt.core.linux_%{_ver_major}.%{_ver_minor}/os/linux/ia64
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

%dir %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*
%dir %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*/os
%dir %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*/os/linux
%dir %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*/os/linux/%{_eclipse_arch}
%attr(755,root,root) %{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*/os/linux/%{_eclipse_arch}/*.so
%{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*/*.jar
%{_eclipsedir}/plugins/org.eclipse.cdt.core.linux_*.*.*/*.xml

%{_eclipsedir}/plugins/org.eclipse.cdt.debug.core_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.debug.mi.core_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.debug.mi.ui_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.debug.ui_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.doc.user_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.launch_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.make.core_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.make.ui_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.managedbuilder.core_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.managedbuilder.ui_*.*.*
%{_eclipsedir}/plugins/org.eclipse.cdt.ui_*.*.*
