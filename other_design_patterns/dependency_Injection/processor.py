from abc import ABC


class Processor(ABC):
    """Example processor base class.

    Processor is a brain of every computer. Processor is a very common term and could be produced
    by different ways in different company.
    """
    pass


class AMDProcessor(Processor):
    """AMD Ryzen Processor"""
    pass


class IntelProcessor(Processor):
    """Intel Core Processor"""
    pass


class ARMProcessor(Processor):
    """ARM Processor"""
    pass
