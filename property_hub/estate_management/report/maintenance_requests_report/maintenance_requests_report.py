import frappe


def execute(filters=None):
	filters = filters or {}
	columns = [
		{"label": "Request", "fieldname": "name", "fieldtype": "Link", "options": "Maintenance Request", "width": 150},
		{"label": "Property", "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 150},
		{"label": "Unit", "fieldname": "unit", "fieldtype": "Link", "options": "Property Unit", "width": 120},
		{"label": "Tenant", "fieldname": "tenant", "fieldtype": "Link", "options": "Customer", "width": 150},
		{"label": "Issue Type", "fieldname": "issue_type", "fieldtype": "Data", "width": 120},
		{"label": "Priority", "fieldname": "priority", "fieldtype": "Data", "width": 90},
		{"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 110},
		{"label": "Estimated Cost", "fieldname": "estimated_cost", "fieldtype": "Currency", "width": 130},
		{"label": "Actual Cost", "fieldname": "actual_cost", "fieldtype": "Currency", "width": 120},
		{"label": "Modified", "fieldname": "modified", "fieldtype": "Datetime", "width": 140},
	]

	where = "1=1"
	values = {}
	if filters.get("property"):
		where += " AND mr.property = %(property)s"
		values["property"] = filters["property"]
	if filters.get("status"):
		where += " AND mr.status = %(status)s"
		values["status"] = filters["status"]
	if filters.get("priority"):
		where += " AND mr.priority = %(priority)s"
		values["priority"] = filters["priority"]

	data = frappe.db.sql(f"""
		SELECT mr.name, mr.property, mr.unit, mr.tenant,
			   mr.issue_type, mr.priority, mr.status,
			   mr.estimated_cost, mr.actual_cost, mr.modified
		FROM `tabMaintenance Request` mr
		WHERE {where}
		ORDER BY mr.modified DESC
	""", values, as_dict=True)

	return columns, data
