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
Summary(pl.UTF-8):	CDT - zestaw wtyczek do środowiska Eclipse implementujący IDE C/C++
Name:		eclipse-plugin-cdt
%define		_ver_major	4.0
%define		_ver_minor	3
Version:	%{_ver_major}.%{_ver_minor}
Release:	0.9
License:	CPL v1.0
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/cdt/releases/europa/dist/cdt-master-%{version}.zip
# Source0-md5:	ff4564cbcec07c234222dd8a779a6b3f
URL:		http://www.eclipse.org/cdt/
BuildRequires:	unzip
Requires:	eclipse >= 3.3
ExclusiveArch:	%{ix86} %{x8664} ia64 ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipse_arch	%(echo %{_target_cpu} | sed 's/i.86/x86/;s/athlon/x86/;s/pentium./x86/')
%define		_eclipsedir  	%{_libdir}/eclipse

%description
The CDT project adds a C/C++ Perspective to the Eclipse Workbench that
supports C/C++ development with a number of views, wizards, a powerful
editor, and a debugger.

%description -l pl.UTF-8
Projekt CDT rozszerza zintegrowane środowisko programistyczne Eclipse
o nowe elementy wspomagające tworzenie aplikacji w językach C i C++.

%prep
%setup -q -c

%build
rm -rf plugins/org.eclipse.cdt.*aix*_%{_ver_major}.*
rm -rf plugins/org.eclipse.cdt.*macosx*_%{_ver_major}.*
rm -rf plugins/org.eclipse.cdt.*qnx*_%{_ver_major}.*
rm -rf plugins/org.eclipse.cdt.*solaris*_%{_ver_major}.*
rm -rf plugins/org.eclipse.cdt.*win32*_%{_ver_major}.*
%ifnarch %{ix86}
rm -rf plugins/org.eclipse.cdt.*.x86_%{_ver_major}.*
%endif
%ifnarch ppc
rm -rf plugins/org.eclipse.cdt.*.ppc_%{_ver_major}.*
%endif
%ifnarch ia64
rm -rf plugins/org.eclipse.cdt.*.ia64_%{_ver_major}.*
%endif
%ifnarch %{x8664}
rm -rf plugins/org.eclipse.cdt.*.x86_64_%{_ver_major}.*
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r * $RPM_BUILD_ROOT%{_eclipsedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_eclipsedir}/features/*.jar
%{_eclipsedir}/plugins/net.sourceforge.lpg*.jar
%{_eclipsedir}/plugins/org.eclipse.ant.*.jar
%{_eclipsedir}/plugins/org.eclipse.cdt*.jar
%{_eclipsedir}/plugins/org.eclipse.test*.jar
