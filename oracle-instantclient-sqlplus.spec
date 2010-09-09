# NOTE:
# - see "URL:" for download links
# - if you want to build 32-bit version, you don't have to download Source1.
#   Just comment it out.
# - if you want to build 64-bit version, comment out Source0
# - it requires libraries provided by oracle-instantclient-basic

%define		i386rel		0.1
%define		x8664rel	0.1.0-1

Summary:	Oracle Database Client - SQL*Plus
Summary(pl.UTF-8):	Klient bazy danych Oracle
Name:		oracle-instantclient-sqlplus
Version:	11.2
Release:	0.1
License:	OTN (proprietary, non-distributable)
Group:		Applications
Source0:	instantclient-sqlplus-linux32-%{version}.%{i386rel}.zip
# NoSource0-md5:	94a004ee4f58149e62ed76107217d7c8
Source1:	oracle-instantclient%{version}-sqlplus-%{version}.%{x8664rel}.x86_64.zip
# NoSource1-md5:	1fdc0c3544194de35d2aabe9e6b3faf5
NoSource:	0
NoSource:	1
URL:		http://www.oracle.com/technology/software/tech/oci/instantclient/index.html
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		srcdir	instantclient_%(echo %{version} | tr . _)

%description
Oracle Database Instant Client Package - SQL*Plus.
Additional libraries and executable for running SQL*Plus
with Instant Client.

%description -l pl.UTF-8
Klient bazy danych Oracle.

%prep
%ifarch %{ix86}
%setup -q -c -T -b 0
%endif

%ifarch %{x8664}
%setup -q -c -T -b 1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir}/sqlplus}

install -p %{srcdir}/libsqlplusic.so $RPM_BUILD_ROOT%{_libdir}/libsqlplusic.so
install -p %{srcdir}/libsqlplus.so $RPM_BUILD_ROOT%{_libdir}/libsqlplus.so
install -p %{srcdir}/sqlplus $RPM_BUILD_ROOT%{_bindir}/sqlplus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsqlplusic.so
%attr(755,root,root) %{_libdir}/libsqlplus.so
%attr(755,root,root) %{_bindir}/sqlplus
%doc %{srcdir}/SQLPLUS_README
