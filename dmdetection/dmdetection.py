# -*- coding: utf-8 -*-

"""Routine for calculating DM collision rates with a generic direct detection experiment."""

__author__ = 'Alan Duffy'
__email__ = 'mail@alanrduffy.com'
__version__ = '0.1.1'

from astropy import units
from astropy import constants
import numpy as np

class Detector:
        def __init__(self, name, atomic_mass, mass_of_detector):
            """Class for variables of Detector properties"""
            self.name=name
            self.atomic_num=atomic_mass 
            self.atomic_mass=atomic_mass * units.g / units.mol
            self.mass_of_detector=mass_of_detector * units.kg

class DM:
        def __init__(self, density, velocity, mass, cross_section):
            """Class for variables of DM particle"""
            self.density=density * units.GeV / constants.c**2 / units.cm**3 #units.msolMass / units.mpc**3
            self.velocity=velocity * units.km / units.s
            self.mass=mass * units.GeV / constants.c**2
            self.cross_section=cross_section * units.pbarn

def calcsigma(det,dm_p):
    """ Modify WIMP-nucleon cross section for collision cross-section with detector material """

    mass_reduced = det.atomic_num * (dm_p.mass/constants.m_p) / (det.atomic_num + dm_p.mass/constants.m_p)
    sigma = det.atomic_num**2. * mass_reduced**2. * dm_p.cross_section

    return sigma

def calcrate(det,dm_p):
    """ Calculate flythough rates per second """
    rate = dm_p.velocity*(dm_p.density/dm_p.mass)

    return rate

def calccol(sigma,rate,det):
    
    return sigma * rate * constants.N_A*(det.mass_of_detector/det.atomic_mass)

def run(detvar, dmvar='CDM'):
    """ Calculate rates and plot """

    if isinstance(detvar, dict):
        ## user is providing own parameters, i.e. det = ['name' : 'SABRE', 'atomic_mass' : 150., 'mass_of_detector' : 50.]
        det = Detector(detvar['name'],detvar['atomic_mass'],detvar['mass_of_detector'])
    elif detvar == 'SABRE':
        det = Detector('SABRE', 149.89, 50.)
    else:
        print "What detector do you want? You said ", detvar
        ## Add a return crash statement

    if isinstance(dmvar, dict):
        ## user is providing own parameters, i.e. particle = ['density' : 0.3 'GeV/cm^3', 'velocity' : 230., 'mass' : 100., 'cross_section' : 1e-5]
        dm_p = DM(dmvar['density'], dmvar['velocity'], dmvar['mass'], dmvar['cross_section'])
    elif dmvar == 'CDM':
        dm_p = DM(0.3, 230., 100., 1e-5)
    else:
        print "What particle is this? You passed ", dmvar

    ## Check numvers
    print "Number density of NaI atoms per unit mass ", (constants.N_A / det.atomic_mass)
    print "Number density of DM particles per unit volume ", (dm_p.density / dm_p.mass).cgs

    rate = calcrate(det, dm_p)
    print "Flythough rate per s ", rate.cgs
    print "Flythough rate per year ", (rate * units.yr).cgs

    sigma = calcsigma(det, dm_p) 
    print "Collision WIMP-nucleon cross section per nucelon ",dm_p.cross_section
    print "Colllision-cross section per WIMP-atom pair ",sigma.cgs

    col_rate = calccol(sigma,rate,det)
    print "Collision rate per s ",col_rate.cgs
    print "Collision rate per hour ",(col_rate * units.hr).cgs
    print "Collision rate per day ",(col_rate * units.day).cgs
    print "Collision rate per year ",(col_rate * units.yr).cgs

    return rate


