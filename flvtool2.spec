%define name	flvtool2
%define version 1.0.6
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Manipulation tool for Macromedia Flash Video files (FLV)

Group:		Video
License:	BSD
URL:		http://www.inlet-media.de/flvtool2
Source:		%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildArch:	noarch

BuildRequires:	ruby
Requires:	ruby

%description
FLVTool2 can calculate a lot of meta data and insert a onMetaData tag.
It can cut FLV files and add cue Points (onCuePoint). A debug command 
lets you see inside our FLV and the print command gives you meta data 
information in XML or YAML format.

%prep
%setup -q

%build
ruby setup.rb config
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
ruby setup.rb install --prefix=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/flvtool2
cp LICENSE CHANGELOG $RPM_BUILD_ROOT%{_datadir}/doc/flvtool2/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%ruby_sitelibdir/*
%doc CHANGELOG LICENSE

