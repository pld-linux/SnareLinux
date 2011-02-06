%include	/usr/lib/rpm/macros.perl
Summary:	Snare for Linux - audit subsystem control and distribution
Name:		SnareLinux
Version:	1.5.1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.intersectalliance.com/projects/SnareLinux/Download/SnareLinux-%{version}.tar.gz
# Source0-md5:	1d469d169e7a3aecfb36b34a7fd1f90b
URL:		http://www.intersectalliance.com/
BuildRequires:	audit-libs-devel >= 1.0.16
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	audit >= 1.0.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The System iNtrusion Analysis and Reporting Environment (SNARE) agent
for Linux provides a event collection, filtering, control and remote
distribution cabability for the Linux operating system. Snare supports
organisations that need to meet national security policy guidelines
such as NISPOM, DCID/DIAM, SOX/Sarbanes Oxley, GLBA, CISP and BS7799.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D SnareDispatcher.pl $RPM_BUILD_ROOT%{_sbindir}/SnareDispatcher
install SnareDispatchHelper $RPM_BUILD_ROOT%{_sbindir}
install SnareWebServer.pl $RPM_BUILD_ROOT%{_sbindir}
install SnareTranslationTable $RPM_BUILD_ROOT%{_sbindir}
install -D snare.conf $RPM_BUILD_ROOT%{_sysconfdir}/snare.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(750,root,root) %{_sbindir}/Snare*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snare.conf
