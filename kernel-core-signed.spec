Name:           kernel-core-signed
Version:        1
Release:        1
Summary:        kernel-core signed binaries

License:        None

BuildArch:      noarch
Requires:       kernel-core
Requires:       secureboot-keys

%description
Package to auto sign kernel-core binaries

%prep

%build

%install

%transfiletriggerin -- %{_datadir}/secureboot/keys/db %{_exec_prefix}/lib/modules
db=%{_datadir}/secureboot/keys/db
for file in %{_exec_prefix}/lib/modules/*/vmlinuz; do
  dir=$(dirname ${file})
  cd ${dir}
  ver=$(basename ${file})-$(basename ${dir})
  sbsign --output ${ver} --key ${db}/db.key --cert ${db}/db.crt ${file}
  sha512hmac ${ver} > .vmlinuz.hmac
  mv ${ver} ${file}
done

%files

%changelog
* Fri Jun 30 2023 Matthieu CHARETTE
- Creation
