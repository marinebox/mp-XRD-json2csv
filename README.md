# mp-XRD-json2csv

The XRD pattern which has been downloaded from Materials Project is JSON file.

This python program convert the json file to csv file.

## Attention

This program ignores "hkl", "d_spacing" values, and X-ray source element and its wavelength.

The output csv file has only two keys: `two-theta`, `amplitude`.
