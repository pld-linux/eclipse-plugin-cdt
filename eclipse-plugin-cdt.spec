Summary:	CDT - a set of plugins for Eclipse that implement a C/C++ IDE
Summary(pl):	CDT - zestaw wtyczek do ¶rodowiska Eclipse implementuj±cy IDE C/C++
Name:		eclipse-plugin-cdt
%define		_ver_major	2.0
%define		_ver_minor	2
Version:	%{_ver_major}.%{_ver_minor}
Release:	1
License:	CPL v0.5
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/cdt/releases/new/zips/org.eclipse.cdt-%{version}-linux.x86.zip
# Source0-md5:	c6e3c5f74fddae54a8ff242b42de4ade
# Source0-size:	8486704
URL:		http://www.eclipse.org/cdt/
Requires:	eclipse >= 3.0
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  %{_datadir}/eclipse

%description
The CDT project adds a C/C++ Perspective to the Eclipse Workbench that
supports C/C++ development with a number of views, wizards, a powerful
editor, and a debugger.

%description -l pl
Projekt CDT rozszerza zintegrowane ¶rodowisko programistyczne Eclipse
o nowe elementy wspomagaj±ce tworzenie aplikacji w jêzykach C i C++.

%prep
%setup -q -c

%build
%ifarch %{ix86}
rm -r eclipse/plugins/org.eclipse.cdt.core.linux_%{_ver_major}.%{_ver_minor}/os/linux/ppc
%endif
%ifarch ppc
rm -r eclipse/plugins/org.eclipse.cdt.core.linux_%{_ver_major}.%{_ver_minor}/os/linux/x86
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r * $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/*
%{_eclipsedir}/plugins/*
