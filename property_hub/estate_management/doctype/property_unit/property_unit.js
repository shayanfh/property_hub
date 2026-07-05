frappe.ui.form.on('Property Unit', {
	refresh(frm) {
		frm.add_custom_button(__('Lease Contracts'), () => {
			frappe.set_route('List', 'Lease Contract', { unit: frm.doc.name });
		}, __('View'));
		if (frm.doc.status === 'Available' && !frm.is_new()) {
			frm.add_custom_button(__('New Lease'), () => {
				frappe.new_doc('Lease Contract', {
					unit: frm.doc.name,
					property: frm.doc.property,
					rent_amount: frm.doc.rent_amount,
				});
			});
		}
	}
});
