%define		plugin_name	cdt
Summary:	CDT - a set of plugins for Eclipse that implement a C/C++ IDE
Summary(pl.UTF-8):	CDT - zestaw wtyczek do środowiska Eclipse implementujący IDE C/C++
Name:		eclipse-plugin-%{plugin_name}
Version:	8.2.1
Release:	1
License:	CPL v1.0
Group:		Development/Languages
Source0:	http://download.eclipse.org/tools/cdt/releases/kepler/sr1/cdt-master-%{version}.zip
# Source0-md5:	c45a575ebafa29e748b19d643d77cdbf
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
%setup -qc

rm -rfv plugins/org.eclipse.cdt.core.aix*_*.*
rm -rfv plugins/org.eclipse.cdt.core.macosx*_*.*
rm -rfv plugins/org.eclipse.cdt.core.solaris*_*.*
rm -rfv plugins/org.eclipse.cdt.core.win32*_*.*
%ifnarch %{ix86}
rm -rfv plugins/org.eclipse.cdt.core.linux.x86_?.*
%endif
%ifnarch ppc ppc64
rm -rfv plugins/org.eclipse.cdt.core.linux.ppc64_*.*
%endif
%ifnarch %{x8664}
rm -rfv plugins/org.eclipse.cdt.core.linux.x86_64_*.*
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}/{features,plugins}
cp -a * $RPM_BUILD_ROOT%{_plugindir}

rm $RPM_BUILD_ROOT%{_plugindir}/artifacts.jar
rm $RPM_BUILD_ROOT%{_plugindir}/content.jar
rm -r $RPM_BUILD_ROOT%{_plugindir}/binary

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_plugindir}
%dir %{_plugindir}/features
%dir %{_plugindir}/plugins
%{_plugindir}/META-INF
%{_plugindir}/features/*.jar*
%{_plugindir}/plugins/net.sourceforge.lpg*.jar*
%{_plugindir}/plugins/org.eclipse.linuxtools.cdt.*.jar*
%{_plugindir}/plugins/org.eclipse.cdt*.jar*
