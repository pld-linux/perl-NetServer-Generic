%include	/usr/lib/rpm/macros.perl
Summary:	NetServer-Generic perl module
Summary(pl):	Modu� perla NetServer-Generic
Name:		perl-NetServer-Generic
Version:	0.03
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/NetServer/NetServer-Generic-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
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
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/NetServer/Generic
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz examples/*

%{perl_sitelib}/NetServer/Generic.pm
%{perl_sitearch}/auto/NetServer/Generic

%{_mandir}/man3/*
