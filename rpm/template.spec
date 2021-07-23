%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-exotica-cartpole-dynamics-solver
Version:        6.2.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS exotica_cartpole_dynamics_solver package

License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-exotica-core
Requires:       ros-noetic-roscpp
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-exotica-core
BuildRequires:  ros-noetic-exotica-python
BuildRequires:  ros-noetic-roscpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Cartpole dynamics solver plug-in for Exotica

%prep
%autosetup -p1

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
* Fri Jul 23 2021 Traiko Dinev <traiko.dinev@ed.ac.uk> - 6.2.0-1
- Autogenerated by Bloom

* Mon Apr 05 2021 Traiko Dinev <traiko.dinev@ed.ac.uk> - 6.1.1-1
- Autogenerated by Bloom

* Mon Mar 15 2021 Traiko Dinev <traiko.dinev@ed.ac.uk> - 6.1.0-1
- Autogenerated by Bloom

* Tue Nov 24 2020 Traiko Dinev <traiko.dinev@ed.ac.uk> - 6.0.2-1
- Autogenerated by Bloom

* Tue Nov 17 2020 Traiko Dinev <traiko.dinev@ed.ac.uk> - 6.0.1-1
- Autogenerated by Bloom

* Mon Nov 09 2020 Traiko Dinev <traiko.dinev@ed.ac.uk> - 6.0.0-1
- Autogenerated by Bloom

