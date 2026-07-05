import frappe
from frappe.utils import today, add_days


def execute(filters=None):
	filters = filters or {}
	days_ahead = int(filters.get("days_ahead", 30))
	threshold = add_days(today(), days_ahead)

	columns = [
		{"label": "Contract", "fieldname": "name", "fieldtype": "Link", "options": "Lease Contract", "width": 150},
		{"label": "Tenant", "fieldname": "tenant", "fieldtype": "Link", "options": "Customer", "width": 150},
		{"label": "Property", "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 150},
		{"label": "Unit", "fieldname": "unit", "fieldtype": "Link", "options": "Property Unit", "width": 120},
		{"label": "End Date", "fieldname": "end_date", "fieldtype": "Date", "width": 110},
		{"label": "Days Remaining", "fieldname": "days_remaining", "fieldtype": "Int", "width": 120},
		{"label": "Rent Amount", "fieldname": "rent_amount", "fieldtype": "Currency", "width": 120},
	]

	data = frappe.db.sql("""
		SELECT lc.name, lc.tenant, lc.property, lc.unit, lc.end_date,
			   DATEDIFF(lc.end_date, CURDATE()) AS days_remaining,
			   lc.rent_amount
		FROM `tabLease Contract` lc
		WHERE lc.status = 'Active'
		  AND lc.docstatus = 1
		  AND lc.end_date BETWEEN CURDATE() AND %(threshold)s
		ORDER BY lc.end_date
	""", {"threshold": threshold}, as_dict=True)

	return columns, data
