%define oname MHonArc

Summary:	A Perl mail-to-HTML converter
Name:		mhonarc
Version:	2.6.19
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		http://www.mhonarc.org/
Source:		http://www.mhonarc.org/release/MHonArc/tar/%{oname}-%{version}.tar.bz2

# Patch based on debian that fixes some issues spotted after 2.6.19 release
Patch0:		mhonarc-2.6.19.patch
Requires:	perl >= 0:5.601
BuildArch:	noarch

Obsoletes:      MHonArc

%global __requires_exclude  %{?__requires_exclude}|^perl\\((mhamain.pl|shellwords.pl)\\)

%description
MHonArc provides HTML mail archiving with index, mail thread linking, etc; plus
other capabilities including support for MIME and powerful user customization
features. 

%prep
%setup -q -n %oname-%version 
%autopatch -p1

%build

%install
perl install.me -batch -libpath %{buildroot}%{_datadir}/MHonArc -nodoc \
	-manpath %{buildroot}%{_mandir} -binpath %{buildroot}%{_bindir}

# just in case
cd %{buildroot}
find . -type f -exec perl -pi -e "s|%{buildroot}||g" {} \;

%files
%doc ACKNOWLG BUGS CHANGES README.txt RELNOTES
%doc doc examples extras logo
%{_bindir}/*
%{_datadir}/MHonArc
%{_mandir}/*/*



