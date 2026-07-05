import frappe


def after_install():
	_create_property_hub_role()
	frappe.db.commit()


def _create_property_hub_role():
	if not frappe.db.exists("Role", "Property Manager"):
		role = frappe.get_doc({"doctype": "Role", "role_name": "Property Manager", "desk_access": 1})
		role.insert(ignore_permissions=True)
