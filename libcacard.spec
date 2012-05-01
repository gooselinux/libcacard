Name:           libcacard
Version:        0.1.2
Release:        2%{?dist}
Summary:        Common Access Card (CAC) Emulation
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.spice-space.org/download
Source0:        http://www.spice-space.org/download/libcacard/libcacard-%{version}.tar.bz2
BuildRequires:  nss-devel >= 3.12

ExclusiveArch:  i686 x86_64

%description
Common Access Card (CAC) emulation library.

%package tools
Summary:        CAC Emulation tools
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description tools
CAC emulation tools.

%package devel
Summary:        CAC Emulation devel
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
CAC emulation development files.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_libdir}/libcacard.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/cacard
%{_libdir}/pkgconfig/libcacard.pc
%{_libdir}/libcacard.so

%files tools
%defattr(-,root,root,-)
%{_bindir}/vscclient

%changelog
* Fri Feb 04 2011 Uri Lublin <uril@redhat.com> - 0.1.2-2
 - ExclusiveArch:  i686 x86_64
  Resolves: rhbz#663063

* Thu Feb 03 2011 Alon Levy <alevy@redhat.com> - 0.1.2-1
 - bump version to 0.1.2
 - style fixes
 - vscclient.c: fix tabulation
  - add copyright header
  - send init on connect, only start vevent thread on response
  - use hton,ntoh
  - read payload after header check, before type switch
  - update for vscard_common changes, empty Flush implementation
 - vcard_emul_nss: load coolkey in more situations
 - vscard_common.h:
  - VSCMsgInit capabilities and magic
  - VSCMsgReconnect stringified
  - define VSCARD_MAGIC
  - update copyright
  - fix message type enum
 - bump version to 0.1.1
  - vcard_emul,vcard_emul_nss
   - add VCARD_EMUL_INIT_ALREADY_INITED
   - add vcard_emul_replay_insertion_events
 - vreader: add vreader_queue_card_event
  Resolves: rhbz#663063

* Thu Dec 16 2010 Hans de Goede <hdegoede@redhat.com> - 0.1.0-5
- Build for RHEL-6
  Resolves: rhbz#663063

* Sun Dec 12 2010 Alon Levy <alevy@redhat.com> - 0.1.0-4
- address review issues:
 - Group for main and devel and tools
 - Requires for devel and tools
- fix changelog for previous entry (day was wrong, and macro quoting)
* Sat Dec 11 2010 Alon Levy <alevy@redhat.com> - 0.1.0-3
- address review issues: defattr typo, %%doc at %%files, remove .*a from install
* Thu Dec 9 2010 Alon Levy <alevy@redhat.com> - 0.1.0-2
- address prereview issues.
* Thu Dec 9 2010 Alon Levy <alevy@redhat.com> - 0.1.0-1
- initial package.

