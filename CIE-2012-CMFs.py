#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PyOpenColorIO
import numpy
import colour
from colour import (
    io,
    adaptation,
    models
)


if __name__ == "__main__":
    CIE2012_cmfs = colour.CMFS["CIE 2012 2 Degree Standard Observer"]

    start_wavelength = numpy.min(CIE2012_cmfs.wavelengths)
    stop_wavelength = numpy.max(CIE2012_cmfs.wavelengths) + 1
    increment = 1
    for wavelength in numpy.arange(
        start=start_wavelength,
        stop=stop_wavelength,
        step=increment
    ):
        if wavelength < stop_wavelength:
            print("make_float4({0:.1f}f, {1:.10E}f, {1:.10E}f, {1:.10E}f)"
                  .format(
                      wavelength,
                      CIE2012_cmfs[wavelength][0],
                      CIE2012_cmfs[wavelength][1],
                      CIE2012_cmfs[wavelength][2]
                      ))
