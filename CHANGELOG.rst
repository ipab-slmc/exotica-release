^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package exotica_python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

6.2.0 (2021-07-23)
------------------
* Trajectory from array in python (`#743 <https://github.com/ipab-slmc/exotica/issues/743>`_)
* Add EndPoseTask::GetTaskJacobian
* Fix build issues with Eigen 3.3.9 (`#740 <https://github.com/ipab-slmc/exotica/issues/740>`_)
* Performance improvements (`#741 <https://github.com/ipab-slmc/exotica/issues/741>`_)
* Remove temporary workaround, formatting
* Contributors: Vladimir Ivan, Wolfgang Merkt

6.1.1 (2021-04-05)
------------------
* Fixes for Python 3 and newly exposed features (`#736 <https://github.com/ipab-slmc/exotica/issues/736>`_)
  * Fix issues identified by static analysis
  * Expose EndPoseTask::GetS
  * Remove transformations.py (usage replaced by exo.KDLFrame)
  * Install convert_moveit_scene_to_sdf & remove use of transformations.py
  * SamplingProblem: Rename IsValid(q) to IsStateValid(q)
* Python 3 fixes
* Contributors: Wolfgang Merkt

6.1.0 (2021-03-15)
------------------
* Fix segmentation fault on exiting Python (`#732 <https://github.com/ipab-slmc/exotica/issues/732>`_)
* Upgrade clang format from v3.9 to v6.0 (`#730 <https://github.com/ipab-slmc/exotica/issues/730>`_)
* Contributors: Wolfgang Merkt

6.0.2 (2020-11-23)
------------------

6.0.1 (2020-11-17)
------------------
* Fix some SparseDDP examples and remove old ones (`#728 <https://github.com/ipab-slmc/exotica/issues/728>`_)
* Contributors: Traiko Dinev, Wolfgang Merkt

6.0.0 (2020-11-08)
------------------
* Noetic/20.04 compatibility
* More unit testing tools and tests
* Expose more features to Python
* Fix issues with instantiation from Python using Initializers and tuple lists
* Contributors: Matt Timmons-Brown, Traiko Dinev, Vladimir Ivan, Wolfgang Merkt

5.1.3 (2020-02-13)
------------------
* Refactor CollisionScene, add faster distance checks, speedup SmoothCollisionDistance (`#688 <https://github.com/ipab-slmc/exotica/issues/688>`_)
* Expose full KinematicTree to Python; expose mesh collision shape information (`#686 <https://github.com/ipab-slmc/exotica/issues/686>`_) 
* Allow labels/legend in plot()
* Contributors: Wolfgang Merkt

5.1.2 (2020-02-10)
------------------

5.1.1 (2020-02-10)
------------------

5.1.0 (2020-01-31)
------------------
* Updates to match code developments and expose more functions
* Contributors: Adabotics, Chris Mower, Christian Rauch, Matt Timmons-Brown, Traiko Dinev, Vladimir Ivan, Wolfgang Merkt
