#!/usr/bin/env python 
"""
Calculate the genome features in an organisms annotation file
"""

import os 
import sys 
from gfftools import GFFParser

def get_features(gtf_file, fa_file):
    """
    get the total number of genes based on the annotation source  
    # of coding genes 
    genes with 3' 5' UTR
    other different class of genes
    """

    anno_db = GFFParser.Parse(gtf_file) 
    total_genes = len(anno_db) 

    non_coding = 0
    cds_coding = 0
    total_transcripts = 0 
    utr = 0 
    utr5 = 0
    utr3 = 0
    no_utr = 0 

    for features in anno_db:
        total_transcripts += len(features['transcripts'])

        for trans in features['cds_exons']:
            if trans.any():
                cds_coding += 1
            else:
                non_coding += 1

        for idx, trans in enumerate(features['transcripts']):
            if features['utr3_exons'][idx].any() and features['utr5_exons'][idx].any():
                utr +=1
            elif features['utr3_exons'][idx].any():
                utr3 +=1
            elif features['utr5_exons'][idx].any():
                utr5 += 1
            else:
                no_utr +=1 
    
    print 'total genes: ', total_genes
    print 'total transcripts: ', total_transcripts
    print 'coding transcripts: ', cds_coding
    print 'noncoding transcripts: ', non_coding
    print '---------------'
    print 'both utrs', utr 
    print '3 utr ', utr3
    print '5 utr ', utr5
    print 'no utr ', no_utr


if __name__=="__main__":

    #gtf_fname = "data/H_sapiens/GRCh38/out.gff"
    gtf_fname = "data/M_musculus/GRCm38/out.gff"

    fas_fname = "data/H_sapiens/GRCh38/out.fas.bz2"

    get_features(gtf_fname, fas_fname)

