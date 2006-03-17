%define		namesrc	npc
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - NPC
Summary(pl):	Wtyczka do Cacti - NPC
Name:		cacti-plugin-npc
Version:	0.1.1a
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.divagater.com/npc/%{namesrc}-%{version}.tar.gz
# Source0-md5:	325f2e49070420346b55b7b4e2994d34
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - A UI replacement for Nagios integrated into Cacti.

%description -l pl
Wtyczka do Cacti - 

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README 
%{webcactipluginroot}
