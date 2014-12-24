#
# spec file for package libvpu-imx6
#
# Copyright (c) 2014 Josua Mayer <privacy@not.given>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

Name: libvpu-imx6
Version: 1
Release: 1
License: Freescale IP
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
%doc imx-vpu-3.10.17-1.0.0/vpu/EULA.txt

%files devel
%defattr(-,root,root)
/usr/lib/*.so
/usr/lib/*.a
/usr/include/*.h

%changelog

