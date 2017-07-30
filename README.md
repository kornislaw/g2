# g2
Generating files based on a template and a CSV list of keywords to be replaced. It is helpful when you need multiple files which are almost the same and differ only with a few settings. In a CSV file you can list these differences and the script will generate files from a given template.

Usage
------

```  
  bccb.py --template=<template_file> --data=<keywords_csv>
  bccb.py -h | --help
  bccb.py -v | --version
```

### CSV format

First column is for output filenames. Second and following are for keywords and differences.

```csv
output,{{URL}},{{TIMEOUT}}
output_1.robot,https://www.google.com,30
output_2.robot,https://www.amazon.com,30
output_3.robot,https://www.ibm.com,40
```

Insert keywords from the header into your template file (in the example above the keywords are `{[URL}}` and `{{TIMEOUT}}`.

Example
-------

``` bash
> g2.py --template=template.robot --data=data.csv

output_1.robot saved
output_2.robot saved
output_3.robot saved
```
