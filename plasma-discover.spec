#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : plasma-discover
Version  : 5.17.2
Release  : 17
URL      : https://download.kde.org/stable/plasma/5.17.2/discover-5.17.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.17.2/discover-5.17.2.tar.xz
Source1 : https://download.kde.org/stable/plasma/5.17.2/discover-5.17.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-3.0 LGPL-2.1
Requires: plasma-discover-bin = %{version}-%{release}
Requires: plasma-discover-data = %{version}-%{release}
Requires: plasma-discover-lib = %{version}-%{release}
Requires: plasma-discover-license = %{version}-%{release}
Requires: plasma-discover-locales = %{version}-%{release}
BuildRequires : appstream-dev
BuildRequires : appstream-extras
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : flatpak-dev
BuildRequires : kirigami2-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(flatpak)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : util-linux

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
%setup -q -n discover-5.17.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572442615
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1572442615
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-discover
cp %{_builddir}/discover-5.17.2/COPYING %{buildroot}/usr/share/package-licenses/plasma-discover/65aec5a8ccb6ecc51d700c66d290ce66f0a5e9f7
cp %{_builddir}/discover-5.17.2/COPYING.GFDL %{buildroot}/usr/share/package-licenses/plasma-discover/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/discover-5.17.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/plasma-discover/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd clr-build
%make_install
popd
%find_lang libdiscover
%find_lang plasma-discover-notifier
%find_lang plasma-discover

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/DiscoverNotifier

%files bin
%defattr(-,root,root,-)
/usr/bin/plasma-discover

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.discover-flatpak.desktop
/usr/share/applications/org.kde.discover.desktop
/usr/share/applications/org.kde.discover.notifier.desktop
/usr/share/applications/org.kde.discover.snap.urlhandler.desktop
/usr/share/applications/org.kde.discover.urlhandler.desktop
/usr/share/icons/hicolor/128x128/apps/plasmadiscover.png
/usr/share/icons/hicolor/16x16/apps/plasmadiscover.png
/usr/share/icons/hicolor/22x22/apps/plasmadiscover.png
/usr/share/icons/hicolor/32x32/apps/plasmadiscover.png
/usr/share/icons/hicolor/48x48/apps/plasmadiscover.png
/usr/share/icons/hicolor/scalable/apps/flatpak-discover.svg
/usr/share/icons/hicolor/scalable/apps/plasmadiscover.svgz
/usr/share/knotifications5/discoverabstractnotifier.notifyrc
/usr/share/knsrcfiles/discover_ktexteditor_codesnippets_core.knsrc
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-discover/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/plasma-discover/65aec5a8ccb6ecc51d700c66d290ce66f0a5e9f7
/usr/share/package-licenses/plasma-discover/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f libdiscover.lang -f plasma-discover-notifier.lang -f plasma-discover.lang
%defattr(-,root,root,-)

