Name:           plasma-applet-wifi
Summary:        Plasma applet that allow to look your wifi signal strengh
Version:        0.5
Release:        %mkrel 3
Url:            http://www.kde-look.org/content/show.php/Plasma+WiFi?content=79476 
License:        GPLv2+
Group:          Graphical desktop/KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        79476-plasma-wifi-%version.tgz
Patch0:         plasma-wifi-fix-cmake.patch
# Fix categories according to http://techbase.kde.org/Projects/Plasma/PIG#Category_Names
Patch1:         plasma-wifi-fix-categories.patch
BuildRequires:  plasma-devel

%description
Plasma applet that allow to look your wifi signal strengh.

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_wifi_signal.so
%_kde_appsdir/desktoptheme/default/widgets/*
%_kde_datadir/kde4/services/plasma-wifi-signal-default.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n plasma-wifi-%version 
%patch0 -p1
%patch1 -p0

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
%{__rm} -rf "%{buildroot}"
