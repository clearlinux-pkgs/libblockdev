#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libblockdev
Version  : 2.21.1
Release  : 30
URL      : https://github.com/storaged-project/libblockdev/releases/download/2.21-1/libblockdev-2.21.tar.gz
Source0  : https://github.com/storaged-project/libblockdev/releases/download/2.21-1/libblockdev-2.21.tar.gz
Summary  : A library for low-level manipulation with block devices
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: libblockdev-bin = %{version}-%{release}
Requires: libblockdev-data = %{version}-%{release}
Requires: libblockdev-lib = %{version}-%{release}
Requires: libblockdev-license = %{version}-%{release}
Requires: libblockdev-python = %{version}-%{release}
Requires: libblockdev-python3 = %{version}-%{release}
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : nss-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(bytesize)
BuildRequires : pkgconfig(devmapper)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libcryptsetup)
BuildRequires : pkgconfig(libkmod)
BuildRequires : pkgconfig(libndctl)
BuildRequires : pkgconfig(libparted)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(mount)
BuildRequires : pkgconfig(uuid)
BuildRequires : pkgconfig(yaml-0.1)
BuildRequires : python-dev
BuildRequires : volume_key-dev

%description
The libblockdev is a C library with GObject introspection support that can be
used for doing low-level operations with block devices like setting up LVM,
BTRFS, LUKS or MD RAID. The library uses plugins (LVM, BTRFS,...) and serves as
a thin wrapper around its plugins' functionality. All the plugins, however, can
be used as standalone libraries. One of the core principles of libblockdev is
that it is stateless from the storage configuration's perspective (e.g. it has
no information about VGs when creating an LV).

%package bin
Summary: bin components for the libblockdev package.
Group: Binaries
Requires: libblockdev-data = %{version}-%{release}
Requires: libblockdev-license = %{version}-%{release}

%description bin
bin components for the libblockdev package.


%package data
Summary: data components for the libblockdev package.
Group: Data

%description data
data components for the libblockdev package.


%package dev
Summary: dev components for the libblockdev package.
Group: Development
Requires: libblockdev-lib = %{version}-%{release}
Requires: libblockdev-bin = %{version}-%{release}
Requires: libblockdev-data = %{version}-%{release}
Provides: libblockdev-devel = %{version}-%{release}
Requires: libblockdev = %{version}-%{release}

%description dev
dev components for the libblockdev package.


%package legacypython
Summary: legacypython components for the libblockdev package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the libblockdev package.


%package lib
Summary: lib components for the libblockdev package.
Group: Libraries
Requires: libblockdev-data = %{version}-%{release}
Requires: libblockdev-license = %{version}-%{release}

%description lib
lib components for the libblockdev package.


%package license
Summary: license components for the libblockdev package.
Group: Default

%description license
license components for the libblockdev package.


%package python
Summary: python components for the libblockdev package.
Group: Default
Requires: libblockdev-python3 = %{version}-%{release}

%description python
python components for the libblockdev package.


%package python3
Summary: python3 components for the libblockdev package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libblockdev package.


%prep
%setup -q -n libblockdev-2.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555365675
export LDFLAGS="${LDFLAGS} -fno-lto"
%configure --disable-static --with-dm=no
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1555365675
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libblockdev
cp LICENSE %{buildroot}/usr/share/package-licenses/libblockdev/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lvm-cache-stats

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/BlockDev-2.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/blockdev/blockdev.h
/usr/include/blockdev/btrfs.h
/usr/include/blockdev/crypto.h
/usr/include/blockdev/dbus.h
/usr/include/blockdev/dev_utils.h
/usr/include/blockdev/exec.h
/usr/include/blockdev/extra_arg.h
/usr/include/blockdev/fs.h
/usr/include/blockdev/fs/ext.h
/usr/include/blockdev/fs/generic.h
/usr/include/blockdev/fs/mount.h
/usr/include/blockdev/fs/ntfs.h
/usr/include/blockdev/fs/vfat.h
/usr/include/blockdev/fs/xfs.h
/usr/include/blockdev/kbd.h
/usr/include/blockdev/loop.h
/usr/include/blockdev/lvm.h
/usr/include/blockdev/mdraid.h
/usr/include/blockdev/module.h
/usr/include/blockdev/mpath.h
/usr/include/blockdev/nvdimm.h
/usr/include/blockdev/part.h
/usr/include/blockdev/plugins.h
/usr/include/blockdev/sizes.h
/usr/include/blockdev/swap.h
/usr/include/blockdev/utils.h
/usr/include/blockdev/vdo.h
/usr/lib64/libbd_btrfs.so
/usr/lib64/libbd_crypto.so
/usr/lib64/libbd_fs.so
/usr/lib64/libbd_kbd.so
/usr/lib64/libbd_loop.so
/usr/lib64/libbd_lvm-dbus.so
/usr/lib64/libbd_lvm.so
/usr/lib64/libbd_mdraid.so
/usr/lib64/libbd_mpath.so
/usr/lib64/libbd_nvdimm.so
/usr/lib64/libbd_part.so
/usr/lib64/libbd_part_err.so
/usr/lib64/libbd_swap.so
/usr/lib64/libbd_utils.so
/usr/lib64/libbd_vdo.so
/usr/lib64/libblockdev.so
/usr/lib64/pkgconfig/blockdev-utils.pc
/usr/lib64/pkgconfig/blockdev.pc

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbd_btrfs.so.2
/usr/lib64/libbd_btrfs.so.2.0.0
/usr/lib64/libbd_crypto.so.2
/usr/lib64/libbd_crypto.so.2.0.0
/usr/lib64/libbd_fs.so.2
/usr/lib64/libbd_fs.so.2.0.0
/usr/lib64/libbd_kbd.so.2
/usr/lib64/libbd_kbd.so.2.0.0
/usr/lib64/libbd_loop.so.2
/usr/lib64/libbd_loop.so.2.0.0
/usr/lib64/libbd_lvm-dbus.so.2
/usr/lib64/libbd_lvm-dbus.so.2.0.0
/usr/lib64/libbd_lvm.so.2
/usr/lib64/libbd_lvm.so.2.0.0
/usr/lib64/libbd_mdraid.so.2
/usr/lib64/libbd_mdraid.so.2.0.0
/usr/lib64/libbd_mpath.so.2
/usr/lib64/libbd_mpath.so.2.0.0
/usr/lib64/libbd_nvdimm.so.2
/usr/lib64/libbd_nvdimm.so.2.0.0
/usr/lib64/libbd_part.so.2
/usr/lib64/libbd_part.so.2.0.0
/usr/lib64/libbd_part_err.so.2
/usr/lib64/libbd_part_err.so.2.0.0
/usr/lib64/libbd_swap.so.2
/usr/lib64/libbd_swap.so.2.0.0
/usr/lib64/libbd_utils.so.2
/usr/lib64/libbd_utils.so.2.1.0
/usr/lib64/libbd_vdo.so.2
/usr/lib64/libbd_vdo.so.2.0.0
/usr/lib64/libblockdev.so.2
/usr/lib64/libblockdev.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libblockdev/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
