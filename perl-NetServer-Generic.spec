%include	/usr/lib/rpm/macros.perl
%define	pdir	NetServer
%define	pnam	Generic
Summary:	NetServer::Generic perl module
Summary(pl):	Modu³ perla NetServer::Generic
Name:		perl-NetServer-Generic
Version:	1.03
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetServer::Generic - simple TCP/IP server.

%description -l pl
NetServer::Generic - prosty serwer TCP/IP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/NetServer/Generic.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755) %{_examplesdir}/%{name}-%{version}/*
