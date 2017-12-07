#!/usr/bin/env python
# coding: utf-8

import string

ALPHA = {c: str(ord(c) % 55) for c in string.ascii_uppercase}

ISPB = {
    'Banco BNP Paribas Brasil S.A.': '01522368',
    'Banco Bradesco S.A.': '60746948',
    'Banco Citibank S.A.': '33479023',
    'Banco Caixa Econômica Federal': '00360305',
    'Banco Cooperativo Sicredi S.A.': '01181521',
    'Banco de La Nacion Argentina': '33042151',
    'Banco de La Provincia de Buenos Aires': '44189447',
    'Banco de La Republica Oriental del Uruguay': '51938876',
    'Banco de Tokyo-Mitsubishi UFJ Brasil S.A.': '60498557',
    'Banco do Brasil S.A.': '00000000',
    'Banco do Estado do Rio Grande do Sul S.A.': '92702067',
    'Banco Intercap S.A.': '58497702',
    'Banco Itaú BBA S.A.': '17298092',
    'Banco Mercantil do Brasil S.A.': '17184037',
    'Banco Modal S.A.': '30723886',
    'Banco Rural S.A.': '33124959',
    'Banco Santander S.A.': '90400888',
    'Banco Société Générale Brasil S.A.': '61533584',
    'BRB - Banco de Brasí­lia S.A.': '00000208',
    'Deutsche Bank S.A. Banco Alemão': '62331228',
    'HSBC Bank Brasil S.A. Banco Múltiplo': '01701201',
    'Itaú Unibanco S.A.': '60701190',
    'Natixis Brasil S.A. Banco Múltiplo': '09274232',
    'Unibanco - União de Bancos Brasileiros S.A.': '33700394'
}


def make_iban(ispb, agency, account, country='BR', account_type='C', account_owner='1'):
    assert(len(ispb) == 8)
    assert(len(agency) <= 5)
    assert(len(account) <= 10)
    agency = agency.zfill(5)
    account = account.zfill(10)
    iban = ispb + agency + account + account_type + account_owner
    check = iban + country + '00'
    check = int(''.join(ALPHA.get(c, c) for c in check))
    check = 98 - (check % 97)
    check = str(check).zfill(2)
    return country + check + iban


def check_iban(iban):
    if len(iban) != 29:
        return False
    check = iban[4:] + iban[:4]
    check = int(''.join(ALPHA.get(c, c) for c in check))
    return check % 97 == 1


if __name__ == '__main__':
    iban = make_iban(ISPB['Banco do Brasil S.A.'], '12345', '123456')
    check = check_iban(iban)
    print check, iban
