import frappe
import foundation

no_cache = 1

def get_context(context):
	if frappe.session.user != 'Guest':
		context.show_sidebar = True
		context.all_memberships = foundation.get_all_memberships_of_one_member()
