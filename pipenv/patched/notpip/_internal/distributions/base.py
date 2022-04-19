import abc

from pipenv.patched.notpip._internal.index.package_finder import PackageFinder
from pipenv.patched.notpip._internal.metadata.base import BaseDistribution
from pipenv.patched.notpip._internal.req import InstallRequirement


class AbstractDistribution(metaclass=abc.ABCMeta):
    """A base class for handling installable artifacts.

    The requirements for anything installable are as follows:

     - we must be able to determine the requirement name
       (or we can't correctly handle the non-upgrade case).

     - for packages with setup requirements, we must also be able
       to determine their requirements without installing additional
       packages (for the same reason as run-time dependencies)

     - we must be able to create a Distribution object exposing the
       above metadata.
    """

    def __init__(self, req: InstallRequirement) -> None:
        super().__init__()
        self.req = req

    @abc.abstractmethod
    def get_metadata_distribution(self) -> BaseDistribution:
        raise NotImplementedError()

    @abc.abstractmethod
    def prepare_distribution_metadata(
        self, finder: PackageFinder, build_isolation: bool
    ) -> None:
        raise NotImplementedError()
