#!/usr/bin/env python
import sys
from xml.etree.ElementTree import parse

def convert_aff(input_file):
    new_url_base = 'http://factfinder2.census.gov/bkmk/table/1.0/en'
    # parse() takes either a file-like object or a filename to open
    document = parse(input_file)
    
    product = document.find('product')
    url = '/'.join([
        new_url_base,
        product.attrib['program-id'],
        product.attrib['dataset-id'],
        product.attrib['table-id']
    ])
    if 'cat-group-spec-id' in product.attrib:
        url = '.'.join([
            url,
            product.attrib['cat-group-spec-id']
        ])
    
    geo_ids = []
    code_types = {}
    selection = document.find('selection')
    if selection is not None and len(selection):
        for dimension in selection.findall('dimension'):
            dimension_type = dimension.attrib['type']
            if dimension_type == 'geo':
                for cat_id in dimension.findall('cat-id'):
                    geo_ids.append(cat_id.text)
            else:
                codes = []
                if dimension_type in code_types:
                    codes = code_types[dimension_type]
                for cat_id in dimension.findall('cat-id'):
                    codes.append(cat_id.text)
                code_types[dimension_type] = codes
    if geo_ids:
        url = '%s/%s' % (url, '|'.join(geo_ids))
    
    if code_types:
        for code_type in code_types.keys():
            url = '%s/%s~%s' % (url, code_type, '|'.join(code_types[code_type]))
    
    return url

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: %s foo.aff" % sys.argv[0]
    else:
        print convert_aff(sys.argv[1])

