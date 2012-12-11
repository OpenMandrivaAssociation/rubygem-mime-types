%define	oname	mime-types

Summary:	MIME content type identification library for ruby
Name:		rubygem-%{oname}
Version:	1.16
Release:	5
License:	GPLv2+ or Ruby or Perl Artistic License
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRequires:	ruby-RubyGems
Requires:	rubygem-hoe >= 1.8.3
Requires:	rubygem(rcov)
Requires:	rubygem-nokogiri
Requires:	rubygem-archive-tar-minitar
BuildArch:	noarch

%description
This ruby library allows for the identification of a file's likely MIME content
type. The identification of MIME content type is based on a file's filename
extensions.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache/%{oname}-%{version}.gem

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec



%changelog
* Wed Dec 15 2010 Rémy Clouard <shikamaru@mandriva.org> 1.16-4mdv2011.0
+ Revision: 622186
- rebuild for new rpm-mandriva-setup

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.16-3mdv2011.0
+ Revision: 614773
- the mass rebuild of 2010.1 packages

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.16-2mdv2010.1
+ Revision: 500515
- don't ship gem with package
- fix dependencies

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.16-1mdv2010.1
+ Revision: 500416
- fix license
- import rubygem-mime-types


* Mon Feb  3 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.16-1
- initial release
