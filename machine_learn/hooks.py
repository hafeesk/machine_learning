# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "machine_learn"
app_title = "Machine Learn"
app_publisher = "hafees"
app_description = "Machine Learning"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hafeesk@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/machine_learn/css/machine_learn.css"
# app_include_js = "/assets/machine_learn/js/machine_learn.js"

# include js, css files in header of web template
# web_include_css = "/assets/machine_learn/css/machine_learn.css"
# web_include_js = "/assets/machine_learn/js/machine_learn.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "machine_learn.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "machine_learn.install.before_install"
# after_install = "machine_learn.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "machine_learn.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"machine_learn.tasks.all"
# 	],
# 	"daily": [
# 		"machine_learn.tasks.daily"
# 	],
# 	"hourly": [
# 		"machine_learn.tasks.hourly"
# 	],
# 	"weekly": [
# 		"machine_learn.tasks.weekly"
# 	]
# 	"monthly": [
# 		"machine_learn.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "machine_learn.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "machine_learn.event.get_events"
# }

