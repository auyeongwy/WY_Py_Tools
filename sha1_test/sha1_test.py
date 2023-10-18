#!/usr/bin/env python3

""" SHA1 hash example

Demos creating a hash from content using SHA1 and a pre-defined secret.
"""

import hmac
import hashlib
import urllib.parse

content = '{"campaign_id":257,"timestamp":1691671400,"event":"click","email":"paul@pramsden.co.uk","link_clicked":"https://www.euronews.com/green/2023/08/09/we-have-never-seen-it-so-low-spain-introduces-water-restrictions-as-reservoirs-run-dry?insEmail=1&insNltCmpId=257&insNltSldt=10080&insPnName=euronewsfr&isIns=1&isInsNltCmp=1&utm_campaign=green_newsletter&utm_medium=referral&utm_source=newsletter","campaign_name":"Green EN","sender_domain":"@pramsden.co.uk","variation_id":257,"iid":"b4fef543-7233-4141-a92d-e0181f6dad5f","ip":"31.94.17.94","user_agent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36","url_offset":{"index":11,"type":"html"},"subject":"\'We have never seen it so low\': Spain introduces water restrictions as reservoirs run dry"}'

secret = '6603b1d9-b061-411b-b912-fc1a65582cb3'

hmac_obj = hmac.new(secret.encode(), content.encode(), 'sha1')

print(content)
print(hmac_obj.hexdigest())
# Got answer: 5f11461be6255fe84524dd10f8c8cd100182b071
