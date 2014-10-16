Summary:	GPT text-mode partitioning tool
Name:		gptfdisk
Version:	0.8.10
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/project/gptfdisk/gptfdisk/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9cf4246c181c324bdbd553fe9b348373
URL:		http://www.rodsbooks.com/gdisk/
BuildRequires:	icu-devel
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-devel
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPT fdisk (consisting of the gdisk, cgdisk, sgdisk, and fixparts
programs) is a set of text-mode partitioning tools for Linux, FreeBSD,
Mac OS X, and Windows. The gdisk, cgdisk, and sgdisk programs work on
Globally Unique Identifier (GUID) Partition Table (GPT) disks, rather
than on the more common (through 2011) Master Boot Record (MBR)
partition tables. The fixparts program repairs certain types of damage
to MBR disks and enables changing partition types from primary
to logical and vice-versa.

%prep
%setup -q

%build
export CXXFLAGS="%{rpmcxxflags} -I%{_includedir}/ncurses"
export LDFLAGS="%{rpmldflags}"

%{__make} \
	CC="%{__cc}"	\
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install {,c,s}gdisk fixparts $RPM_BUILD_ROOT%{_sbindir}
install {{,c,s}gdisk,fixparts}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*

