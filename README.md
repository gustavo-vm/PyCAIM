LAIM is a supervised discretization method for multi label data [1] and Python-LAIM is a implementation of LAIM. It is an adaptation of [Python-CAIM](https://github.com/Morgan243/PyCAIM).

**CLI Options**

    usage: caim.py [-h] [-t TARGET_FIELD] [-o OUTPUT_PATH] [-H] [-q] input_file

    LAIM Algorithm Command Line Tool and Library

    positional arguments:
      input_file            CSV input data file

    optional arguments:
      -h, --help            show this help message and exit
      -t TARGET_FIELD, --target-field TARGET_FIELD
                            Target field as an integer (0-indexed) or string
                            corresponding to column name. Negative indices (e.g.
                            -1) are allowed.
      -o OUTPUT_PATH, --output-path OUTPUT_PATH
                            File path to write discretized form of data in CSV
                            format
      -H, --header          Use first row as column/field names
      -q, --quiet           Minimal information is printed to STDOUT

**Interval Output**

Intervals are printed in the form:

    [ 0.13  0.34  0.39  0.66]

Which should be interpretted as:

    [0.13, 0.34](0.34, 0.39](0.39, 0.66]

The output dataset will use the right-end of each interval as the discretized value.


[1] Cano, A., Luna, J. M., Gibaja, E. L., & Ventura, S. (2016). LAIM discretization for multi-label data. Information Sciences, 330, 370-384.
