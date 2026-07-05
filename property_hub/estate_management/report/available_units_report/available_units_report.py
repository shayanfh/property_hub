import frappe


def execute(filters=None):
	filters = filters or {}
	columns = [
		{"label": "Unit", "fieldname": "name", "fieldtype": "Link", "options": "Property Unit", "width": 130},
		{"label": "Unit Number", "fieldname": "unit_number", "fieldtype": "Data", "width": 110},
		{"label": "Property", "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 150},
		{"label": "Unit Type", "fieldname": "unit_type", "fieldtype": "Data", "width": 120},
		{"label": "Floor", "fieldname": "floor", "fieldtype": "Int", "width": 70},
		{"label": "Bedrooms", "fieldname": "bedrooms", "fieldtype": "Int", "width": 90},
		{"label": "Bathrooms", "fieldname": "bathrooms", "fieldtype": "Int", "width": 90},
		{"label": "Area (sqm)", "fieldname": "area", "fieldtype": "Float", "width": 100},
		{"label": "Rent Amount", "fieldname": "rent_amount", "fieldtype": "Currency", "width": 120},
	]

	where_conditions = "pu.status = 'Available'"
	values = {}
	if filters.get("property"):
		where_conditions += " AND pu.property = %(property)s"
		values["property"] = filters["property"]
	if filters.get("unit_type"):
		where_conditions += " AND pu.unit_type = %(unit_type)s"
		values["unit_type"] = filters["unit_type"]

	data = frappe.db.sql(f"""
		SELECT
			pu.name, pu.unit_number, pu.property, pu.unit_type,
			pu.floor, pu.bedrooms, pu.bathrooms, pu.area, pu.rent_amount
		FROM `tabProperty Unit` pu
		WHERE {where_conditions}
		ORDER BY pu.property, pu.unit_number
	""", values, as_dict=True)

	return columns, data
