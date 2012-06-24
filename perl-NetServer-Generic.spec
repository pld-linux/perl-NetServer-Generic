%include	/usr/lib/rpm/macros.perl
Summary:	NetServer-Generic perl module
Summary(pl):	Modu� perla NetServer-Generic
Name:		perl-NetServer-Generic
Version:	1.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/NetServer/NetServer-Generic-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetServer-Generic - simple TCP/IP server.

%description -l pl
NetServer-Generic - prosty serwer TCP/IP.

%prep
%setup -q -n NetServer-Generic-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples/*
%{perl_sitelib}/NetServer/Generic.pm
%{_mandir}/man3/*
