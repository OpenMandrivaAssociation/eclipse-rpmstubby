%define eclipse_base   %{_libdir}/eclipse
%define install_loc    %{_datadir}/eclipse/dropins/rpmstubby

Name:           eclipse-rpmstubby
Version:        0.1.1
Release:        %mkrel 2
Summary:        Rpm specfile generator for Eclipse features

Group:          Development/Java
License:        EPL
URL:            http://www.eclipse.org/linuxtools/
#sh eclipse-rpmstubby-fetch-src.sh
Source0:        %{name}-fetched-src-%{version}.tar.bz2
Source1:        eclipse-rpmstubby-fetch-src.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildArch: noarch

BuildRequires: eclipse-pde >= 1:3.4.0
BuildRequires: zip
Requires: eclipse-platform >= 3.4.0

%description
RPM Stubby Plug-in is a plugin aiming to auto-generate RPM specfile from
feature.xml.

%prep
%setup -q -n %{name}-fetched-src-%{version}

%build
%{eclipse_base}/buildscripts/pdebuild

%install
%{__rm} -rf %{buildroot}
install -d -m 755 $RPM_BUILD_ROOT%{install_loc}

%{__unzip} -q -d $RPM_BUILD_ROOT%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.rpmstubby.zip

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{install_loc}
%doc org.eclipse.linuxtools.rpmstubby-feature/license.html
%doc org.eclipse.linuxtools.rpmstubby-feature/epl-v10.html
