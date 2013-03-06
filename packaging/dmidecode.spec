Name:           dmidecode
Url:            http://www.nongnu.org/dmidecode/
Version:        2.11
Release:        0
License:        GPL-2.0+
Group:          System/Base
Summary:        DMI table decoder
Source:         %{name}-%{version}.tar.bz2
ExclusiveArch:  %ix86 x86_64

%description
Dmidecode reports information about your system's hardware as described
in your system BIOS according to the SMBIOS/DMI standard. This
information typically includes system manufacturer, model name, serial
number, BIOS version, asset tag as well as a lot of other details of
varying level of interest and reliability depending on the
manufacturer. This will often include usage status for the CPU sockets,
expansion slots (e.g. AGP, PCI, ISA) and memory module slots, and the
list of I/O ports (e.g. serial, parallel, USB).

Beware that DMI data have proven to be too unreliable to be blindly
trusted. Dmidecode does not scan your hardware, it only reports what
the BIOS told it to.

%prep
%setup

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
install -dm 755 %{buildroot}/usr/sbin
install -dm 755 %{buildroot}%{_mandir}/man8
install -dm 755 %{buildroot}%{_docdir}/%{name}
for i in dmidecode vpddecode ownership biosdecode ; do
install -m 755 $i %{buildroot}/usr/sbin/
install -m 644 man/$i.8 %{buildroot}%{_mandir}/man8/
done

%files
%defattr(-,root,root)
%license LICENSE
/usr/sbin/*
/%{_mandir}/man8/*

%changelog
