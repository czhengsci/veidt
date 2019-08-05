# coding: utf-8
# Copyright (c) Materials Virtual Lab
# Distributed under the terms of the BSD License.
from numbers import Number


class CenvPrediction(object):

    def __init__(self, xanes_spectrum, energy_reference, energy_range):

        self.xanes_spectrum = xanes_spectrum
        self.energy_reference = energy_reference
        self.energy_range = energy_range
        if isinstance(self.energy_range, list):
            self.energy_lower_bound = self.energy_range[0]
            self.energy_higher_bound = self.energy_range[-1]

        self._parameter_validation()


    def _parameter_validation(self):

        if self.energy_reference == 'lowest':
            if not isinstance(self.energy_range, Number):
                raise ValueError(
                    'Energy range needs to be a number when the energy reference point is the starting energy of the spectrum')

            if self.energy_range < 0:
                raise ValueError(
                    'Energy range needs to be larger than 0. Invalid energy range error.'
                )

        if self.energy_reference == 'E0':
            if not isinstance(self.energy_range, list):
                raise ValueError(
                    'Energy range needs to be a list contains lower energy bound and higher energy bound refer to energy reference point'
                )

            if self.energy_lower_bound >0:
                raise ValueError(
                    'Energy lower bound needs to be less than zero.'
                )

            if self.energy_higher_bound < 0:
                raise ValueError(
                    'Energy higher bound needs to be larger than zero.'
                )




