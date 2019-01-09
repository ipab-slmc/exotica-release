Name:           ros-melodic-exotica-core-task-maps
Version:        5.0.0
Release:        0%{?dist}
Summary:        ROS exotica_core_task_maps package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/ipab-slmc/exotica
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-exotica-core
Requires:       ros-melodic-exotica-python
Requires:       ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-exotica-core
BuildRequires:  ros-melodic-exotica-python
BuildRequires:  ros-melodic-geometry-msgs

%description
Common taskmaps provided with EXOTica.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Jan 09 2019 Vladimir Ivan <v.ivan@ed.ac.uk> - 5.0.0-0
- Autogenerated by Bloom

