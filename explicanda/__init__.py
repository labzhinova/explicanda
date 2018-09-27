from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('ExplicandaPrototype').version
except DistributionNotFound:
    __version__ = '(local)'
