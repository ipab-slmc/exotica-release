%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-exotica-core
Version:        6.1.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS exotica_core package

License:        BSD
URL:            https://github.com/ipab-slmc/exotica
Source0:        %{name}-%{version}.tar.gz

Requires:       cppzmq-devel
Requires:       msgpack-devel
Requires:       orocos-kdl
Requires:       orocos-kdl-devel
Requires:       ros-noetic-eigen-conversions
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-kdl-parser
Requires:       ros-noetic-moveit-core
Requires:       ros-noetic-moveit-msgs
Requires:       ros-noetic-moveit-ros-planning
Requires:       ros-noetic-pluginlib
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-tf
Requires:       ros-noetic-tf-conversions
Requires:       tinyxml2-devel
BuildRequires:  cppzmq-devel
BuildRequires:  msgpack-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-cmake-modules
BuildRequires:  ros-noetic-eigen-conversions
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-kdl-parser
BuildRequires:  ros-noetic-moveit-core
BuildRequires:  ros-noetic-moveit-msgs
BuildRequires:  ros-noetic-moveit-ros-planning
BuildRequires:  ros-noetic-pluginlib
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-rosunit
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-tf
BuildRequires:  ros-noetic-tf-conversions
BuildRequires:  tinyxml2-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The Extensible Optimization Toolset (EXOTica) is a library for defining problems
for robot motion planning.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Mon Apr 05 2021 Vladimir Ivan <v.ivan@ed.ac.uk> - 6.1.1-1
- Autogenerated by Bloom

* Mon Mar 15 2021 Vladimir Ivan <v.ivan@ed.ac.uk> - 6.1.0-1
- Autogenerated by Bloom

* Tue Nov 24 2020 Vladimir Ivan <v.ivan@ed.ac.uk> - 6.0.2-1
- Autogenerated by Bloom

* Tue Nov 17 2020 Vladimir Ivan <v.ivan@ed.ac.uk> - 6.0.1-1
- Autogenerated by Bloom

* Mon Nov 09 2020 Vladimir Ivan <v.ivan@ed.ac.uk> - 6.0.0-1
- Autogenerated by Bloom

