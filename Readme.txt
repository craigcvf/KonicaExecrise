Description & Background:

This solution set is a Python Flask-based sample application server that provides user identity and user authentication features.
Uses a Python Flask based web server to serve both a REST API and a web front-end that uses DJANGO to present a set of
basic features that most web sites use for user account creation, login, forgot password, verify email address,
lock account, change password, edit account profile, etc.

The objective is to provide an example application skeleton, REST API example, web application example, and a useful
starting point for any web application that fits with this or similar application architecture.

REQUIREMENTS:

The coding was prepared using the following applications and components:
OS:  Microsoft Windows 10 Professional V1803==Build: 17134.471
IDE:  Microsoft Visual Studio Community 2017==15.9.4
.NET Framework==4.7.x
Python=3.7.x
coverage==4.2
Flask==0.12
Flask-Bcrypt==0.7.1
Flask-Cors==3.0.3
Flask-Migrate==2.0.2
Flask-Script==2.0.5
Flask-SQLAlchemy==2.1
aiohttp==0.18.4
cchardet==1.0.0
gunicorn==19.3.0
httpie==0.9.2
PyJWT==1.4.0

CREDITS:

classTokenAuthenitication: Jyoti Gautam, medium.com https://medium.com/python-pandemonium/json-web-token-based-authentication-in-django-b6dcfa42a332
config.py & test_config.py:  Micheal Herman, realpython  https://github.com/realpython/flask-jwt-auth/commit/3a851f5ed6a01f4b61aa95ad1e8fbf2ebcde26a1
forms.py, views.py, views_test.py & backend.py:  https://github.com/keedio

LICENSES:

config.py:
The MIT License (MIT) Copyright (c) 2016 Michael Herman
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

forms.py:
Licensed to Cloudera, Inc. under one or more contributor license agreements.  See the NOTICE file distributed with this work for additional information
regarding copyright ownership.  Cloudera, Inc. licenses this file to you under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and
limitations under the License.