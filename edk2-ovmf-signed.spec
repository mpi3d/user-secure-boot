Name:           edk2-ovmf-signed
Version:        1
Release:        1%{?dist}
Summary:        edk2-ovmf signed binaries

License:        None

BuildArch:      noarch
Requires:       edk2-ovmf
Requires:       secureboot-keys

%description
Package to auto sign edk2-ovmf binaries

%prep

%build

%install

%transfiletriggerin -- %{_datadir}/secureboot/keys/db %{_datadir}/edk2/ovmf
db=%{_datadir}/secureboot/keys/db
for file in %{_datadir}/edk2/ovmf/*.efi; do
  sbsign --key ${db}/db.key --cert ${db}/db.crt ${file}
done

%files

%changelog
* Fri Jun 30 2023 Matthieu CHARETTE
- Creation
