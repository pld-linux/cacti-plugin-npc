# TODO
# - Edit the MySQL options on line 143 of /cacti/plugins/npc/neb/inserter.c
# - not lib64 safe
%define		namesrc	npc
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - NPC
Summary(pl.UTF-8):	Wtyczka do Cacti - NPC
Name:		cacti-plugin-npc
Version:	0.1.1a
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://forums.cacti.net/files/%{namesrc}-%{version}.tar.gz
# Source0-md5:	325f2e49070420346b55b7b4e2994d34
Patch0:		%{name}-path_headers.patch
# inserter.c patch for nagios 3.0b6 from http://forums.cacti.net/about10327-0-asc-150.html
#Patch1: http://forums.cacti.net/files/neb_159.patch
# from http://forums.cacti.net/about10327-0-asc-135.html
Patch1:		%{name}-extinfo.patch
URL:		http://forums.cacti.net/about10327
BuildRequires:	mysql-devel >= 4.1.0
BuildRequires:	nagios-devel >= 2.1
BuildRequires:	rpm-perlprov
Requires:	cacti >= 0.8.6h
Requires:	nagios >= 2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}
%define		pathtonagiosmodules	/usr/lib/nagios/modules

%description
Plugin for Cacti - A UI replacement for Nagios integrated into Cacti.

%description -l pl.UTF-8
Wtyczka do Cacti - zamiennik interfejsu użytkownika dla Nagiosa
zintegrowany z Cacti.

%prep
%setup -q -n %{namesrc}
%patch0 -p1
%patch1 -p1

%build
cd neb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
install -d $RPM_BUILD_ROOT%{pathtonagiosmodules}
install neb/inserter.o $RPM_BUILD_ROOT%{pathtonagiosmodules}
rm -rf neb
cp -a * $RPM_BUILD_ROOT%{webcactipluginroot}

# Edit nagios.cfg and set:
#
#        retain_state_information=0
#        event_broker_options=-1
#        broker_module=%{pathtonagiosmodules}/inserter.o

# Setting retain_state_information=0 causes all hosts and services to
# go to a pending state until rechecked by Nagios. Without this setting
# the inserter module will never update any data in NPC. Its a minor
# inconvenience that I will try to fix in the inserter module.

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README
%{webcactipluginroot}
%attr(755,root,root) %{pathtonagiosmodules}/inserter.o
