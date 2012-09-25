Summary: Demonstration software
Name: cgbuddy
Version: 1.0
Release: 1
License: Freely redistributable without restriction
Group: Applications/Productivity
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libcgroup

%description
cgbuddy is a libcgroup GUI example program

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/{bin,lib,share/man/man1}
install cgbuddy $RPM_BUILD_ROOT/usr/local/bin
gzip -9c cgbuddy.1 > cgbuddy.1.gz
install cgbuddy.1.gz $RPM_BUILD_ROOT/usr/local/share/man/man1

%clean
make clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/local/bin/cgbuddy
%doc /usr/local/share/man/man1/cgbuddy.1.gz


%post


%changelog
* Tue May 10 2010 Bob Kozdemba <koz@redhat.com> - 1.0-0
- Initial build.
