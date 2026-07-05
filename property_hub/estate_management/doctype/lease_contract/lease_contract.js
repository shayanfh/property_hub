frappe.ui.form.on('Lease Contract', {
	refresh(frm) {
		if (frm.doc.docstatus === 1) {
			frm.add_custom_button(__('Rent Schedules'), () => {
				frappe.set_route('List', 'Rent Schedule', { lease_contract: frm.doc.name });
			}, __('View'));
			frm.add_custom_button(__('Create Rent Invoice'), () => {
				frappe.call({
					method: 'property_hub.estate_management.doctype.rent_schedule.rent_schedule.create_invoice_for_contract',
					args: { lease_contract: frm.doc.name },
					callback(r) {
						if (r.message) {
							frappe.msgprint(__('Invoice created: ') + r.message);
						}
					}
				});
			});
		}
	},
	unit(frm) {
		if (frm.doc.unit) {
			frappe.db.get_value('Property Unit', frm.doc.unit, ['rent_amount', 'property'], (r) => {
				if (r) {
					frm.set_value('rent_amount', r.rent_amount);
					frm.set_value('property', r.property);
				}
			});
		}
	}
});
