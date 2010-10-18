# Generated from racc-1.4.6.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname racc
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Racc is a LALR(1) parser generator
Name: rubygem-%{gemname}
Version: 1.4.6
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://racc.rubyforge.org/
Source0: http://gemcutter.orggems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: rubygems
BuildRequires: rubygems
Provides: rubygem(%{gemname}) = %{version}

%description
Racc is a LALR(1) parser generator. It is written in Ruby itself, and
generates Ruby program.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
mkdir -p ./%{gemdir}
mkdir -p %{buildroot}/%{_bindir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir ./%{gemdir} \
            --force --rdoc %{SOURCE0}
rm -rf ./%{gemdir}/ext/
rm -f ./%{gemdir}/{.autotest,.require_paths}
cp -a ./%{gemdir}/* %{buildroot}%{gemdir}
sed -i 's/\/usr\/local\/bin\/ruby/\/usr\/bin\/env ruby/' %{buildroot}/%{geminstdir}/bin/y2racc
sed -i 's/\/usr\/local\/bin\/ruby/\/usr\/bin\/env ruby/' %{buildroot}/%{geminstdir}/bin/racc2y
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/racc
%{_bindir}/racc2y
%{_bindir}/y2racc
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Oct 18 2010 : Sergio Rubio <rubiojr@frameos.org> - 1.4.6-2
- Fix shbang in bin scripts

* Mon Oct 18 2010 : Sergio Rubio <rubiojr@frameos.org> - 1.4.6-1
- Initial package
