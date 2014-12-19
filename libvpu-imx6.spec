Name: libvpu-imx6
Version: 1
Release: 1
License: TODO
Group: Productivity/Multimedia/Other
Summary: Freescale i.MX VPU library
Source: %{name}-%{version}.tar.gz
Source1: imx-vpu-3.10.17-1.0.0.bin
Source10: rpmlintrc
Requires: firmware-imx6

%description
Provides access to the VPU in i.MX CPUs

%package devel
Group: Development/Libraries/C and C++
Summary: Development Files for libvpu
Requires: %{name} = %{version}-%{release}
%description devel
Provides Development files for building against Freescale's VPU library.

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%prep
%setup -q
chmod +x %{SOURCE1}
%{SOURCE1} --auto-accept --force

%build
make -C imx-vpu-3.10.17-1.0.0 PLATFORM=IMX6Q

%install
make -C imx-vpu-3.10.17-1.0.0 install DEST_DIR=%{buildroot}

%files
%defattr(-,root,root)
/usr/lib/*.so.*

%files devel
%defattr(-,root,root)
/usr/lib/*.so
/usr/lib/*.a
/usr/include/*.h

%changelog

