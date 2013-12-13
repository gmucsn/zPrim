#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import tornado.web
import tornado.ioloop
import os, sys
import glob
import fix_path
from expGeneral import *
from expManager import *
from regionManager import *

#experimentPath = "/exp"
adminForm = '''<p>Register:</p>
                    <form action="/" method="post">
                        <input type="submit" name="action" value="register">
                    </form>
               <p>Census:</p>
                    <form action="/" method="post">
                        <input type="submit" name="action" value="census">
                    </form>'''

root = os.path.dirname(__file__)
port = 9001
        
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(adminForm)
        
    def post(self): # This is really dumb, but whatever.
        #self.response.write(open('index.html').read())
        action = self.get_argument("action")
        print "hello world"
        print ExpManager.expTypes
        if action == "register":
            ExpManager.experiments["Twiegtest"].registerSession("TE16")
            RegManager.regions["TE16"].load_new("twiegtest")
            RegManager.regions["TE16"].session_uri = ""
            self.write(adminForm+"<br>Register")
        elif action == "census":
            #ExpManager.experiments["Twiegtest"].registerSession("TE16")
            #RegManager.regions["TE16"].load_new("twiegtest")
            self.write(adminForm+"<br>Census")
        #elif self.request.get("census"):
        #    self.response.write("session")
        
        
class MasterHandler(tornado.web.RequestHandler):
    def post(self):
        region = self.get_argument('region')
        uri = self.get_argument('uri')
        RegManager.regions[region].session_uri = uri
        print uri
        self.response("")
        
class testHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(testStr)
        #self.response.write([experiment.testVal for experiment in ExpManager.experiments])

ExpManager = ExperimentManager()
RegManager = RegionManager(ExpManager.experiments.iterkeys()) 

app = tornado.web.Application([
    (r'/', MainHandler),
    (r'/master', MasterHandler),
    (r'/test', testHandler)
],template_path = root, static_path = root)

if __name__ == "__main__":
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()
