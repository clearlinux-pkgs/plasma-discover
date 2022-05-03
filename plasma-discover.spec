#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : plasma-discover
Version  : 5.24.5
Release  : 58
URL      : https://download.kde.org/stable/plasma/5.24.5/discover-5.24.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.24.5/discover-5.24.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.24.5/discover-5.24.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: plasma-discover-bin = %{version}-%{release}
Requires: plasma-discover-data = %{version}-%{release}
Requires: plasma-discover-lib = %{version}-%{release}
Requires: plasma-discover-license = %{version}-%{release}
Requires: plasma-discover-locales = %{version}-%{release}
BuildRequires : appstream-dev
BuildRequires : appstream-extras
BuildRequires : attica-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : flatpak-dev
BuildRequires : ki18n-dev
BuildRequires : kidletime-dev
BuildRequires : kirigami2-dev
BuildRequires : knewstuff-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(flatpak)
BuildRequires : pkgconfig(ostree-1)
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the plasma-discover package.
Group: Binaries
Requires: plasma-discover-data = %{version}-%{release}
Requires: plasma-discover-license = %{version}-%{release}

%description bin
bin components for the plasma-discover package.


%package data
Summary: data components for the plasma-discover package.
Group: Data

%description data
data components for the plasma-discover package.


%package lib
Summary: lib components for the plasma-discover package.
Group: Libraries
Requires: plasma-discover-data = %{version}-%{release}
Requires: plasma-discover-license = %{version}-%{release}

%description lib
lib components for the plasma-discover package.


%package license
Summary: license components for the plasma-discover package.
Group: Default

%description license
license components for the plasma-discover package.


%package locales
Summary: locales components for the plasma-discover package.
Group: Default

%description locales
locales components for the plasma-discover package.


%prep
%setup -q -n discover-5.24.5
cd %{_builddir}/discover-5.24.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651621166
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1651621166
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-discover
cp %{_builddir}/discover-5.24.5/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/plasma-discover/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/discover-5.24.5/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-discover/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/discover-5.24.5/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-discover/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/discover-5.24.5/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-discover/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/discover-5.24.5/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma-discover/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/discover-5.24.5/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/plasma-discover/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/discover-5.24.5/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/plasma-discover/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/discover-5.24.5/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-discover/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/discover-5.24.5/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/plasma-discover/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/discover-5.24.5/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-discover/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/discover-5.24.5/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/plasma-discover/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/discover-5.24.5/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/plasma-discover/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
pushd clr-build
%make_install
popd
%find_lang kcm_updates
%find_lang libdiscover
%find_lang plasma-discover-notifier
%find_lang plasma-discover

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/DiscoverNotifier

%files bin
%defattr(-,root,root,-)
/usr/bin/plasma-discover
/usr/bin/plasma-discover-update

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.discover-flatpak.desktop
/usr/share/applications/org.kde.discover.desktop
/usr/share/applications/org.kde.discover.notifier.desktop
/usr/share/applications/org.kde.discover.snap.desktop
/usr/share/applications/org.kde.discover.urlhandler.desktop
/usr/share/icons/hicolor/128x128/apps/plasmadiscover.png
/usr/share/icons/hicolor/16x16/apps/plasmadiscover.png
/usr/share/icons/hicolor/22x22/apps/plasmadiscover.png
/usr/share/icons/hicolor/32x32/apps/plasmadiscover.png
/usr/share/icons/hicolor/48x48/apps/plasmadiscover.png
/usr/share/icons/hicolor/scalable/apps/flatpak-discover.svg
/usr/share/icons/hicolor/scalable/apps/plasmadiscover.svg
/usr/share/knotifications5/discoverabstractnotifier.notifyrc
/usr/share/kpackage/kcms/kcm_updates/contents/ui/main.qml
/usr/share/kxmlgui5/plasmadiscover/plasmadiscoverui.rc
/usr/share/libdiscover/categories/flatpak-backend-categories.xml
/usr/share/metainfo/org.kde.discover.appdata.xml
/usr/share/metainfo/org.kde.discover.flatpak.appdata.xml
/usr/share/qlogging-categories5/discover.categories
/usr/share/xdg/autostart/org.kde.discover.notifier.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/plasma-discover/libDiscoverCommon.so
/usr/lib64/plasma-discover/libDiscoverNotifiers.so
/usr/lib64/qt5/plugins/discover-notifier/FlatpakNotifier.so
/usr/lib64/qt5/plugins/discover/flatpak-backend.so
/usr/lib64/qt5/plugins/discover/kns-backend.so
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings/kcm_updates.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-discover/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/plasma-discover/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/plasma-discover/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/plasma-discover/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/plasma-discover/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/plasma-discover/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/plasma-discover/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/plasma-discover/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/plasma-discover/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/plasma-discover/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kcm_updates.lang -f libdiscover.lang -f plasma-discover-notifier.lang -f plasma-discover.lang
%defattr(-,root,root,-)

