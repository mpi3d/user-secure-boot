Name:           secureboot-keys
Version:        1
Release:        1
Summary:        Secure boot keys

License:        None
Source:         %{name}-%{version}.tar.xz

BuildArch:      noarch
Requires:       sbsigntools

%description
Secure boot keys from source

%prep
tar -xf %{_sourcedir}/%{name}-%{version}.tar.xz

%build

%install
dir=%{buildroot}/%{_datadir}/secureboot/keys
mkdir -p ${dir}
for key in PK KEK db; do
  mkdir ${dir}/${key}
  mv ${key}.{auth,crt,der,esl,key} ${dir}/${key}
done
mkdir ${dir}/dbx

%files
%{_datadir}/secureboot/keys

%changelog
* Fri Jun 30 2023 Matthieu CHARETTE
- Creation
