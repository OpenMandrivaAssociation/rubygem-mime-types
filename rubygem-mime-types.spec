%define	oname	mime-types

Summary:	MIME content type identification library for ruby
Name:		rubygem-%{oname}
Version:	1.16
Release:	%mkrel 4
License:	GPLv2+ or Ruby or Perl Artistic License
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	rubygem-hoe >= 1.8.3 ruby-rcov rubygem-nokogiri
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

