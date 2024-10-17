%define eclipse_base   %{_libdir}/eclipse
%define install_loc    %{_datadir}/eclipse/dropins/rpmstubby
%define qualifier      201006152250

Name:           eclipse-rpmstubby
Version:        0.6.0
Release:        4
Summary:        Rpm specfile generator for Eclipse features

Group:          Development/Java
License:        EPL
URL:            https://www.eclipse.org/linuxtools/projectPages/rpmstubby/
#sh eclipse-rpmstubby-fetch-src.sh
Source0:        %{name}-fetched-src-%{version}.tar.bz2
Source1:        eclipse-rpmstubby-fetch-src.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

BuildRequires: eclipse-pde >= 0:3.4.0
Requires: eclipse-platform >= 3.4.0

%description
RPM Stubby Plug-in is a plugin aiming to auto-generate RPM specfile from
feature.xml.

%prep
%setup -q -n %{name}-fetched-src-%{version}
cp org.eclipse.linuxtools.rpmstubby-feature/ChangeLog org.eclipse.linuxtools.rpmstubby-feature/ChangeLog.feature

%build
%{eclipse_base}/buildscripts/pdebuild \
 -a "-DforceContextQualifier=%{qualifier} -DjavacSource=1.5 -DjavacTarget=1.5"

%install
%{__rm} -rf %{buildroot}
install -d -m 755 %{buildroot}%{install_loc}

%{__unzip} -q -d %{buildroot}%{install_loc} \
     build/rpmBuild/org.eclipse.linuxtools.rpmstubby.zip

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{install_loc}
%doc org.eclipse.linuxtools.rpmstubby-feature/license.html
%doc org.eclipse.linuxtools.rpmstubby-feature/epl-v10.html
%doc org.eclipse.linuxtools.rpmstubby-feature/ChangeLog.feature
%doc org.eclipse.linuxtools.rpmstubby/ChangeLog

