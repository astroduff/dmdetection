#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dmdetection
----------------------------------

Tests for `dmdetection` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from dmdetection import dmdetection
from dmdetection import cli


class TestDmdetection(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass
    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'dmdetection.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    def test_cosmologies(self):
        cosmolist = ['WMAP1', 'WMAP3', 'WMAP5',
                     'WMAP7', 'WMAP9',
                     'Planck13', 'Planck15']
        conclist = [8.84952, 6.57093, 7.66308,
                    7.893508, 8.88391,
                    9.25026, 9.044999]
        ival = 0
        for cosmo in cosmolist:
            output = commah.run(cosmo, Mi=[1e12])
            assert(np.allclose(output['c'].flatten()[0],
                   conclist[ival], rtol=1e-3))
            ival += 1
        pass

    def test_evolution(self):
        zlist = np.array([0., 1., 2.])
        conclist = np.array([7.66308, 5.70009, 4.55295])
        output = commah.run('WMAP5', zi=[0.], Mi=[1e12], z=zlist)
        assert(np.allclose(output['c'].flatten(), conclist, rtol=1e-3))
        pass

    def test_startingz(self):
        zlist = np.array([0., 1., 2.])
        conclist = np.array([4.55295, 4.43175, 4.26342])
        output = commah.run('WMAP5', zi=zlist, Mi=[1e12], z=2.)
        assert(np.allclose(output['c'].flatten(), conclist, rtol=1e-3))
        pass

    def tearDown(self):
        pass
    @classmethod
    def teardown_class(cls):
        pass

