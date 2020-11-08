^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package exotica_core
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

5.1.3 (2020-02-13)
------------------
* Refactor CollisionScene, add faster distance checks, speedup SmoothCollisionDistance (`#688 <https://github.com/ipab-slmc/exotica/issues/688>`_)
* Expose full KinematicTree to Python; expose mesh collision shape information (`#686 <https://github.com/ipab-slmc/exotica/issues/686>`_)
* Contributors: Wolfgang Merkt

5.1.2 (2020-02-10)
------------------
* Fix bug in updating root tree (`#684 <https://github.com/ipab-slmc/exotica/issues/684>`_)
* Contributors: Wolfgang Merkt

5.1.1 (2020-02-10)
------------------
* Fix to avoid duplicate ID=0 in KinematicTree (`#683 <https://github.com/ipab-slmc/exotica/issues/683>`_)
* Added explicit general dependency on libzmq3-dev to fix buildfarm build issues
* Contributors: Vladimir Ivan, Wolfgang Merkt

5.1.0 (2020-01-31)
------------------
* Add support for Scene creation without SRDF, from robot param server (`#681 <https://github.com/ipab-slmc/exotica/issues/681>`_)
* Address -Wall warnings (`#679 <https://github.com/ipab-slmc/exotica/issues/679>`_)
* Fix floating-base Jacobian column switch bug, fix floating-base collision links (`#668 <https://github.com/ipab-slmc/exotica/issues/668>`_)
* Nice XML error handling on 18.04+; fix validity checkers; add ContinuousCollisionCast (`#660 <https://github.com/ipab-slmc/exotica/issues/660>`_)
* Add Meshcat visualisation (`#633 <https://github.com/ipab-slmc/exotica/issues/633>`_)
* New GetNumberOfIterations method in planning problem (`#603 <https://github.com/ipab-slmc/exotica/issues/603>`_)
* KinematicTree: getter for joints (`#598 <https://github.com/ipab-slmc/exotica/issues/598>`_)
* Change cost Jacobian to be a row vector (`#596 <https://github.com/ipab-slmc/exotica/issues/596>`_)
* Support full start state (position + velocity) for dynamic problems (`#572 <https://github.com/ipab-slmc/exotica/issues/572>`_)
* Deprecate non-const initializer, activate related warning as error, fix random issues (`#562 <https://github.com/ipab-slmc/exotica/issues/562>`_)
* Python3 compatibility (`#553 <https://github.com/ipab-slmc/exotica/issues/553>`_)
* Distinguish between controlled and model joints and links (`#528 <https://github.com/ipab-slmc/exotica/issues/528>`_)
* Sparse Jacobian triplets for TimeIndexedProblems
* Global random seed
* ... and many more
* Contributors: Chris Mower, Christian Rauch, Traiko Dinev, Vladimir Ivan, Wolfgang Merkt
