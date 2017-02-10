#!/usr/bin/env python
# coding: utf-8

import webapp2
import iban
import json


class IBAN(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        data = {
            'ispb': '',
            'agency': '',
            'account': '',
            'country': 'BR',
            'account_type': 'C',
            'account_owner': '1',
        }
        args = self.request.params
        if args.get('iban'):
            return self._check_iban(args['iban'])
        data.update((k, args[k].replace('-', '').strip())
            for k in set(data).intersection(args))
        if not all(data.viewvalues()):
            data['ispb'] = iban.ISPB
            self.response.write(json.dumps(data))
        else:
            return self._make_iban(data)

    def _check_iban(self, value):
        check = iban.check_iban(value.upper())
        self.response.write(json.dumps({'valid': check}))

    def _make_iban(self, data):
        try:
            value = iban.make_iban(
                data['ispb'], data['agency'], data['account'], data['country'],
                data['account_type'], data['account_owner'])
        except Exception:
            self.response.status = 403
            value = 'Invalid parameters'
        self.response.write(json.dumps({'iban': value}))


application = webapp2.WSGIApplication([
    ('/rest/', IBAN),
], debug=True)
