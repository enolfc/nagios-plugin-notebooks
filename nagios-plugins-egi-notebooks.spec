#
# nagios-plugins-egi-notebooks RPM
#

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define dir /usr/libexec/argo-monitoring/probes/eu.egi.notebooks

Summary: Nagios plugin for EGI notebooks
Name: nagios-plugins-egi-notebooks
Version: 0.2.2
Release: 1%{?dist}
Group: Applications/Internet
License: ASL 2.0
URL: https://github.com/EGI-Foundation/nagios-plugin-notebooks
Source: nagios_plugins_egi_notebooks-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-setuptools
BuildRequires: python-pbr
Requires: python
Requires: python-requests
Requires: python-argparse
# This is to enable SNI in python < 2.7.9
Requires: pyOpenSSL
Requires: python2-ndg_httpsclient
BuildArch: noarch

%description
Nagios plugins for monitoring EGI notebooks

%prep
%setup -q -n nagios_plugins_egi_notebooks-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT --install-scripts %{dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/nagios_plugins_egi_notebooks*
%{dir}

%changelog
* Tue Nov 13 2018 Enol Fernandez <enol.fernandez@egi.eu> 0.2.2-1%{dist}
- Add dependencies for SNI support
* Fri Aug 17 2018 Enol Fernandez <enol.fernandez@egi.eu> 0.2.1-1%{dist}
- Improve build to build from tar
* Thu Aug 16 2018 Enol Fernandez <enol.fernandez@egi.eu> 0.2.0-1%{dist}
- Adapt to ARGO probes requirements
* Fri Jul 20 2018 Enol Fernandez <enol.fernandez@egi.eu> 0.1.0
- Initial release (Enol Fernandez)

