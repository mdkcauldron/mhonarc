%define  name mhonarc
%define oname MHonArc
%define version 2.6.18
%define release %mkrel 2

Summary:	A Perl mail-to-HTML converter
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Networking/WWW
URL:		http://www.mhonarc.org/
Source:		http://www.mhonarc.org/release/MHonArc/tar/%{oname}-%{version}.tar.bz2
Patch0:         MHonArc-2.6.15-fix-perl.patch 
Requires:	perl >= 0:5.601
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{oname}%{version}

Obsoletes:      MHonArc

%description
MHonArc provides HTML mail archiving with index, mail thread linking, etc; plus
other capabilities including support for MIME and powerful user customization
features. 

%prep

%setup -q -n %oname-%version 
%patch0 -p1

%build

%install
rm -rf %{buildroot}

perl install.me -batch -libpath %{buildroot}%{_datadir}/MHonArc -nodoc \
	-manpath %{buildroot}%{_mandir} -binpath %{buildroot}%{_bindir}

# just in case
cd %{buildroot}
find . -type f -exec perl -pi -e "s|%{buildroot}||g" {} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ACKNOWLG BUGS CHANGES README.txt RELNOTES
%doc doc examples extras logo
%{_bindir}/*
%{_datadir}/MHonArc
%{_mandir}/*/*



