Name:           edk2-ext4-signed
Version:        1
Release:        1%{?dist}
Summary:        edk2-ext4 signed binaries

License:        None

BuildArch:      noarch
Requires:       edk2-ext4
Requires:       secureboot-keys

%description
Package to auto sign edk2-ext4 binaries

%prep

%build

%install

%transfiletriggerin -- %{_datadir}/secureboot/keys/db %{_datadir}/edk2/drivers
db=%{_datadir}/secureboot/keys/db
for file in %{_datadir}/edk2/drivers/*.efi; do
  sbsign --key ${db}/db.key --cert ${db}/db.crt ${file}
done

%files

%changelog
* Fri Jun 30 2023 Matthieu CHARETTE
- Creation
