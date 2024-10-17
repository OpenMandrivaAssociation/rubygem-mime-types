%define	oname	mime-types

Summary:	MIME content type identification library for ruby
Name:		rubygem-%{oname}
Version:	1.19
Release:	4
License:	GPLv2+ or Ruby or Perl Artistic License
Group:		Development/Ruby
URL:		https://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRequires:	ruby-RubyGems
Requires:	rubygem-hoe >= 1.8.3
Requires:	rubygem(simplecov)
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
gem install --local --install-dir %{buildroot}/%{gem_dir} --force %{SOURCE0}

rm -rf %{buildroot}%{gem_dir}/cache/%{oname}-%{version}.gem

%files
%doc %{gem_dir}/doc/%{oname}-%{version}
%{gem_dir}/gems/%{oname}-%{version}
%{gem_dir}/specifications/%{oname}-%{version}.gemspec



