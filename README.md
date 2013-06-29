iban-generator
==============

Generate the IBAN code for a bank account number.

**Warning:**
> The current code only has the IBAN rules for Brazilian Banks (29 digits).

Includes a REST webservice that is being served on Google AppEngine at:

[http://iban-generator.appspot.com](http://iban-generator.appspot.com/).


References
----------
[Wikipedia International Bank Account Number](https://en.wikipedia.org/wiki/International_Bank_Account_Number),
provides good information on the algorithms.

[SWIFT IBAN Registry](http://www.swift.com/dsp/resources/documents/IBAN_Registry.pdf),
provides detailed information about all ISO 13616 compliant national IBAN
formats.

[IBAN Implementation Guidelines for Brazil](www.bcb.gov.br/?IBAN-ING),
a complete description of the algorithm for Brazilian Banks.

[BACEN ISPB list](www.bcb.gov.br/?RELPARTSTR), the full list of ISPB codes
for Brazilian Banks.
