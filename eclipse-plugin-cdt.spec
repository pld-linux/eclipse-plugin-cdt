Summary:	CDT - a set of plugins for Eclipse that implement a C/C++ IDE
Name:		eclipse-plugin-cdt
%define		_ver_major	2.0
%define		_ver_minor	0
Version:	%{_ver_major}
Release:	0.1
License:	CPL
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/cdt/releases/new/zips/org.eclipse.cdt-%{version}-linux.gtk.x86.zip
# Source0-md5:	15fbefa22a0baf1e9ed4139ce219ade4
URL:		http://www.eclipse.org/cdt/
Requires:	eclipse >= 3.0
ExclusiveArch:	%{ix86} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipsedir  %{_datadir}/eclipse

%description
The CDT project provides a set of plugins that implement a C/C++ IDE.
It adds a C/C++ Perspective to the Eclipse Workbench that supports
C/C++ development with a number of views, wizards, a powerful editor,
and a debugger.

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
