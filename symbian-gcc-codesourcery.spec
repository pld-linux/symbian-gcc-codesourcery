#
# TODO: recompile sources instead of redistributing binaries?
#
Summary:	GNU Toolchain for ARM Processors
Summary(pl.UTF-8):	Zestaw narzędzi GNU dla procesorów ARM
Name:		symbian-gcc-codesourcery
Version:	2005Q1C
Release:	1
License:	GPL
Group:		Developement
# http://www.codesourcery.com/gnu_toolchains/arm/download.html
Source0:	http://www.codesourcery.com/public/gnu_toolchain/arm-none-symbianelf/gnu-csl-arm-2005Q1C-arm-none-symbianelf-i686-pc-linux-gnu.tar.bz2
# Source0-md5:	622e4db70cfae6a9eec26892a9932633
URL:		http://www.codesourcery.com/gnu_toolchains/arm
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CodeSourcery, in partnership with ARM, Ltd., develops improvements to
the GNU Toolchain for ARM processors and provides regular, validated
releases of the GNU Toolchain. Sourcery G++ Lite Edition supports ARM,
Thumb, and Thumb-2 compilation for all architectures in active use,
including Version 7 of the ARM Architecture.

%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}

cp -r arm-none-symbianelf $RPM_BUILD_ROOT%{_prefix}/
cp -r bin/* $RPM_BUILD_ROOT%{_bindir}
cp -r lib/gcc $RPM_BUILD_ROOT%{_libdir}
cp libexec/gcc/arm-none-symbianelf/3.4.3/c* $RPM_BUILD_ROOT%{_prefix}/arm-none-symbianelf/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/gcc/arm-none-symbianelf
%dir %{_prefix}/arm-none-symbianelf
%dir %{_prefix}/arm-none-symbianelf/bin
%attr(755,root,root) %{_prefix}/arm-none-symbianelf/bin/*
%{_prefix}/arm-none-symbianelf/lib
