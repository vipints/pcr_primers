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
    
    cds_exons = 0 
    utr3_exons = 0 
    for idp, feat in enumerate(gtf_content):
        if not feat['cds_exons'][0].any():
            cds_exons += 1 
        if not feat['utr3_exons'][0].any():
            utr3_exons += 1 

if __name__=="__main__":

    gtf_fname = "data/H_sapiens/GRCh38/out.gff.bz2"
    fas_fname = "data/H_sapiens/GRCh38/out.fas.bz2"

    get_features(gtf_fname, fas_fname)

