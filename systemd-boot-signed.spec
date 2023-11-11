Name:           systemd-boot-signed
Version:        1
Release:        1
Summary:        systemd-boot signed binaries

License:        None

BuildArch:      noarch
Requires:       systemd-boot
Requires:       secureboot-keys

%description
Package to auto sign systemd-boot binaries

%prep

%build

%install

%transfiletriggerin -- %{_datadir}/secureboot/keys/db %{_exec_prefix}/lib/systemd/boot/efi
db=%{_datadir}/secureboot/keys/db
for file in %{_exec_prefix}/lib/systemd/boot/efi/*.efi; do
  sbsign --key ${db}/db.key --cert ${db}/db.crt ${file}
done

%files

%changelog
* Fri Jun 30 2023 Matthieu CHARETTE
- Creation
