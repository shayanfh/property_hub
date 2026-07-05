import frappe
from frappe.utils import today, get_first_day, get_last_day


def execute(filters=None):
	filters = filters or {}
	from_date = filters.get("from_date") or get_first_day(today())
	to_date = filters.get("to_date") or get_last_day(today())

	columns = [
		{"label": "Property", "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 180},
		{"label": "Total Requests", "fieldname": "total_requests", "fieldtype": "Int", "width": 120},
		{"label": "Open", "fieldname": "open_requests", "fieldtype": "Int", "width": 80},
		{"label": "Completed", "fieldname": "completed_requests", "fieldtype": "Int", "width": 100},
		{"label": "Total Estimated", "fieldname": "total_estimated", "fieldtype": "Currency", "width": 140},
		{"label": "Total Actual", "fieldname": "total_actual", "fieldtype": "Currency", "width": 130},
		{"label": "Variance", "fieldname": "variance", "fieldtype": "Currency", "width": 120},
	]

	data = frappe.db.sql("""
		SELECT
			mr.property,
			COUNT(mr.name) AS total_requests,
			SUM(CASE WHEN mr.status = 'Open' THEN 1 ELSE 0 END) AS open_requests,
			SUM(CASE WHEN mr.status = 'Completed' THEN 1 ELSE 0 END) AS completed_requests,
			SUM(IFNULL(mr.estimated_cost, 0)) AS total_estimated,
			SUM(IFNULL(mr.actual_cost, 0)) AS total_actual,
			SUM(IFNULL(mr.actual_cost, 0)) - SUM(IFNULL(mr.estimated_cost, 0)) AS variance
		FROM `tabMaintenance Request` mr
		WHERE mr.modified BETWEEN %(from_date)s AND %(to_date)s
		GROUP BY mr.property
		ORDER BY total_actual DESC
	""", {"from_date": from_date, "to_date": to_date}, as_dict=True)

	return columns, data
