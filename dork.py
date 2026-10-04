#!/usr/bin/env python3

import argparse
import urllib.parse
import webbrowser
import time

DORKS = [
    "site:{d}",
    "site:*.{d}",
    "site:{d} -www",
    "related:{d}",
    "site:*.{d} -www -mail -docs",

    "site:{d} (inurl:login OR inurl:signin OR inurl:auth)",
    "site:{d} (inurl:admin OR inurl:dashboard OR inurl:panel)",
    'site:{d} (intitle:"sign in" OR intitle:"admin" OR intitle:"login")',

    "site:{d} inurl:phpmyadmin OR intitle:phpmyadmin",

    'site:{d} intitle:"index of"',
    'site:{d} intitle:"index of" (backup OR uploads OR logs)',

    "site:{d} (ext:zip OR ext:tar OR ext:gz OR ext:rar OR ext:7z OR ext:bak OR ext:old)",
    "site:{d} (ext:env OR ext:ini OR ext:yml OR ext:yaml OR ext:json OR ext:xml)",
    "site:{d} (ext:log OR ext:sql OR ext:csv OR ext:xls OR ext:xlsx)",

    "site:{d} ext:conf (nginx.conf OR httpd.conf)",
    "site:{d} inurl:wp-config.php",

    'site:{d} filetype:env "DB_PASSWORD"',
    'site:{d} intext:"password="',
    'site:{d} ("API_KEY" OR "API_SECRET" OR "token" OR "secret")',
    'site:{d} "password" (filetype:xls OR filetype:csv OR filetype:txt)',

    "site:{d} (inurl:/api/ OR inurl:swagger OR inurl:openapi OR inurl:api-docs)",
    "site:{d} (inurl:graphql OR inurl:graphiql)",

    'site:{d} (".git" OR ".svn" OR "package.json" OR "composer.json")',

    "site:{d} ext:js",
    "site:{d} ext:map",

    "site:{d} (ext:pdf OR ext:doc OR ext:docx OR ext:xls OR ext:xlsx OR ext:ppt OR ext:pptx)",

    "site:{d} inurl:php?id=",

    'site:{d} intext:"sql syntax near" OR intext:"error in your sql syntax"',

    'site:{d} ext:xml "phpinfo"',
    'site:{d} "Warning: include("',

    'site:s3.amazonaws.com "{d}"',
    'site:storage.googleapis.com "bucket" "{d}"',
    
    'site:{d} intitle:"employees" OR intitle:"directory" OR intitle:"staff"',
    'site:{d} intitle:"our team" OR intitle:"about us" OR intitle:"leadership"',
    'site:{d} intext:"@{d}"',
    'site:{d} filetype:pdf "Email:" "@{d}"',
    'site:{d} inurl:contact phone',
    'site:{d} intitle:"resume" OR intitle:"cv"',
    'site:linkedin.com/in "{d}"',
    'site:{d} intitle:"about" "software engineer"',
    'site:{d} filetype:pdf strategy',
    'site:{d} project initiative codename',
    'site:{d} server nas intranet',
    'site:{d} inurl:careers OR inurl:jobs requirements',
    'site:{d} partnered with filetype:pdf',
    'site:{d} inurl:wiki OR inurl:sharepoint OR inurl:confluence',
    'site:pastebin.com "@{d}"',
    'site:github.com "{d}" "api_key"',
    'site:github.com "@{d}"',
    'site:trello.com "{d}"',
    'site:s3.amazonaws.com "{d}"',
    'site:{d} filetype:pdf "Author:"',
    'site:{d} filetype:docx "Last modified by"',
    'site:{d} filetype:xlsx "\\\\fileserver\\\\"',
    'site:{d} filetype:pdf before:2018-01-01',
    'site:{d} before:2020-01-01 password',
    'site:{d} (intitle:"cv" OR intitle:"resume" OR intitle:"team" OR intitle:"contact") -inurl:blog -inurl:legal'
]
def google_url(query):
    return "https://www.google.com/search?q=" + urllib.parse.quote(query)

parser = argparse.ArgumentParser()
parser.add_argument("domain", help="Target domain")
parser.add_argument("--delay", type=int, default=3,
                    help="Seconds between tabs")
args = parser.parse_args()

for dork in DORKS:
    query = dork.format(d=args.domain)
    url = google_url(query)
    print(f"[+] {query}")
    webbrowser.open_new_tab(url)
    time.sleep(args.delay)
