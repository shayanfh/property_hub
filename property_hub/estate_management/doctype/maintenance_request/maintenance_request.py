import frappe
from frappe.model.document import Document


class MaintenanceRequest(Document):
	def validate(self):
		if self.estimated_cost and self.estimated_cost < 0:
			frappe.throw("Estimated cost cannot be negative.")
		if self.actual_cost and self.actual_cost < 0:
			frappe.throw("Actual cost cannot be negative.")
		if self.status == "Completed" and not self.actual_cost:
			frappe.msgprint("Consider adding actual cost for completed requests.", indicator="orange", alert=True)

	def on_update(self):
		if self.status in ("In Progress", "Assigned"):
			frappe.db.set_value("Property Unit", self.unit, "status", "Under Maintenance")
		elif self.status in ("Completed", "Cancelled"):
			active_mr = frappe.db.count("Maintenance Request", {
				"unit": self.unit, "status": ["in", ["Open", "Assigned", "In Progress"]]
			})
			if not active_mr:
				frappe.db.set_value("Property Unit", self.unit, "status", "Available")
