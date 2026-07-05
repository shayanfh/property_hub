"""
Property Hub - Demo Data Setup
Run: bench --site <site> execute property_hub.estate_management.setup.setup_demo_data.setup
Idempotent: safe to run multiple times.
"""
import frappe
from frappe.utils import add_months, add_days, getdate, today


# ── Owners ────────────────────────────────────────────────────────────────────

OWNERS = [
	{
		"owner_name": "Khalid Al-Balushi",
		"phone": "+968-9911-2233",
		"email": "khalid.balushi@demo.com",
		"nationality": "Omani",
		"civil_id": "10234567",
		"status": "Active",
	},
	{
		"owner_name": "Maryam Al-Harthi",
		"phone": "+968-9922-3344",
		"email": "maryam.harthi@demo.com",
		"nationality": "Omani",
		"civil_id": "10345678",
		"status": "Active",
	},
	{
		"owner_name": "Muscat Real Estate LLC",
		"phone": "+968-2234-5566",
		"email": "info@muscatrealestate.demo",
		"nationality": "Company",
		"civil_id": "",
		"status": "Active",
	},
]

# ── Properties ────────────────────────────────────────────────────────────────
# owner_index → index into OWNERS list
# final_status → property status after all leases are applied

PROPERTIES = [
	{
		"property_name": "Al-Qurum Tower",
		"property_code": "AQT-001",
		"owner_index": 0,
		"property_type": "Residential",
		"address": "Qurum Heights, Way 3012",
		"city": "Muscat",
		"final_status": "Occupied",
	},
	{
		"property_name": "Ruwi Business Center",
		"property_code": "RBC-001",
		"owner_index": 2,
		"property_type": "Commercial",
		"address": "Al-Noor Street, Ruwi",
		"city": "Muscat",
		"final_status": "Occupied",
	},
	{
		"property_name": "Al-Mouj Residences",
		"property_code": "AMR-001",
		"owner_index": 1,
		"property_type": "Residential",
		"address": "Al-Mouj Marina, Building 7",
		"city": "Muscat",
		"final_status": "Occupied",
	},
	{
		"property_name": "Salalah Garden Villas",
		"property_code": "SGV-001",
		"owner_index": 0,
		"property_type": "Residential",
		"address": "Al-Haffa District, Street 14",
		"city": "Salalah",
		"final_status": "Under Maintenance",
	},
	{
		"property_name": "Sohar Industrial Warehouses",
		"property_code": "SIW-001",
		"owner_index": 2,
		"property_type": "Warehouse",
		"address": "Sohar Free Zone, Block C",
		"city": "Sohar",
		"final_status": "Available",
	},
]

# ── Units ─────────────────────────────────────────────────────────────────────
# prop_index → index into PROPERTIES list
# final_status → desired status AFTER leases are applied
#   "Rented" units must have a matching LEASE_CONTRACT entry
#   others are set directly

UNITS = [
	# ── Al-Qurum Tower (3 units) ─────────────────────
	{"unit_number": "101", "prop_index": 0, "floor": 1, "unit_type": "2 Bedroom",  "rent_amount": 450,  "bedrooms": 2, "bathrooms": 2, "area": 120.0, "final_status": "Rented"},
	{"unit_number": "102", "prop_index": 0, "floor": 1, "unit_type": "1 Bedroom",  "rent_amount": 280,  "bedrooms": 1, "bathrooms": 1, "area": 75.0,  "final_status": "Rented"},
	{"unit_number": "201", "prop_index": 0, "floor": 2, "unit_type": "3 Bedroom",  "rent_amount": 650,  "bedrooms": 3, "bathrooms": 2, "area": 160.0, "final_status": "Reserved"},
	# ── Ruwi Business Center (2 units) ───────────────
	{"unit_number": "G01", "prop_index": 1, "floor": 0, "unit_type": "Shop",       "rent_amount": 800,  "bedrooms": 0, "bathrooms": 1, "area": 60.0,  "final_status": "Rented"},
	{"unit_number": "G02", "prop_index": 1, "floor": 0, "unit_type": "Office",     "rent_amount": 1200, "bedrooms": 0, "bathrooms": 2, "area": 150.0, "final_status": "Available"},
	# ── Al-Mouj Residences (4 units) ─────────────────
	{"unit_number": "A101","prop_index": 2, "floor": 1, "unit_type": "2 Bedroom",  "rent_amount": 550,  "bedrooms": 2, "bathrooms": 2, "area": 130.0, "final_status": "Rented"},
	{"unit_number": "A102","prop_index": 2, "floor": 1, "unit_type": "Studio",     "rent_amount": 200,  "bedrooms": 0, "bathrooms": 1, "area": 45.0,  "final_status": "Under Maintenance"},
	{"unit_number": "B201","prop_index": 2, "floor": 2, "unit_type": "Penthouse",  "rent_amount": 1500, "bedrooms": 4, "bathrooms": 3, "area": 250.0, "final_status": "Reserved"},
	{"unit_number": "B202","prop_index": 2, "floor": 2, "unit_type": "2 Bedroom",  "rent_amount": 480,  "bedrooms": 2, "bathrooms": 2, "area": 115.0, "final_status": "Rented"},
	# ── Salalah Garden Villas (3 units) ──────────────
	{"unit_number": "V01", "prop_index": 3, "floor": 1, "unit_type": "4 Bedroom",  "rent_amount": 900,  "bedrooms": 4, "bathrooms": 3, "area": 280.0, "final_status": "Rented"},
	{"unit_number": "V02", "prop_index": 3, "floor": 1, "unit_type": "3 Bedroom",  "rent_amount": 700,  "bedrooms": 3, "bathrooms": 2, "area": 200.0, "final_status": "Rented"},
	{"unit_number": "V03", "prop_index": 3, "floor": 2, "unit_type": "3 Bedroom",  "rent_amount": 720,  "bedrooms": 3, "bathrooms": 2, "area": 195.0, "final_status": "Rented"},
	# ── Sohar Industrial Warehouses (3 units) ─────────
	{"unit_number": "W01", "prop_index": 4, "floor": 0, "unit_type": "Warehouse",  "rent_amount": 600,  "bedrooms": 0, "bathrooms": 1, "area": 400.0, "final_status": "Rented"},
	{"unit_number": "W02", "prop_index": 4, "floor": 0, "unit_type": "Warehouse",  "rent_amount": 500,  "bedrooms": 0, "bathrooms": 1, "area": 300.0, "final_status": "Available"},
	{"unit_number": "W03", "prop_index": 4, "floor": 0, "unit_type": "Warehouse",  "rent_amount": 400,  "bedrooms": 0, "bathrooms": 0, "area": 200.0, "final_status": "Available"},
]
# unit indices summary:
#  0=AQT101(Rented)  1=AQT102(Rented)  2=AQT201(Reserved)
#  3=G01(Rented)     4=G02(Available)
#  5=A101(Rented)    6=A102(UnderMaint) 7=B201(Reserved) 8=B202(Rented)
#  9=V01(Rented)    10=V02(Rented)     11=V03(Rented)
# 12=W01(Rented)    13=W02(Available)  14=W03(Available)

# ── Tenants / Customers ───────────────────────────────────────────────────────

TENANTS = [
	{"customer_name": "Sultan Al-Farsi",             "customer_type": "Individual", "civil_id": "10456789", "tenant_type": "Individual"},   # 0
	{"customer_name": "Huda Al-Lawati",              "customer_type": "Individual", "civil_id": "10567890", "tenant_type": "Individual"},   # 1
	{"customer_name": "Oman Tech Solutions LLC",     "customer_type": "Company",    "civil_id": "",         "tenant_type": "Corporate"},    # 2
	{"customer_name": "Hamad Al-Shanfari",           "customer_type": "Individual", "civil_id": "10678901", "tenant_type": "Individual"},   # 3
	{"customer_name": "Gulf Logistics Oman LLC",     "customer_type": "Company",    "civil_id": "",         "tenant_type": "Corporate"},    # 4
	{"customer_name": "Fatma Al-Maqbali",            "customer_type": "Individual", "civil_id": "10789012", "tenant_type": "Individual"},   # 5
	{"customer_name": "Yousuf Al-Rawahi",            "customer_type": "Individual", "civil_id": "10890123", "tenant_type": "Individual"},   # 6
	{"customer_name": "Salalah Trading Est.",        "customer_type": "Company",    "civil_id": "",         "tenant_type": "Corporate"},    # 7
	{"customer_name": "Aisha Al-Hinai",              "customer_type": "Individual", "civil_id": "10901234", "tenant_type": "Individual"},   # 8
	{"customer_name": "Muscat Freight Co.",          "customer_type": "Company",    "civil_id": "",         "tenant_type": "Corporate"},    # 9
]

# ── Lease Contracts ───────────────────────────────────────────────────────────
# paid_months = how many past schedules to mark as Paid (rest that are past → Overdue)

LEASE_CONTRACTS = [
	# Expiring in ~1 month  →  shows in Expiring Contracts Report
	{"tenant_index": 2, "unit_index": 3,  "start_months_ago": 11, "duration_months": 12, "paid_months": 9},
	# Al-Noor 101 - good payment history
	{"tenant_index": 0, "unit_index": 0,  "start_months_ago": 8,  "duration_months": 12, "paid_months": 7},
	# Al-Noor 102 - 1 overdue month
	{"tenant_index": 1, "unit_index": 1,  "start_months_ago": 5,  "duration_months": 12, "paid_months": 4},
	# Marina A101 - 1 overdue month
	{"tenant_index": 3, "unit_index": 5,  "start_months_ago": 4,  "duration_months": 12, "paid_months": 3},
	# Marina B202 - new contract, all paid so far
	{"tenant_index": 8, "unit_index": 8,  "start_months_ago": 2,  "duration_months": 12, "paid_months": 2},
	# Jabriya V01 - long 24-month contract, 1 overdue
	{"tenant_index": 5, "unit_index": 9,  "start_months_ago": 14, "duration_months": 24, "paid_months": 13},
	# Jabriya V02 - 5 months in, 1 overdue
	{"tenant_index": 6, "unit_index": 10, "start_months_ago": 5,  "duration_months": 12, "paid_months": 4},
	# Jabriya V03 - recent, all paid
	{"tenant_index": 7, "unit_index": 11, "start_months_ago": 3,  "duration_months": 12, "paid_months": 3},
	# Warehouse W01 - corporate, 2 months in
	{"tenant_index": 4, "unit_index": 12, "start_months_ago": 2,  "duration_months": 12, "paid_months": 2},
]

# ── Maintenance Requests ──────────────────────────────────────────────────────

MAINTENANCE_REQUESTS = [
	{
		"unit_index": 0, "tenant_index": 0,
		"issue_type": "Plumbing",   "priority": "High",   "status": "Completed",
		"estimated_cost": 150, "actual_cost": 175,
		"desc": "Water leak under kitchen sink — pipe replaced and sealed.",
	},
	{
		"unit_index": 1, "tenant_index": 1,
		"issue_type": "Electrical", "priority": "Urgent", "status": "In Progress",
		"estimated_cost": 300, "actual_cost": None,
		"desc": "Electrical trip in bedroom sockets. Technician scheduled.",
	},
	{
		"unit_index": 3, "tenant_index": 2,
		"issue_type": "HVAC",       "priority": "Medium", "status": "Open",
		"estimated_cost": 500, "actual_cost": None,
		"desc": "Central AC not cooling adequately in the main office. Needs gas recharge.",
	},
	{
		"unit_index": 5, "tenant_index": 3,
		"issue_type": "Appliance",  "priority": "Low",    "status": "Assigned",
		"estimated_cost": 80, "actual_cost": None,
		"desc": "Washing machine vibrating loudly during spin cycle.",
	},
	{
		"unit_index": 9, "tenant_index": 5,
		"issue_type": "Structural", "priority": "High",   "status": "Completed",
		"estimated_cost": 2000, "actual_cost": 1900,
		"desc": "Hairline crack in external wall due to temperature expansion — sealed and waterproofed.",
	},
	{
		"unit_index": 6, "tenant_index": None,
		"issue_type": "Cleaning",   "priority": "Medium", "status": "In Progress",
		"estimated_cost": 350, "actual_cost": None,
		"desc": "Full deep clean and repainting of studio unit A102 before relisting.",
	},
]


# ── Entry Point ───────────────────────────────────────────────────────────────

def setup():
	frappe.flags.ignore_account_permission = True
	print("\n========================================")
	print("  Property Hub — Demo Data Setup")
	print("========================================\n")

	owner_names    = _create_owners()
	property_names = _create_properties(owner_names)
	unit_names     = _create_units(property_names)
	tenant_names   = _create_tenants()
	_create_lease_contracts(tenant_names, owner_names, property_names, unit_names)
	_finalise_unit_statuses(unit_names)
	_finalise_property_statuses(property_names)
	_create_maintenance_requests(property_names, unit_names, tenant_names)

	frappe.db.commit()
	print("\n========================================")
	print("  Demo data setup complete!")
	print("========================================\n")


# ── Owners ────────────────────────────────────────────────────────────────────

def _create_owners():
	names = []
	for o in OWNERS:
		if frappe.db.exists("Property Owner", o["owner_name"]):
			print(f"  [skip] Owner exists: {o['owner_name']}")
			names.append(o["owner_name"])
			continue
		try:
			doc = frappe.get_doc({"doctype": "Property Owner", **{
				k: v for k, v in o.items()
			}})
			doc.insert(ignore_permissions=True)
			names.append(doc.name)
			print(f"  [+] Owner: {doc.name}")
		except Exception as e:
			frappe.db.rollback()
			print(f"  [!] Owner creation failed for {o['owner_name']}: {e}")
			names.append(o["owner_name"])
	return names


# ── Properties ────────────────────────────────────────────────────────────────

def _create_properties(owner_names):
	names = []
	for p in PROPERTIES:
		if frappe.db.exists("Property", p["property_code"]):
			print(f"  [skip] Property exists: {p['property_code']}")
			names.append(p["property_code"])
			continue
		doc = frappe.get_doc({
			"doctype": "Property",
			"property_name": p["property_name"],
			"property_code": p["property_code"],
			"owner": owner_names[p["owner_index"]],
			"property_type": p["property_type"],
			"address": p["address"],
			"city": p["city"],
			"status": "Available",
		})
		doc.insert(ignore_permissions=True)
		names.append(doc.name)
		print(f"  [+] Property: {doc.name}")
	return names


# ── Units ─────────────────────────────────────────────────────────────────────

def _create_units(property_names):
	names = []
	for u in UNITS:
		prop = property_names[u["prop_index"]]
		existing = frappe.db.get_value(
			"Property Unit", {"property": prop, "unit_number": u["unit_number"]}, "name"
		)
		if existing:
			print(f"  [skip] Unit exists: {existing}")
			names.append(existing)
			continue
		doc = frappe.get_doc({
			"doctype": "Property Unit",
			"unit_number": u["unit_number"],
			"property": prop,
			"floor": u["floor"],
			"unit_type": u["unit_type"],
			"rent_amount": u["rent_amount"],
			"bedrooms": u["bedrooms"],
			"bathrooms": u["bathrooms"],
			"area": u["area"],
			"status": "Available",   # will be updated after leases
		})
		doc.insert(ignore_permissions=True)
		names.append(doc.name)
		print(f"  [+] Unit: {doc.name}")
	return names


# ── Tenants / Customers ───────────────────────────────────────────────────────

def _create_tenants():
	names = []
	default_cg = (
		frappe.db.get_single_value("Selling Settings", "customer_group")
		or _first_customer_group()
		or "All Customer Groups"
	)
	default_territory = _first_territory() or "All Territories"

	for t in TENANTS:
		existing = frappe.db.get_value("Customer", {"customer_name": t["customer_name"]}, "name")
		if existing:
			print(f"  [skip] Tenant exists: {existing}")
			names.append(existing)
			continue
		cg = _get_or_default_cg(t["customer_type"], default_cg)
		doc = frappe.get_doc({
			"doctype": "Customer",
			"customer_name": t["customer_name"],
			"customer_group": cg,
			"territory": default_territory,
			"customer_type": t["customer_type"],
		})
		doc.insert(ignore_permissions=True)
		if t.get("civil_id"):
			frappe.db.set_value("Customer", doc.name, "civil_id", t["civil_id"])
		frappe.db.set_value("Customer", doc.name, "tenant_type", t["tenant_type"])
		names.append(doc.name)
		print(f"  [+] Tenant: {doc.name}")
	return names


def _first_customer_group():
	row = frappe.get_all("Customer Group", limit=1, fields=["name"])
	return row[0].name if row else None


def _first_territory():
	row = frappe.get_all("Territory", limit=1, fields=["name"])
	return row[0].name if row else None


def _get_or_default_cg(customer_type, default_cg):
	guess = "Individual" if customer_type == "Individual" else "Commercial"
	return guess if frappe.db.exists("Customer Group", guess) else default_cg


# ── Lease Contracts & Rent Schedules ─────────────────────────────────────────

def _create_lease_contracts(tenant_names, owner_names, property_names, unit_names):
	for lc_data in LEASE_CONTRACTS:
		tenant     = tenant_names[lc_data["tenant_index"]]
		unit       = unit_names[lc_data["unit_index"]]
		prop_idx   = UNITS[lc_data["unit_index"]]["prop_index"]
		prop       = property_names[prop_idx]
		owner      = owner_names[PROPERTIES[prop_idx]["owner_index"]]
		rent_amt   = UNITS[lc_data["unit_index"]]["rent_amount"]
		start_date = add_months(today(), -lc_data["start_months_ago"])
		end_date   = add_months(start_date, lc_data["duration_months"])

		existing = frappe.db.get_value(
			"Lease Contract", {"tenant": tenant, "unit": unit, "docstatus": 1}, "name"
		)
		if existing:
			print(f"  [skip] Lease exists: {existing}")
			continue

		lc = frappe.get_doc({
			"doctype": "Lease Contract",
			"tenant": tenant,
			"owner": owner,
			"property": prop,
			"unit": unit,
			"start_date": start_date,
			"end_date": end_date,
			"rent_amount": rent_amt,
			"payment_frequency": "Monthly",
			"security_deposit": rent_amt,
			"status": "Draft",
		})
		lc.insert(ignore_permissions=True)
		lc.submit()   # triggers on_submit → generates Rent Schedule rows, sets unit → Rented
		frappe.db.commit()
		print(f"  [+] Lease: {lc.name}  ({tenant} → {unit})")

		_apply_payment_history(lc.name, lc_data["paid_months"])


def _apply_payment_history(lease_contract, paid_months):
	"""
	Mark the first `paid_months` past-due schedules as Paid.
	Any remaining past-due schedules are left as Overdue.
	Future schedules stay Unpaid.
	"""
	past = frappe.get_all(
		"Rent Schedule",
		filters={"lease_contract": lease_contract, "due_date": ["<", today()]},
		fields=["name", "due_date"],
		order_by="due_date asc",
	)
	future = frappe.get_all(
		"Rent Schedule",
		filters={"lease_contract": lease_contract, "due_date": [">=", today()]},
		fields=["name"],
	)

	for i, rs in enumerate(past):
		status = "Paid" if i < paid_months else "Overdue"
		frappe.db.set_value("Rent Schedule", rs.name, "payment_status", status)

	for rs in future:
		frappe.db.set_value("Rent Schedule", rs.name, "payment_status", "Unpaid")


# ── Post-lease status cleanup ─────────────────────────────────────────────────

def _finalise_unit_statuses(unit_names):
	"""Override statuses for non-leased units (Reserved, Under Maintenance, etc.)."""
	for i, u in enumerate(UNITS):
		desired = u["final_status"]
		if desired == "Rented":
			continue   # already set by lease submission
		current = frappe.db.get_value("Property Unit", unit_names[i], "status")
		if current != desired:
			frappe.db.set_value("Property Unit", unit_names[i], "status", desired)
			print(f"  [~] Unit {unit_names[i]} status → {desired}")


def _finalise_property_statuses(property_names):
	"""Set explicit property-level statuses for the demo."""
	for i, p in enumerate(PROPERTIES):
		desired = p["final_status"]
		current = frappe.db.get_value("Property", property_names[i], "status")
		if current != desired:
			frappe.db.set_value("Property", property_names[i], "status", desired)
			print(f"  [~] Property {property_names[i]} status → {desired}")


# ── Maintenance Requests ──────────────────────────────────────────────────────

def _create_maintenance_requests(property_names, unit_names, tenant_names):
	for mr in MAINTENANCE_REQUESTS:
		unit      = unit_names[mr["unit_index"]]
		prop      = property_names[UNITS[mr["unit_index"]]["prop_index"]]
		tenant    = tenant_names[mr["tenant_index"]] if mr["tenant_index"] is not None else None

		existing = frappe.db.get_value(
			"Maintenance Request",
			{"unit": unit, "issue_type": mr["issue_type"]},
			"name",
		)
		if existing:
			print(f"  [skip] Maintenance request exists: {existing}")
			continue

		doc = frappe.get_doc({
			"doctype": "Maintenance Request",
			"property": prop,
			"unit": unit,
			"tenant": tenant,
			"issue_type": mr["issue_type"],
			"priority": mr["priority"],
			"status": mr["status"],
			"description": mr["desc"],
			"estimated_cost": mr["estimated_cost"],
			"actual_cost": mr.get("actual_cost"),
		})
		doc.insert(ignore_permissions=True)
		print(f"  [+] Maintenance: {doc.name}  ({mr['issue_type']} – {mr['status']})")
