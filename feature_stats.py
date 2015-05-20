#!/usr/bin/env python 
"""
Calculate the genome features in an organisms annotation file
"""

import os 
import sys 
from gfftools import GFFParser

def get_features(gtf_file, fa_file):
    """
    core function
    """
    
    gtf_content = GFFParser.Parse(gtf_file) 
    
    print len(gtf_content)


if __name__=="__main__":

    gtf_fname = "/home/vipin/data/H_sapiens/GRCh38/out.gff.bz2"
    fas_fname = "/home/vipin/data/H_sapiens/GRCh38/out.fas.bz2"

    get_features()

