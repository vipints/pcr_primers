#!/usr/bin/env python 
"""
wrapper for primer3 primer design program
"""

import os 
import sys 
from gfftools import GFFParser

def main():
    """
    core function
    """
    
    gtf_fname = ""
    gene_name = ""

    gtf_content = GFFParser.Parse(gtf_fname)
    
    ## extract the gene of interest 


if __name__=="__main__":
    main()
