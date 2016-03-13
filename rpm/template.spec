Name:           ros-indigo-mm-mux-demux
Version:        0.2.3
Release:        0%{?dist}
Summary:        ROS mm_mux_demux package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ecl-build
Requires:       ros-indigo-ecl-command-line
Requires:       ros-indigo-ecl-containers
Requires:       ros-indigo-ecl-formatters
Requires:       ros-indigo-ecl-threads
Requires:       ros-indigo-ecl-time
Requires:       ros-indigo-ecl-utilities
Requires:       ros-indigo-mm-core-msgs
Requires:       ros-indigo-mm-messages
Requires:       ros-indigo-nanomsg
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-build
BuildRequires:  ros-indigo-ecl-command-line
BuildRequires:  ros-indigo-ecl-containers
BuildRequires:  ros-indigo-ecl-formatters
BuildRequires:  ros-indigo-ecl-threads
BuildRequires:  ros-indigo-ecl-time
BuildRequires:  ros-indigo-ecl-utilities
BuildRequires:  ros-indigo-mm-core-msgs
BuildRequires:  ros-indigo-mm-messages
BuildRequires:  ros-indigo-nanomsg

%description
Multiplexing many packet types across a single connection. Great for embedded
connections by serial or ethernet types.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Mar 13 2016 Daniel Stonier <d.stonier@gmail.com> - 0.2.3-0
- Autogenerated by Bloom

* Sat Feb 28 2015 Daniel Stonier <d.stonier@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

* Wed Sep 17 2014 Daniel Stonier <d.stonier@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

* Sun Sep 14 2014 Daniel Stonier <d.stonier@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

