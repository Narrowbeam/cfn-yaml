# Copyright {2016} {Narrowbeam Limited}

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
   
from bs4 import BeautifulSoup
import requests
import re
import os

docurl = "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/"

page = requests.get (docurl + "aws-template-resource-type-ref.html" )
html_doc = page.content

urllist = []

# Create the folder for the snippets
try:
  os.mkdir("./cfn-yaml")
except:
  pass

soup = BeautifulSoup(html_doc, 'html.parser')

# Selector based lookup - gets what we want and awstoc duplicates
urllisttmp = soup.select('li a[href*="aws-"]')

# Build a list of link description, url
for url in urllisttmp:
  try:
    myclass = url['class']
  except:
    # We actually only care about the ones without a class !!!
    urllist.append([url.text, docurl + url['href']])

snippetStart = """<snippet>
  <content><![CDATA[
"""
snippetEnd = """
]]></content>"""


count = 0
for (pagelink,pageurl) in urllist:

  hotkey = ""
  snippet = ""
  pagelinklist = pagelink.split("::")
  hotkey = "cfn-" + pagelinklist[1]
  for i in range(2,len(pagelinklist)):
    hotkey =  hotkey + "-" + pagelinklist[i]

  snippetFinish = """
  <tabTrigger>""" + hotkey + """</tabTrigger>
  <scope>source.yaml, source.cloudformation</scope>
  </snippet>"""

  # print hotkey

  snippet = snippet +  snippetStart
  snippet = snippet +  "# AWS-DOC " + pageurl + '\n'

  page = requests.get(pageurl).content
  soup2 = BeautifulSoup(page, 'html.parser')
  fragment = soup2.select_one('#YAML pre')

  for tag in fragment:
    #Some source material has an extra \n that needs to be stripped
    snippetfilter = tag.text
    if snippetfilter[0] == '\n':
      snippet = snippet + snippetfilter[1:]
    else:
      snippet = snippet + tag.text  

  count += 1
  snippet = snippet + snippetEnd
  snippet = snippet +  snippetFinish

  # if count == 10:
  #   break

  print "writing: " + "cfn-yaml/" + hotkey+".sublime-snippet"
  # print snippet
  try:
    os.mkdir("cfn-yaml/" + pagelinklist[1])
  except:
    pass

  f = open("cfn-yaml/" + pagelinklist[1] + "/" + hotkey+".sublime-snippet", "wb")
  f.write(snippet)
  f.close()
