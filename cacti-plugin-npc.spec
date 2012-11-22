# TODO
# - bundles Doctrine 1.0.7: use system phpdoctrine.spec
# - bundles Ext JS Library 2.2
# - forum thread: http://forums.cacti.net/viewtopic.php?t=26540
%define		plugin	npc
%define		php_min_version 5.2.1
%include	/usr/lib/rpm/macros.php
Summary:	Nagios Plugin for Cacti (NPC)
Summary(pl.UTF-8):	Wtyczka do Cacti - NPC
Name:		cacti-plugin-npc
Version:	2.0.4
Release:	0.4
License:	GPL v3
Group:		Applications/WWW
#Source0:	http://downloads.sourceforge.net/gibtmirdas/npc-%{version}.tar.gz
Source0:	npc-%{version}.tar.gz
# Source0-md5:	7b30302c544f10ed73cff406fda14499
URL:		https://trac.assembla.com/npc/
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	cacti >= 0.8.7b
Requires:	cacti(pia) >= 2.0
Requires:	nagios >= 3.0
Requires:	nagios-ndoutils >= 1.4b7
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(iconv)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(mysql)
Requires:	php(mysqli)
Requires:	php(pcre)
Requires:	php(session)
Requires:	php(simplexml)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}
%define		moduledir		%{_libdir}/nagios/modules

%define		_noautoreq pear

%description
The purpose of NPC is to be a complete web based UI replacement to
Nagios while fully integrating into Cacti using the Cacti Plugin
Architecture. This integration will provide a single point of access
for trending and alert monitoring.

%description -l pl.UTF-8
Wtyczka do Cacti - zamiennik interfejsu użytkownika dla Nagiosa
zintegrowany z Cacti.

%prep
%setup -qc
mv %{plugin}/*.debug .
mv %{plugin}/build.xml .
mv %{plugin}/{README,LICENSE} .
%undos -f php README

# dev code, not needed for production functionality
cd %{plugin}
%{__rm} controllers/layoutDev.php
%{__rm} -r js/src
%{__rm} js/ext/*-debug.js
%{__rm} js/ext/resources/resources.jsb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{plugindir}
%attr(755,root,root) %{plugindir}/cli.php
%attr(755,root,root) %{plugindir}/perfdata.php
%{plugindir}/config.php
%{plugindir}/index.php
%{plugindir}/nagioscmd.php
%{plugindir}/npc.php
%{plugindir}/setup.php
%{plugindir}/top_graph_header.php
%{plugindir}/upgrade_schema.sql
%{plugindir}/controllers
%{plugindir}/css
%{plugindir}/images
%{plugindir}/js
%{plugindir}/lib
%{plugindir}/models
%{plugindir}/queries
