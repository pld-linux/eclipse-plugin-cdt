#
# Conditional build:
%bcond_without	incall	# don't include all tarballs in .src.rpm
#
%define		plugin_name	cdt
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
Name:		eclipse-plugin-%{plugin_name}
%define		_ver_major	7.0
%define		_ver_minor	2
Version:	%{_ver_major}.%{_ver_minor}
Release:	1
License:	CPL v1.0
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/cdt/releases/helios/dist/cdt-master-%{version}.zip
# Source0-md5:	01a34887d24bded98769f44fccc51282
URL:		http://www.eclipse.org/cdt/
BuildRequires:	unzip
Requires:	eclipse >= 3.6
ExclusiveArch:	%{ix86} %{x8664} ia64 ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/eclipse/dropins/%{plugin_name}

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
install -d $RPM_BUILD_ROOT%{_plugindir}/{features,plugins}
cp -a * $RPM_BUILD_ROOT%{_plugindir}

rm $RPM_BUILD_ROOT%{_plugindir}/artifacts.jar
rm $RPM_BUILD_ROOT%{_plugindir}/content.jar
rm $RPM_BUILD_ROOT%{_plugindir}/epl-v10.html
rm $RPM_BUILD_ROOT%{_plugindir}/notice.html
rm $RPM_BUILD_ROOT%{_plugindir}/pack.properties
rm $RPM_BUILD_ROOT%{_plugindir}/site.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_plugindir}
%dir %{_plugindir}/features
%dir %{_plugindir}/plugins
%{_plugindir}/features/*.jar
%{_plugindir}/plugins/net.sourceforge.lpg*.jar
%{_plugindir}/plugins/org.eclipse.ant.*.jar
%{_plugindir}/plugins/org.eclipse.cdt*.jar
%{_plugindir}/plugins/org.eclipse.test*.jar
%{_plugindir}/plugins/org.eclipse.tm.tcf*.jar
