Name:           fwupd-efi-signed
Version:        1
Release:        1
Summary:        fwupd-efi signed binaries

License:        None

BuildArch:      noarch
Requires:       fwupd-efi
Requires:       secureboot-keys

%description
Package to auto sign fwupd-efi binaries

%prep

%build

%install

%transfiletriggerin -- %{_datadir}/secureboot/keys/db %{_libexecdir}/fwupd/efi
db=%{_datadir}/secureboot/keys/db
for file in %{_libexecdir}/fwupd/efi/*.efi; do
  sbsign --key ${db}/db.key --cert ${db}/db.crt ${file}
done

%files

%changelog
* Fri Jun 30 2023 Matthieu CHARETTE
- Creation
