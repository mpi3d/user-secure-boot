Name:           secureboot-keys
Version:        1
Release:        1
Summary:        Secure boot keys

License:        None

BuildArch:      noarch
BuildRequires:  systemd
BuildRequires:  openssl
BuildRequires:  sbsigntools
Requires:       sbsigntools

%description
Secure boot keys generated at build time

%prep

%build
uuid=$(systemd-id128 new --uuid)
openssl req -new -x509 -subj "/CN=Platform Key/" -keyout PK.key -out PK.crt -noenc
openssl req -new -x509 -subj "/CN=Key Exchange Key/" -keyout KEK.key -out KEK.crt -noenc
openssl req -new -x509 -subj "/CN=Signature Database/" -keyout db.key -out db.crt -noenc
for key in PK KEK db; do
  openssl x509 -outform DER -in ${key}.crt -out ${key}.der
  sbsiglist --owner ${uuid} --type x509 --output ${key}.esl ${key}.der
done
attr=NON_VOLATILE,RUNTIME_ACCESS,BOOTSERVICE_ACCESS,TIME_BASED_AUTHENTICATED_WRITE_ACCESS
sbvarsign --attr ${attr} --key PK.key --cert PK.crt --output PK.auth PK PK.esl
sbvarsign --attr ${attr} --key PK.key --cert PK.crt --output KEK.auth KEK KEK.esl
sbvarsign --attr ${attr} --key KEK.key --cert KEK.crt --output db.auth db db.esl

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
